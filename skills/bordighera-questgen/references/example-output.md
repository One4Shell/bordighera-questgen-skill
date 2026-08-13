# Esempio di riferimento (formato output)

Questo è l'esempio **obbligatorio** di riferimento per struttura, ordine dei
campi, tipi e stile. È ridotto a 3 tappe solo per brevità: nel tuo output le
tappe devono essere **sempre 5** (1 `photo`, 2 `word`, 2 `moving`).

Non aggiungere testo prima o dopo la riga. Non usare backtick né blocchi
markdown nella risposta reale: qui sotto sono presenti solo per la
leggibilità di questo documento.

```
masterquest output {"masterQuests":[{"id":"mq_sentiero_dei_pirati","name":{"it":"Il Sentiero dei Pirati","en":"The Pirate's Trail"},"subtitle":{"it":"Ogni esploratore ha bisogno di un punto di partenza. Accetta la quest e inizia la tua avventura.","en":"Every explorer needs a starting point. Accept the quest and begin your adventure."},"description":{"it":"Completa le tappe di questo percorso e scopri i segreti nascosti di Bordighera.","en":"Complete the stages of this path and uncover Bordighera's hidden secrets."},"hint":{"it":"Raggiungi il punto indicato sulla mappa e attiva la missione.","en":"Reach the point shown on the map and activate the mission."},"lat":43.7778,"lng":7.6697,"icon":"quest","type":"master","enabled":true,"collectible":"public/models/pirati/mq_pirati.obj","reward":{"sponsorId":"marmura","title":{"it":"Il tuo premio ti aspetta","en":"Your prize awaits you"},"description":{"it":"Ritira il tuo <strong>caffè omaggio</strong> alla Marmura. Presenta questa schermata allo sponsor per riceverlo.","en":"Collect your <strong>FREE coffee</strong> at Marmura. Show this screen to the sponsor to receive it."},"share":{"text":{"it":"Ho completato la Bordighera Quest - {path} con {name}! \ud83c\udf89\n\n\u25b6 Gioca ora: {url}\n#{tags}","en":"I completed the Bordighera Quest - {path} as {name}! \ud83c\udf89\n\n\u25b6 Play now: {url}\n#{tags}"},"hashtags":["BordigheraQuest","Bordighera"],"facebook":"https://www.facebook.com/","instagram":"https://www.instagram.com/"},"sponsorPin":"0000"},"quests":[{"id":"photo_nave_legno","name":{"it":"La Nave di Legno","en":"The Wooden Ship"},"subtitle":{"it":"Un vascello fermo nel tempo.","en":"A vessel frozen in time."},"lat":43.7795,"lng":7.6734,"description":{"it":"Scatta una foto dell'antica nave di legno che ancora guarda verso il mare.","en":"Take a photo of the ancient wooden ship still gazing at the sea."},"hint":{"it":"Dove il legno incontra le onde, troverai lo scafo dimenticato.","en":"Where wood meets the waves, you'll find the forgotten hull."},"icon":"quest"},{"id":"word_statua_regina","name":{"it":"La Regina Silenziosa","en":"The Silent Queen"},"subtitle":{"it":"Ogni monumento custodisce una storia.","en":"Every monument preserves a story."},"lat":43.7781,"lng":7.6739,"description":{"it":"Quale animale si avvolge silenziosamente attorno al braccio destro della statua?","en":"What animal silently coils around the statue's right arm?"},"hint":{"it":"Trova il braccio destro della statua e troverai la risposta.","en":"Find the right arm of the statue and you'll find the answer."},"icon":"quest","type":"word","answers":["serpente","snake","serpent","vipera","biscia"]},{"id":"moving_spirito_monet","name":{"it":"Lo Spirito Smarrito","en":"The Wandering Spirit"},"subtitle":{"it":"Non si ferma mai.","en":"It never stops."},"lat":43.7786,"lng":7.6746,"description":{"it":"Intercetta la figura che pattuglia il lungomare prima che svanisca tra la folla.","en":"Intercept the figure patrolling the seafront before it vanishes into the crowd."},"hint":{"it":"Segui il lungomare e anticipa i suoi passi per intercettarlo.","en":"Follow the seafront and anticipate its steps to intercept it."},"icon":"quest","type":"moving","speed":3,"waypoints":[[43.7783,7.6739],[43.7786,7.6741],[43.7789,7.6741],[43.7792,7.6740],[43.7791,7.6739]]}]}]}
```

## Cosa osservare in questo esempio

- La riga inizia con `masterquest output ` (con lo spazio finale) seguita
  subito dalla graffa di apertura del JSON — nessuna riga vuota, nessun
  preambolo.
- L'ordine dei campi della `MasterQuest` è: `id`, `name`, `subtitle`,
  `description`, `hint`, `lat`, `lng`, `icon`, `type`, `enabled`,
  `collectible`, `reward`, `quests`.
- L'ordine dei campi di ogni `SottoQuest` è: `id`, `name`, `subtitle`, `lat`,
  `lng`, `description`, `hint`, `icon`, poi eventuali campi specifici del
  tipo (`type`, `answers` oppure `type`, `speed`, `waypoints`).
- Le tappe `photo` non hanno il campo `type` esplicito in questo esempio
  (è accettabile anche `"type":"photo"` esplicito, ma non è obbligatorio).
- `answers` è sempre in minuscolo, senza punteggiatura, con più varianti
  reali in italiano e inglese.
- `waypoints` descrive un tragitto lineare credibile (il lungomare), non
  salti casuali sulla mappa.
- Il tuo output reale avrà **5** elementi in `quests`, non 3: aggiungi una
  seconda tappa `word` e una seconda tappa `moving`, mantenendo lo stesso
  stile e la stessa coerenza narrativa mostrati qui.
