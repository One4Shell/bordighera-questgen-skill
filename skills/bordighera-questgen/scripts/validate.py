#!/usr/bin/env python3
"""
validate.py — valida il file "masterquest.json" generato dalla skill
bordighera-questgen rispetto allo schema atteso.

Uso:
    python3 validate.py path/to/masterquest.json
    cat masterquest.json | python3 validate.py -

Compatibilità: accetta sia il file JSON "puro" (oggetto MasterQuest diretto,
senza wrapper) sia la vecchia forma con prefisso "masterquest output {...}".

Esce con codice 0 se l'output è valido, 1 se ci sono errori (che vengono
stampati su stderr, uno per riga).
"""

from __future__ import annotations

import json
import re
import sys

PREFIX = "masterquest output "

LAT_MIN, LAT_MAX = 43.777, 43.781
LNG_MIN, LNG_MAX = 7.668, 7.677

ID_RE = re.compile(r"^[a-z0-9_]{1,100}$")
LANG_KEYS = {"it", "en"}


def fail(errors: list[str], msg: str) -> None:
    errors.append(msg)


def check_lang_obj(obj, path, errors):
    if not isinstance(obj, dict):
        fail(errors, f"{path}: atteso oggetto {{it, en}}, trovato {type(obj).__name__}")
        return
    missing = LANG_KEYS - obj.keys()
    if missing:
        fail(errors, f"{path}: mancano le chiavi lingua {sorted(missing)}")
    for k, v in obj.items():
        if k in LANG_KEYS and not isinstance(v, str):
            fail(errors, f"{path}.{k}: atteso stringa")


def check_coords(lat, lng, path, errors):
    if not isinstance(lat, (int, float)) or not isinstance(lng, (int, float)):
        fail(errors, f"{path}: lat/lng devono essere numeri")
        return
    if not (LAT_MIN <= lat <= LAT_MAX):
        fail(errors, f"{path}: lat={lat} fuori dall'area di gioco [{LAT_MIN}, {LAT_MAX}]")
    if not (LNG_MIN <= lng <= LNG_MAX):
        fail(errors, f"{path}: lng={lng} fuori dall'area di gioco [{LNG_MIN}, {LNG_MAX}]")


def check_subquest(q, index, errors, seen_ids):
    path = f"quests[{index}]"
    qtype = q.get("type", "photo")

    for field in ("id", "name", "subtitle", "lat", "lng", "description", "hint", "icon"):
        if field not in q:
            fail(errors, f"{path}: campo obbligatorio mancante '{field}'")

    qid = q.get("id", "")
    if not isinstance(qid, str) or not ID_RE.match(qid):
        fail(errors, f"{path}.id: '{qid}' non rispetta il pattern [a-z0-9_], 1-100 caratteri")
    else:
        if qid in seen_ids:
            fail(errors, f"{path}.id: '{qid}' duplicato")
        seen_ids.add(qid)

    for f in ("name", "subtitle", "description", "hint"):
        if f in q:
            check_lang_obj(q[f], f"{path}.{f}", errors)

    if "lat" in q and "lng" in q:
        check_coords(q["lat"], q["lng"], path, errors)

    if q.get("icon") != "quest":
        fail(errors, f"{path}.icon: atteso 'quest'")

    if qtype == "word":
        answers = q.get("answers")
        if not isinstance(answers, list) or not answers:
            fail(errors, f"{path}.answers: atteso array non vuoto di stringhe")
        else:
            for a in answers:
                if not isinstance(a, str) or a != a.lower():
                    fail(errors, f"{path}.answers: '{a}' deve essere una stringa minuscola")
                elif re.search(r"[^\w\s]", a, flags=re.UNICODE):
                    fail(errors, f"{path}.answers: '{a}' non deve contenere punteggiatura")
            if len(answers) < 2:
                fail(errors, f"{path}.answers: servono più varianti reali (trovate {len(answers)})")

    elif qtype == "moving":
        speed = q.get("speed")
        if not isinstance(speed, (int, float)) or not (2 <= speed <= 4):
            fail(errors, f"{path}.speed: atteso numero realistico 2-4, trovato {speed!r}")
        waypoints = q.get("waypoints")
        if not isinstance(waypoints, list) or len(waypoints) < 5:
            fail(errors, f"{path}.waypoints: attesi almeno 5 waypoint, trovati {len(waypoints) if isinstance(waypoints, list) else 0}")
        else:
            for i, wp in enumerate(waypoints):
                if not (isinstance(wp, list) and len(wp) == 2):
                    fail(errors, f"{path}.waypoints[{i}]: atteso [lat, lng]")
                    continue
                check_coords(wp[0], wp[1], f"{path}.waypoints[{i}]", errors)

    elif qtype not in ("photo",):
        fail(errors, f"{path}.type: valore non valido '{qtype}' (atteso photo, word o moving)")


