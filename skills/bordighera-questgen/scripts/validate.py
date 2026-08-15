#!/usr/bin/env python3
import json
import math
import re
import sys

AREA_LAT_MIN, AREA_LAT_MAX = 43.777, 43.781
AREA_LNG_MIN, AREA_LNG_MAX = 7.668, 7.677
AREA_EPS = 0.0005
WAYPOINT_ERROR_M = 150.0
WAYPOINT_WARNING_M = 50.0
DUPLICATE_M = 1.0
ROUTE_WARNING_M = 3500.0
ID_RE = re.compile(r"^[a-z0-9_]{1,100}$")
PLACEHOLDERS = ("{path}", "{name}", "{url}", "{tags}")
REQUIRED_HASHTAGS = ("BordigheraQuest", "Bordighera")

MASTER_REQUIRED = (
    "id", "name", "subtitle", "description", "hint", "start", "end",
    "icon", "type", "enabled", "collectible", "reward", "quests",
)
MASTER_OPTIONAL = ("hintImage",)
QUEST_COMMON = ("id", "name", "subtitle", "lat", "lng", "description", "hint", "icon")
QUEST_OPTIONAL = ("hintImage",)
REWARD_REQUIRED = ("sponsorId", "title", "description", "share")
SHARE_REQUIRED = ("text", "hashtags", "facebook", "instagram")

errors = []
warnings = []


def error(ctx, msg):
    errors.append(f"[{ctx}] {msg}")


def warning(ctx, msg):
    warnings.append(f"[{ctx}] {msg}")


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def check_localized(ctx, obj, field, where):
    if not isinstance(obj, dict):
        error(ctx, f"{where}.{field} deve essere un oggetto {{it, en}}")
        return False
    ok = True
    for lang in ("it", "en"):
        val = obj.get(lang)
        if not isinstance(val, str) or not val.strip():
            error(ctx, f"{where}.{field}.{lang} mancante o vuoto")
            ok = False
    extra = set(obj) - {"it", "en"}
    if extra:
        error(ctx, f"{where}.{field} ha chiavi non previste: {sorted(extra)}")
        ok = False
    return ok


def in_area(ctx, lat, lng, where):
    ok = True
    if not (AREA_LAT_MIN - AREA_EPS <= lat <= AREA_LAT_MAX + AREA_EPS):
        error(ctx, f"{where}: lat {lat} fuori dall'area di gioco ({AREA_LAT_MIN}-{AREA_LAT_MAX})")
        ok = False
    if not (AREA_LNG_MIN - AREA_EPS <= lng <= AREA_LNG_MAX + AREA_EPS):
        error(ctx, f"{where}: lng {lng} fuori dall'area di gioco ({AREA_LNG_MIN}-{AREA_LNG_MAX})")
        ok = False
    return ok


def haversine(a, b):
    lat1, lng1, lat2, lng2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    dlat, dlng = lat2 - lat1, lng2 - lng1
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    return 2 * 6371000 * math.asin(math.sqrt(h))


def check_coords_pair(ctx, obj, where):
    if not isinstance(obj, dict):
        error(ctx, f"{where} deve essere un oggetto {{lat, lng}}")
        return None
    extra = set(obj) - {"lat", "lng"}
    if extra:
        error(ctx, f"{where} ha chiavi non previste: {sorted(extra)}")
    lat, lng = obj.get("lat"), obj.get("lng")
    if not is_num(lat) or not is_num(lng):
        error(ctx, f"{where}.lat/.lng devono essere numeri")
        return None
    in_area(ctx, lat, lng, where)
    return (lat, lng)


def check_id(ctx, value, where):
    if not isinstance(value, str) or not ID_RE.match(value):
        error(ctx, f"{where}: id non valido (atteso minuscolo [a-z0-9_], 1-100 caratteri): {value!r}")


def check_reward(ctx, reward):
    if not isinstance(reward, dict):
        error(ctx, "reward deve essere un oggetto")
        return
    extra = set(reward) - set(REWARD_REQUIRED)
    if extra:
        error(ctx, f"reward ha campi non previsti: {sorted(extra)}")
    for f in REWARD_REQUIRED:
        if f not in reward:
            error(ctx, f"reward.{f} mancante")
    sponsor = reward.get("sponsorId")
    if not isinstance(sponsor, str) or not sponsor.strip() or sponsor != sponsor.lower() or re.search(r"\s", sponsor):
        error(ctx, f"reward.sponsorId non valido (minuscolo, senza spazi): {sponsor!r}")
    check_localized(ctx, reward.get("title"), "title", "reward")
    check_localized(ctx, reward.get("description"), "description", "reward")
    share = reward.get("share")
    if not isinstance(share, dict):
        error(ctx, "reward.share deve essere un oggetto")
        return
    extra = set(share) - set(SHARE_REQUIRED)
    if extra:
        error(ctx, f"reward.share ha campi non previsti: {sorted(extra)}")
    for f in SHARE_REQUIRED:
        if f not in share:
            error(ctx, f"reward.share.{f} mancante")
    text = share.get("text")
    if check_localized(ctx, text, "text", "reward.share"):
        for lang in ("it", "en"):
            missing = [p for p in PLACEHOLDERS if p not in text[lang]]
            if missing:
                error(ctx, f"reward.share.text.{lang} mancano i placeholder: {' '.join(missing)}")
    hashtags = share.get("hashtags")
    if not isinstance(hashtags, list) or not hashtags or not all(isinstance(h, str) and h.strip() for h in hashtags):
        error(ctx, "reward.share.hashtags deve essere un array di stringhe non vuote")
    else:
        missing = [t for t in REQUIRED_HASHTAGS if t not in hashtags]
        if missing:
            error(ctx, f"reward.share.hashtags deve includere almeno {missing}")
    for key, domain in (("facebook", "facebook.com"), ("instagram", "instagram.com")):
        url = share.get(key)
        if not isinstance(url, str) or not url.startswith("https://") or domain not in url:
            error(ctx, f"reward.share.{key} deve essere un URL https valido ({domain})")


