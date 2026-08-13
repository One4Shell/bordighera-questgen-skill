# Esempio di riferimento (struttura output)

Questo è l'esempio **obbligatorio** di riferimento per struttura, ordine dei
campi, tipi e stile. È ridotto a 3 tappe solo per brevità: nel tuo output le
tappe devono essere **sempre 5** (1 `photo`, 2 `word`, 2 `moving`).

Il risultato della generazione viene scritto nel file **`masterquest.json`**
nella cartella corrente di lavoro, come oggetto JSON valido senza alcun testo
aggiuntivo. Nessun wrapper `masterQuests`, nessuna riga di prefisso, nessun
blocco markdown, nessun backtick.

## Struttura del file `masterquest.json`

```json
{
  "id": "masterquest_sentiero_pirati",
  "name": { "it": "Il Sentiero dei Pirati", "en": "The Pirate's Trail" },
  "subtitle": { "it": "Ogni esploratore ha bisogno di un punto di partenza.", "en": "Every explorer needs a starting point." },
  "description": { "it": "Completa le tappe di questo percorso e scopri i segreti nascosti di Bordighera.", "en": "Complete the stages of this path and uncover Bordighera's hidden secrets." },
  "hint": { "it": "Raggiungi il punto indicato sulla mappa e attiva la missione.", "en": "Reach the point shown on the map and activate the mission." },
  "lat": 43.7778,
  "lng": 7.6697,
  "icon": "quest",
  "type": "master",
  "enabled": true,
  "hintImage": "sponsor/premi/marmura-premio.webp",
  "collectible": "public/models/pirati/mq_pirati.obj",
  "reward": {
    "sponsorId": "marmura",
    "title": { "it": "Il tuo premio ti aspetta", "en": "Your prize awaits you" },
    "description": { "it": "Ritira il tuo <strong>caffè omaggio</strong> alla Marmura.", "en": "Collect your <strong>FREE coffee</strong> at Marmura." },
    "share": {
      "text": { "it": "Ho completato la Bordighera Quest - {path} con {name}! 🎉\n\n▶ Gioca ora: {url}\n#{tags}", "en": "I completed the Bordighera Quest - {path} as {name}! 🎉\n\n▶ Play now: {url}\n#{tags}" },
      "hashtags": ["BordigheraQuest", "Bordighera"],
      "facebook": "https://www.facebook.com/",
      "instagram": "https://www.instagram.com/"
    },
    "sponsorPin": "0000"
  },
  "quests": [
    {
      "id": "nave_legno_1712345678",
      "name": { "it": "La Nave di Legno", "en": "The Wooden Ship" },
      "subtitle": { "it": "Un vascello fermo nel tempo.", "en": "A vessel frozen in time." },
      "lat": 43.7795,
      "lng": 7.6734,
      "description": { "it": "Scatta una foto dell'antica nave di legno.", "en": "Take a photo of the ancient wooden ship." },
      "hint": { "it": "Dove il legno incontra le onde troverai lo scafo dimenticato.", "en": "Where wood meets the waves you will find the forgotten hull." },
      "icon": "quest"
    },
    {
      "id": "statua_regina_1712345679",
      "name": { "it": "La Regina di Pietra", "en": "The Stone Queen" },
      "subtitle": { "it": "Un nome inciso tra le foglie.", "en": "A name carved among the leaves." },
      "lat": 43.7784,
      "lng": 7.6711,
      "description": { "it": "Quale nome è scritto alla base della statua?", "en": "Which name is written at the base of the statue?" },
      "hint": { "it": "Il suo sguardo punta verso il mare, ma il suo nome guarda al passato.", "en": "Her gaze faces the sea, but her name looks to the past." },
      "icon": "quest",
      "type": "word",
      "hintImage": "data:image/webp,...",
      "answers": ["giulia", "regina", "giulia regina", "queen giulia"]
    },
    {
      "id": "patrol_lungomare_1712345680",
      "name": { "it": "La Sentinella", "en": "The Sentinel" },
      "subtitle": { "it": "Un'ombra che non si ferma mai.", "en": "A shadow that never stops." },
      "lat": 43.7790,
      "lng": 7.6746,
      "description": { "it": "Intercetta la sentinella che pattuglia il lungomare.", "en": "Intercept the sentinel patrolling the seafront." },
      "hint": { "it": "Seguila mentre si muove tra le palme.", "en": "Follow her as she moves among the palms." },
      "icon": "quest",
      "type": "moving",
      "hintImage": "data:image/webp,...",
      "speed": 3,
      "waypoints": [
        [43.7784, 7.6740],
        [43.7786, 7.6742],
        [43.7790, 7.6742],
        [43.7792, 7.6741],
        [43.7790, 7.6739]
      ]
    }
  ]
}
```

## Cosa osservare in questo esempio

- Il file `masterquest.json` è un **oggetto JSON unico**, senza wrapper
  `masterQuests` e senza prefissi di riga. I testi it/en sono completi, non
  segnaposto.
- L'ordine dei campi della `MasterQuest` è: `id`, `name`, `subtitle`,
  `description`, `hint`, `lat`, `lng`, `icon`, `type`, `enabled`,
  `hintImage`, `collectible`, `reward`, `quests`.
- L'ordine dei campi di ogni `SottoQuest` è: `id`, `name`, `subtitle`, `lat`,
  `lng`, `description`, `hint`, `icon`, poi eventuali campi specifici del
  tipo (`type`, `hintImage`, `answers` oppure `type`, `hintImage`, `speed`,
  `waypoints`).
- Le tappe `photo` non hanno il campo `type` esplicito in questo esempio
  (è accettabile anche `"type":"photo"` esplicito, ma non è obbligatorio).
- Gli `id` non richiedono prefissi di tipo (`mq_`, `photo_`, …): sono slug
  minuscoli unici, eventualmente con suffisso numerico.
- `answers` è sempre in minuscolo, senza punteggiatura, con più varianti
  reali in italiano e inglese.
- `waypoints` descrive un tragitto lineare credibile (il lungomare), non
  salti casuali sulla mappa.
- Il tuo output reale avrà **5** elementi in `quests`, non 3: aggiungi una
  seconda tappa `word` e una seconda tappa `moving`, mantenendo lo stesso
  stile e la stessa coerenza narrativa mostrati qui.
