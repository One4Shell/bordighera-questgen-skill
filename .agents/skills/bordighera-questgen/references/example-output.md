# Esempio di riferimento (struttura output)

Questo è l'esempio **obbligatorio** di riferimento per struttura, ordine dei
campi, tipi e stile. Mostra l'output completo con **5 tappe** (1 `photo`,
2 `word`, 2 `moving`), come richiesto dallo schema.

Il risultato della generazione viene scritto in due file JSON nella cartella
corrente di lavoro: **`masterquest.json`** (oggetto JSON valido senza alcun
testo aggiuntivo; nessun wrapper `masterQuests`, nessuna riga di prefisso,
nessun blocco markdown, nessun backtick) e **`images.json`** (array di entry
`{id, hintImage, prompt}` per le tappe `word`/`moving`).

## Struttura del file `masterquest.json`

```json
{
  "id": "masterquest_sentiero_pirati",
  "name": {
    "it": "Il Sentiero dei Pirati",
    "en": "The Pirate's Trail"
  },
  "subtitle": {
    "it": "Ogni esploratore ha bisogno di un punto di partenza.",
    "en": "Every explorer needs a starting point."
  },
  "description": {
    "it": "Completa le tappe di questo percorso e scopri i segreti nascosti di Bordighera.",
    "en": "Complete the stages of this path and uncover Bordighera's hidden secrets."
  },
  "hint": {
    "it": "Raggiungi il punto indicato sulla mappa e attiva la missione.",
    "en": "Reach the point shown on the map and activate the mission."
  },
  "start": {
    "lat": 43.778119,
    "lng": 7.673973
  },
  "end": {
    "lat": 43.779352,
    "lng": 7.672379
  },
  "icon": "quest",
  "type": "master",
  "enabled": true,
  "hintImage": "sponsor/premi/premio.webp",
  "collectible": "public/models/masterquest_sentiero_pirati/mq_marmura.obj",
  "reward": {
    "price": 200,
    "sponsorId": "nothing",
    "title": {
      "it": "Il tuo premio ti aspetta",
      "en": "Your prize awaits you"
    },
    "description": {
      "it": "Hai completato il tuo percorso recati nel punto indicato nella mappa per riscattare il tui premio: <strong>Carta Collezionabile</strong>",
      "en": "You have completed your path. Go to the spot shown on the map to get your prize: <strong>Collectible Card</strong>."
    },
    "share": {
      "text": {
        "it": "Ho completato la Bordighera Quest - {path} con {name}! 🎉\n\n▶ Gioca ora: {url}\n#{tags}",
        "en": "I completed the Bordighera Quest - {path} as {name}! 🎉\n\n▶ Play now: {url}\n#{tags}"
      },
      "hashtags": [
        "BordigheraQuest",
        "Bordighera"
      ],
      "facebook": "https://www.facebook.com/",
      "instagram": "https://www.instagram.com/"
    }
  },
  "quests": [
    {
      "id": "guardia_pietra_1712345678",
      "name": {
        "it": "La Guardia di Pietra",
        "en": "The Stone Guard"
      },
      "subtitle": {
        "it": "La torre che scrutava il mare.",
        "en": "The tower that watched the sea."
      },
      "lat": 43.780551,
      "lng": 7.673551,
      "description": {
        "it": "Inquadra il campanile della chiesa che un tempo serviva da torre di avvistamento contro i pirati.",
        "en": "Frame the church bell-tower that once served as a lookout tower against pirates."
      },
      "hint": {
        "it": "Dalla torre più alta del borgo, dove la vigilia non dormiva mai.",
        "en": "From the tallest tower of the old town, where the watch never slept."
      },
      "icon": "quest"
    },
    {
      "id": "bocca_fuoco_1712345679",
      "name": {
        "it": "La Bocca di Fuoco",
        "en": "The Fire Mouth"
      },
      "subtitle": {
        "it": "Un nome scolpito nella pietra.",
        "en": "A name carved in stone."
      },
      "lat": 43.777709,
      "lng": 7.673454,
      "description": {
        "it": "Quale nome è scritto alla base della statua del marabutto, accanto ai cannoni?",
        "en": "Which name is written at the base of the Marabutto statue, beside the cannons?"
      },
      "hint": {
        "it": "Chi pregava qui, secondo la leggenda, era un santone dal nome lontano.",
        "en": "According to legend, whoever prayed here was a holy man from a distant land."
      },
      "icon": "quest",
      "type": "word",
      "hintImage": "public/images/quests/bocca_fuoco_1712345679.webp",
      "answers": [
        "marabutto",
        "marabuto"
      ]
    },
    {
      "id": "confratelli_1712345680",
      "name": {
        "it": "I Confratelli del Segreto",
        "en": "The Secret Brotherhood"
      },
      "subtitle": {
        "it": "Una porta dietro la chiesa.",
        "en": "A door behind the church."
      },
      "lat": 43.780285,
      "lng": 7.674057,
      "description": {
        "it": "L'oratorio nascondeva un nome antico: che cosa custodiva la confraternita?",
        "en": "The oratory hid an ancient name: what did the brotherhood guard?"
      },
      "hint": {
        "it": "Seguivano i condannati fino all'ultimo passo.",
        "en": "They followed the condemned to their last step."
      },
      "icon": "quest",
      "type": "word",
      "hintImage": "public/images/quests/confratelli_1712345680.webp",
      "answers": [
        "condannati",
        "confraternita dei condannati",
        "confraternita"
      ]
    },
    {
      "id": "ronda_marinai_1712345681",
      "name": {
        "it": "La Ronda dei Marinai",
        "en": "The Sailors' Patrol"
      },
      "subtitle": {
        "it": "Un'ombra lunga la banchina.",
        "en": "A shadow along the pier."
      },
      "lat": 43.779983,
      "lng": 7.675677,
      "description": {
        "it": "Percorri la banchina seguendo i passi degli schiavi del mare.",
        "en": "Walk the pier following the steps of the sea slaves."
      },
      "hint": {
        "it": "Dove gli schiavi tiravano le barche, ora camminano i guardiani.",
        "en": "Where the slaves hauled the boats, now the guardians walk."
      },
      "icon": "quest",
      "type": "moving",
      "hintImage": "public/images/quests/ronda_marinai_1712345681.webp",
      "speed": 3,
      "waypoints": [
        [
          43.780544,
          7.676579
        ],
        [
          43.78072,
          7.676301
        ],
        [
          43.780679,
          7.676023
        ],
        [
          43.78046,
          7.675815
        ],
        [
          43.78028,
          7.675652
        ],
        [
          43.780109,
          7.675543
        ]
      ]
    },
    {
      "id": "sentinella_palme_1712345682",
      "name": {
        "it": "La Sentinella delle Palme",
        "en": "The Sentinel of the Palms"
      },
      "subtitle": {
        "it": "Un'ombra che non si ferma mai.",
        "en": "A shadow that never stops."
      },
      "lat": 43.777273,
      "lng": 7.670669,
      "description": {
        "it": "Intercetta la sentinella che percorre il lungomare e completa la ronda.",
        "en": "Intercept the sentinel patrolling the seafront and finish the rounds."
      },
      "hint": {
        "it": "La sua ombra scorre tra le palme, sempre in avanti.",
        "en": "Her shadow glides among the palms, always moving forward."
      },
      "icon": "quest",
      "type": "moving",
      "hintImage": "public/images/quests/sentinella_palme_1712345682.webp",
      "speed": 3,
      "waypoints": [
        [
          43.777015,
          7.67202
        ],
        [
          43.777041,
          7.671726
        ],
        [
          43.777067,
          7.671432
        ],
        [
          43.777093,
          7.671139
        ],
        [
          43.777119,
          7.670845
        ]
      ]
    }
  ]
}
```