def check_quest(ctx, q, idx, seen_ids):
    label = f"quests[{idx}]" if not isinstance(q, dict) else f"quests[{idx}] ({q.get('id', '?')})"
    if not isinstance(q, dict):
        error(label, "la sotto-quest deve essere un oggetto")
        return
    qtype = q.get("type", "photo")
    if qtype not in ("photo", "word", "moving"):
        error(label, f"type non valido: {qtype!r} (atteso photo, word o moving)")
    allowed = set(QUEST_COMMON) | set(QUEST_OPTIONAL) | {"type"}
    if qtype == "word":
        allowed.add("answers")
    elif qtype == "moving":
        allowed.update(("speed", "waypoints"))
    extra = set(q) - allowed
    if extra:
        error(label, f"campi non previsti: {sorted(extra)}")
    for f in QUEST_COMMON:
        if f not in q:
            error(label, f"campo obbligatorio mancante: {f}")
    check_id(label, q.get("id"), f"quests[{idx}].id")
    if isinstance(q.get("id"), str) and ID_RE.match(q.get("id", "")):
        if q["id"] in seen_ids:
            error(label, f"id duplicato: {q['id']!r}")
        seen_ids.add(q["id"])
    check_localized(label, q.get("name"), "name", label)
    check_localized(label, q.get("subtitle"), "subtitle", label)
    check_localized(label, q.get("description"), "description", label)
    check_localized(label, q.get("hint"), "hint", label)
    if q.get("icon") != "quest":
        error(label, f"icon deve essere 'quest', trovato {q.get('icon')!r}")
    if "hintImage" in q and (not isinstance(q["hintImage"], str) or not q["hintImage"].strip()):
        error(label, "hintImage deve essere una stringa non vuota")
    lat, lng = q.get("lat"), q.get("lng")
    position = None
    if not is_num(lat) or not is_num(lng):
        error(label, "lat/lng devono essere numeri")
    else:
        in_area(label, lat, lng, f"quests[{idx}]")
        position = (lat, lng)
    if qtype == "word":
        answers = q.get("answers")
        if not isinstance(answers, list) or len(answers) < 2:
            error(label, "answers deve essere un array con almeno 2 varianti reali")
        else:
            for i, a in enumerate(answers):
                if not isinstance(a, str) or not a.strip():
                    error(label, f"answers[{i}] deve essere una stringa non vuota")
                    continue
                if a != a.lower():
                    error(label, f"answers[{i}] non è minuscolo: {a!r}")
                if re.search(r"[^\w\s]", a, re.UNICODE):
                    error(label, f"answers[{i}] contiene punteggiatura: {a!r}")
    elif qtype == "moving":
        speed = q.get("speed")
        if not is_num(speed) or not (2 <= speed <= 4):
            error(label, f"speed deve essere un numero tra 2 e 4, trovato {speed!r}")
        wps = q.get("waypoints")
        if not isinstance(wps, list) or len(wps) < 5:
            error(label, "waypoints deve essere un array di almeno 5 coppie [lat, lng]")
        else:
            prev = None
            for i, wp in enumerate(wps):
                if not (isinstance(wp, list) and len(wp) == 2 and is_num(wp[0]) and is_num(wp[1])):
                    error(label, f"waypoints[{i}] deve essere una coppia [lat, lng] numerica")
                    prev = None
                    continue
                in_area(label, wp[0], wp[1], f"waypoints[{i}]")
                if prev is not None:
                    d = haversine(prev, wp)
                    if d > WAYPOINT_ERROR_M:
                        error(label, f"distanza waypoints[{i-1}]->[{i}] = {d:.0f} m (max {WAYPOINT_ERROR_M:.0f} m)")
                    elif d > WAYPOINT_WARNING_M:
                        warning(label, f"distanza waypoints[{i-1}]->[{i}] = {d:.0f} m (consigliate poche decine di metri)")
                prev = wp
    return position


