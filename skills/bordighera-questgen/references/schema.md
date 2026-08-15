# Schema JSON — MasterQuest

Fonte di verità per la struttura dell'output di `bordighera-questgen`. Non
inventare campi, non ometterne, non rinominarli, non cambiare l'ordine
suggerito.

## Oggetto top-level

L'output è un **oggetto `MasterQuest` diretto** (senza wrapper `masterQuests`).
Il risultato della generazione viene scritto nel file `masterquest.json` nella
cartella corrente di lavoro.

```json
{ /* esattamente 1 <MasterQuest> */ }
```

## `<MasterQuest>`

Campi obbligatori: `id`, `name`, `subtitle`, `description`, `hint`, `start`,
`end`, `icon`, `type`, `enabled`, `collectible`, `reward`, `quests`.
Campo opzionale: `hintImage`.

| Campo | Tipo | Regole |
| --- | --- | --- |
| `id` | string | Unico, `[a-z0-9_]`, 1-100 caratteri, minuscolo. Formato suggerito: slug del tema, eventualmente con suffisso (`masterquestname_timestamp`, es. `masterquest_sentiero_pirati`). Vietati spazi, trattini, punti, maiuscole. |
| `name` | `{ it, en }` | Titolo del percorso, tono narrativo accattivante. |
| `subtitle` | `{ it, en }` | Frase breve che invita ad accettare la quest. |
| `description` | `{ it, en }` | Descrizione del percorso e dell'avventura. |
| `hint` | `{ it, en }` | Indizio su come iniziare (raggiungere il punto giallo sulla mappa). |
| `start` | `{ lat, lng }` | Coordinate del punto di partenza/accettazione della master, sempre presso un POI verificato di `references/locations.json` (vedi `coordinates.md`). |
| `end` | `{ lat, lng }` | Coordinate del punto di arrivo/riscatto presso lo sponsor, sempre presso un POI verificato di `references/locations.json`. |
| `icon` | string | Sempre `"quest"`. |
| `type` | string | Sempre `"master"`. |
| `enabled` | boolean | Sempre `true`. |
| `hintImage` | string | Opzionale: percorso immagine, es. `sponsor/premi/<sponsor>-premio.webp`. |
| `collectible` | string | Percorso del modello collezionabile sbloccato al completamento, es. `public/models/<slug>/mq_<slug>.obj`. |
| `reward` | oggetto | Vedi sotto. |
| `quests` | array | Esattamente 5 sotto-quest: 1 `photo`, 2 `word`, 2 `moving`. |

### `reward`

| Campo | Tipo | Regole |
| --- | --- | --- |
| `sponsorId` | string | Id dello sponsor che finanzia il premio (minuscolo, senza spazi). |
| `price` | integer | **Opzionale.** Prezzo in monete per acquistare direttamente il collezionabile senza completare il percorso. Assente o `0` = non acquistabile. Se presente, deve essere un intero positivo (es. `200`). |
| `title` | `{ it, en }` | Titolo del premio (es. "Il tuo premio ti aspetta"). |
| `description` | `{ it, en }` | Cosa e come riscattare il premio presso lo sponsor; può contenere `<strong>` per evidenziare il premio. |
| `share.text` | `{ it, en }` | Testo di condivisione con placeholder `{path}`, `{name}`, `{url}`, `{tags}`. |
| `share.hashtags` | array&lt;string&gt; | Almeno `["BordigheraQuest","Bordighera"]`. |
| `share.facebook` | string | URL pagina Facebook dello sponsor. |
| `share.instagram` | string | URL pagina Instagram dello sponsor. |

## `<SottoQuest>` — campi comuni a tutti i tipi

| Campo | Tipo | Regole |
| --- | --- | --- |
| `id` | string | Unico, minuscolo `[a-z0-9_]`, 1-100 caratteri. Formato suggerito: slug della tappa, eventualmente con suffisso (`questname_timestamp`, es. `statua_regina_1234567890`). Non richiede prefisso per tipo. |
| `name` | `{ it, en }` | Nome evocativo della tappa. |
| `subtitle` | `{ it, en }` | Frase breve e misteriosa. |
| `lat` / `lng` | number | Posizione reale della tappa a Bordighera, **sempre presso un POI verificato** di `references/locations.json` (vedi `coordinates.md`). |
| `description` | `{ it, en }` | Narrazione atmosferica + cosa fare. Per `photo`: "scatta una foto del..."; per `word`: la domanda precisa. |
| `hint` | `{ it, en }` | Indizio enigmatico, senza rivelare la risposta. |
| `icon` | string | Sempre `"quest"`. |
| `hintImage` | string | Opzionale: immagine della tappa (es. `data:image/webp,...`). |

## Campi specifici per tipo

### 1. `photo`

`type` omesso oppure `"type": "photo"`. Nessun campo aggiuntivo oltre a
quelli comuni.

### 2. `word` — `"type": "word"`

| Campo | Tipo | Regole |
| --- | --- | --- |
| `answers` | array&lt;string&gt; | Risposte esatte accettate, **tutte minuscole, senza punteggiatura**, con **più varianti reali** in italiano e inglese (sinonimi, forme senza apostrofi, ecc.). Esempio: `["serpente","snake","serpent","vipera","biscia"]`. |

### 3. `moving` — `"type": "moving"`

| Campo | Tipo | Regole |
| --- | --- | --- |
| `speed` | number | Velocità del bersaglio, valori realistici 2-4. |
| `waypoints` | array&lt;[lat, lng]&gt; | Almeno 5 coppie di coordinate che formano il percorso di pattuglia, che deve seguire una **polilinea verificata** di `references/locations.json` (distanza tra waypoint di poche decine di metri). Vedi `coordinates.md`. |

## Regole di formato dell'output

- Il risultato è un **unico oggetto JSON** (MasterQuest) privo di testo
  aggiuntivo, scritto nel file `masterquest.json` nella cartella corrente
  di lavoro.
- Nessun campo extra rispetto allo schema, nessun campo mancante.
- Nessun commento, nessuna virgola finale (trailing comma), nessun backtick
  nel file: JSON valido.