## Struttura del file `images.json`

Un **array** con una entry per ogni sotto-quest `word`/`moving` uguale ai
campi `id` e `hintImage` di `masterquest.json`, più il `prompt` (inglese)
ottimizzato per "nano banana".

```json
[
  {
    "id": "bocca_fuoco_1712345679",
    "hintImage": "public/images/quests/bocca_fuoco_1712345679.webp",
    "prompt": "A weathered stone statue of a Marabutto holy man, carved with a distant serene face and flowing robes, standing on a round stone base engraved with a subtle ornamental name, flanked by two small old bronze cannons, on a seaside esplanade of the old Ligurian town of Bordighera. Golden late-afternoon Mediterranean light, warm limestone tones, slight sea mist in the background, cypress and palm silhouettes. Cinematic ground-level shot, front three-quarter view, shallow depth of field, storytelling fantasy illustration style, rich earthy palette, no text, no watermark."
  },
  {
    "id": "confratelli_1712345680",
    "hintImage": "public/images/quests/confratelli_1712345680.webp",
    "prompt": "A narrow stone alley in the medieval borgo of Bordighera at dusk, a heavy wooden door behind a small baroque church, above the lintel a worn carved emblem of a hooded brotherhood and a small lantern glowing amber, a long shadow of a hooded figure cast on the cobblestones, still and mysterious. Low dutch-angle shot from the street, chiaroscuro lighting with warm lantern glow against cool twilight blue, cinematic composition, illustrated mystery story game art style, textured stone and weathered wood, no text, no watermark."
  },
  {
    "id": "ronda_marinai_1712345681",
    "hintImage": "public/images/quests/ronda_marinai_1712345681.webp",
    "prompt": "A rugged old sailor character, weathered face, navy knit cap and wool coat, holding a brass lantern, walking the stone pier of Bordighera harbour at moonrise, fishing boats moored along the quay, rippling sea reflections, seagulls overhead, the lighthouse of Capo Sant'Ampelio faint in the distance. Full-body dynamic walking pose in profile, medium-wide shot, dramatic night lighting with cool moonlight and warm lantern glow, hand-painted storybook adventure game illustration style, muted navy and amber palette, no text, no watermark."
  },
  {
    "id": "sentinella_palme_1712345682",
    "hintImage": "public/images/quests/sentinella_palme_1712345682.webp",
    "prompt": "A graceful female guardian character with flowing white dress moving swiftly along the palm-lined seafront promenade of Bordighera, long hair and dress wafting in the breeze, her right palm extended with a faint luminous trail of light, rows of date palms and elegant belle-époque villas on her flank, the turquoise Mediterranean sea glowing at golden hour. Low-angle tracking shot capturing fast motion, dynamic forward stride, warm sunset backlight with long shadows, vibrant stylized illustration art, light teal and gold palette, no text, no watermark."
  }
]
```