def validate(data):
    ctx = "master"
    if "masterQuests" in data:
        error(ctx, "wrapper 'masterQuests' non ammesso: il file deve contenere la MasterQuest diretta")
        return
    extra = set(data) - set(MASTER_REQUIRED) - set(MASTER_OPTIONAL)
    if extra:
        error(ctx, f"campi non previsti: {sorted(extra)}")
        if "lat" in extra or "lng" in extra:
            error(ctx, "usare start/end come da esempio di riferimento, non lat/lng diretti")
    for f in MASTER_REQUIRED:
        if f not in data:
            error(ctx, f"campo obbligatorio mancante: {f}")
    check_id(ctx, data.get("id"), "id")
    seen_ids = {data["id"]} if isinstance(data.get("id"), str) else set()
    for f in ("name", "subtitle", "description", "hint"):
        check_localized(ctx, data.get(f), f, "master")
    if data.get("icon") != "quest":
        error(ctx, f"icon deve essere 'quest', trovato {data.get('icon')!r}")
    if data.get("type") != "master":
        error(ctx, f"type deve essere 'master', trovato {data.get('type')!r}")
    if data.get("enabled") is not True:
        error(ctx, "enabled deve essere true")
    if "hintImage" in data and (not isinstance(data["hintImage"], str) or not data["hintImage"].strip()):
        error(ctx, "hintImage deve essere una stringa non vuota")
    if not isinstance(data.get("collectible"), str) or not data["collectible"].strip():
        error(ctx, "collectible deve essere una stringa non vuota")
    check_reward(ctx, data.get("reward"))
    points = {}
    start = check_coords_pair(ctx, data.get("start"), "start")
    end = check_coords_pair(ctx, data.get("end"), "end")
    if start:
        points["master.start"] = start
    if end:
        points["master.end"] = end
    quests = data.get("quests")
    if not isinstance(quests, list):
        error(ctx, "quests deve essere un array")
        quests = []
    types = {}
    for i, q in enumerate(quests):
        pos = check_quest(ctx, q, i, seen_ids)
        qid = q.get("id") if isinstance(q, dict) else None
        if isinstance(q, dict) and pos:
            points[f"quests[{i}] ({qid})"] = pos
        if isinstance(q, dict):
            types[q.get("type", "photo")] = types.get(q.get("type", "photo"), 0) + 1
    if len(quests) != 5:
        error(ctx, f"quests deve contenere esattamente 5 sotto-quest, trovate {len(quests)}")
    expected = {"photo": 1, "word": 2, "moving": 2}
    for t, n in expected.items():
        if types.get(t, 0) != n:
            error(ctx, f"composizione errata: attese {n} tappe '{t}', trovate {types.get(t, 0)}")
    names = list(points)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            d = haversine(points[names[i]], points[names[j]])
            if d < DUPLICATE_M:
                error(ctx, f"punti coincidenti (~{d:.1f} m): {names[i]} e {names[j]}")
    route_pts = []
    if start:
        route_pts.append(start)
    for i, q in enumerate(quests):
        if isinstance(q, dict) and is_num(q.get("lat")) and is_num(q.get("lng")):
            route_pts.append((q["lat"], q["lng"]))
    if end:
        route_pts.append(end)
    if len(route_pts) >= 2 and not errors:
        total = sum(haversine(route_pts[k], route_pts[k + 1]) for k in range(len(route_pts) - 1))
        if total > ROUTE_WARNING_M:
            warning(ctx, f"percorso complessivo ~{total:.0f} m: verifica sia percorribile a piedi in 15-40 minuti")


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "masterquest.json"
    if len(sys.argv) > 2:
        print(f"Uso: validate.py [masterquest.json]", file=sys.stderr)
        return 2
    try:
        with open(path, "r", encoding="utf-8") as fh:
            raw = fh.read()
    except OSError as e:
        print(f"ERRORE: impossibile leggere {path}: {e}", file=sys.stderr)
        return 2
    stripped = raw.strip()
    if "```" in raw:
        print("ERRORE: il file contiene backtick: deve contenere solo JSON, senza blocchi di codice", file=sys.stderr)
        return 1
    if not stripped.startswith("{") or not stripped.endswith("}"):
        print("ERRORE: il file deve contenere un unico oggetto JSON senza testo aggiuntivo", file=sys.stderr)
        return 1
    try:
        data = json.loads(stripped)
    except json.JSONDecodeError as e:
        print(f"ERRORE: JSON non valido: {e}", file=sys.stderr)
        return 1
    if not isinstance(data, dict):
        print("ERRORE: il file deve contenere un unico oggetto JSON (MasterQuest)", file=sys.stderr)
        return 1
    validate(data)
    if warnings:
        for w in warnings:
            print(f"AVVISO: {w}")
    if errors:
        for e in errors:
            print(f"ERRORE: {e}")
        print(f"\n{len(errors)} errori, {len(warnings)} avvisi in {path}")
        return 1
    if warnings:
        print(f"{len(warnings)} avvisi in {path}")
    print(f"OK: {path} è una MasterQuest valida")
    return 0


if __name__ == "__main__":
    sys.exit(main())