def check_master_quest(mq, errors):
    for field in (
        "id", "name", "subtitle", "description", "hint", "lat", "lng",
        "icon", "type", "enabled", "collectible", "reward", "quests",
    ):
        if field not in mq:
            fail(errors, f"masterQuest: campo obbligatorio mancante '{field}'")

    mqid = mq.get("id", "")
    if not isinstance(mqid, str) or not ID_RE.match(mqid):
        fail(errors, f"masterQuest.id: '{mqid}' deve rispettare [a-z0-9_], 1-100 caratteri")

    for f in ("name", "subtitle", "description", "hint"):
        if f in mq:
            check_lang_obj(mq[f], f"masterQuest.{f}", errors)

    if "lat" in mq and "lng" in mq:
        check_coords(mq["lat"], mq["lng"], "masterQuest", errors)

    if mq.get("icon") != "quest":
        fail(errors, "masterQuest.icon: atteso 'quest'")
    if mq.get("type") != "master":
        fail(errors, "masterQuest.type: atteso 'master'")
    if mq.get("enabled") is not True:
        fail(errors, "masterQuest.enabled: atteso true")

    reward = mq.get("reward")
    if not isinstance(reward, dict):
        fail(errors, "masterQuest.reward: atteso oggetto")
    else:
        for f in ("sponsorId", "title", "description", "share", "sponsorPin"):
            if f not in reward:
                fail(errors, f"masterQuest.reward: campo obbligatorio mancante '{f}'")
        for f in ("title", "description"):
            if f in reward:
                check_lang_obj(reward[f], f"masterQuest.reward.{f}", errors)
        share = reward.get("share")
        if not isinstance(share, dict):
            fail(errors, "masterQuest.reward.share: atteso oggetto")
        else:
            if "text" in share:
                check_lang_obj(share["text"], "masterQuest.reward.share.text", errors)
                for lang in LANG_KEYS:
                    txt = share["text"].get(lang, "") if isinstance(share["text"], dict) else ""
                    for placeholder in ("{path}", "{name}", "{url}", "{tags}"):
                        if placeholder not in txt:
                            fail(errors, f"masterQuest.reward.share.text.{lang}: manca il placeholder '{placeholder}'")
            hashtags = share.get("hashtags")
            if not isinstance(hashtags, list) or not {"BordigheraQuest", "Bordighera"}.issubset(set(hashtags)):
                fail(errors, "masterQuest.reward.share.hashtags: deve includere almeno ['BordigheraQuest','Bordighera']")
        pin = reward.get("sponsorPin")
        if not isinstance(pin, str) or not re.match(r"^\d{4}$", pin):
            fail(errors, f"masterQuest.reward.sponsorPin: '{pin}' deve essere una stringa di 4 cifre")

    quests = mq.get("quests")
    if not isinstance(quests, list) or len(quests) != 5:
        fail(errors, f"masterQuest.quests: attese esattamente 5 sotto-quest, trovate {len(quests) if isinstance(quests, list) else 0}")
        quests = quests if isinstance(quests, list) else []

    seen_ids = set()
    type_counts = {"photo": 0, "word": 0, "moving": 0}
    for i, q in enumerate(quests):
        if not isinstance(q, dict):
            fail(errors, f"quests[{i}]: atteso oggetto")
            continue
        qtype = q.get("type", "photo")
        if qtype in type_counts:
            type_counts[qtype] += 1
        check_subquest(q, i, errors, seen_ids)

    if quests:
        expected = {"photo": 1, "word": 2, "moving": 2}
        if type_counts != expected:
            fail(
                errors,
                f"masterQuest.quests: composizione attesa {expected}, trovata {type_counts}",
            )


def validate(raw_text: str) -> list[str]:
    errors: list[str] = []
    text = raw_text.strip()

    if text.startswith(PREFIX):
        json_part = text[len(PREFIX):]
    else:
        json_part = text

    try:
        data = json.loads(json_part)
    except json.JSONDecodeError as e:
        fail(errors, f"JSON non valido: {e}")
        return errors

    if not isinstance(data, dict):
        fail(errors, "Atteso oggetto MasterQuest diretto (oppure wrapper con chiave 'masterQuests')")
        return errors

    if "masterQuests" in data:
        mqs = data["masterQuests"]
        if not isinstance(mqs, list) or len(mqs) != 1:
            fail(errors, f"'masterQuests' deve contenere esattamente 1 elemento, trovati {len(mqs) if isinstance(mqs, list) else 0}")
            return errors
        data = mqs[0]

    check_master_quest(data, errors)
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    src = sys.argv[1]
    if src == "-":
        raw_text = sys.stdin.read()
    else:
        with open(src, "r", encoding="utf-8") as f:
            raw_text = f.read()

    errors = validate(raw_text)
    if errors:
        print(f"Trovati {len(errors)} problema/i:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print("OK: l'output rispetta lo schema di bordighera-questgen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())