## Cosa osservare in questo esempio

- Il file `masterquest.json` è un **oggetto JSON unico**, senza wrapper
  `masterQuests` e senza prefissi di riga. I testi it/en sono completi, non
  segnaposto.
- L'ordine dei campi della `MasterQuest` è: `id`, `name`, `subtitle`,
  `description`, `hint`, `start`, `end`, `icon`, `type`, `enabled`,
  `hintImage`, `collectible`, `reward`, `quests`.
- L'ordine dei campi di ogni `SottoQuest` è: `id`, `name`, `subtitle`, `lat`,
  `lng`, `description`, `hint`, `icon`, poi eventuali campi specifici del
  tipo (`type`, `hintImage`, `answers` oppure `type`, `hintImage`, `speed`,
  `waypoints`).
- Tutte le coordinate (`start`, `end`, `lat`/`lng` di ogni tappa) sono prese
  **solo** dai POI verificati di `references/locations.json` (vedi
  `coordinates.md`). Mai inventare coordinate a mano.
- I `waypoints` delle tappe `moving` seguono le **polilinee stradali
  verificate** di `references/locations.json` (lungomare, banchina, borgo
  antico): niente salti casuali sulla mappa.
- Le tappe `photo` possono omettere `"type"` esplicito (è accettabile anche
  `"type":"photo"`, ma non è obbligatorio).
- Gli `id` non richiedono prefissi di tipo (`mq_`, `photo_`, …): sono slug
  minuscoli unici, eventualmente con suffisso numerico.
- `answers` è sempre in minuscolo, senza punteggiatura, con più varianti
  reali in italiano e inglese.
- Le domande `word` chiedono sempre qualcosa di **osservabile sul luogo**
  (nomi incisi, targhe, statue), come nello schema.
- Il file `images.json` è un **array** con **una entry per ogni tappa `word`
  e `moving`** (mai per `photo` o per la master), nello stesso ordine delle
  tappe: `id` e `hintImage` sono **identici** a quelli della tappa in
  `masterquest.json` (pattern `public/images/quests/<quest_id>.webp`).
- Ogni `prompt` è un **prompt narrativo ottimizzato per "nano banana"** in
  inglese: descrive il character/NPC per le `moving` e la scena/oggetto del
  clue (senza rivelare la risposta) per le `word`, con soggetto, azione,
  luogo/ambientazione, composizione, luce e stile coerenti tra loro ("no
  text", "no watermark").
- Il percorso narrativo è coerente con le storie verificate di
  `references/history.md` (assedio del 1543, torri di avvistamento,
  confraternita dei Condannati, banchina degli Schiavi del Mare).
