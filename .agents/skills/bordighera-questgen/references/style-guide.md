# Guida di stile narrativo

## Principio generale

La storia deve essere **avvincente, coerente e verificata**, intrecciata con
la storia reale di Bordighera. Il testo di input deve "sfociare"
naturalmente nel percorso: le 5 tappe raccontano uno sviluppo narrativo con
un arco completo, costruito in stile **"caccia al segreto della città"**:

1. **Introduzione** — la masterquest (accettazione della quest) e la prima
   tappa piantano il seme del mistero. Il `subtitle` deve generare una
   domanda senza risposta (curiosity gap).
2. **Sviluppo** — le tappe centrali approfondiscono il mistero e aggiungono
   un **indizio nuovo per ogni tappa** (ogni tappa sblocca un pezzo
   dell'enigma).
3. **Climax** — il momento di massima tensione, spesso una tappa `moving` (un
   inseguimento, un'intercettazione, una pattuglia che custodisce il segreto).
4. **Conclusione** — l'ultima tappa chiude il cerchio narrativo, rivela il
   segreto e porta al riscatto del premio presso lo sponsor.

## Veridicità storica (obbligatoria)

- **Niente fatti inventati**: tutte le informazioni storiche devono venire da
  `references/history.md`, che raccoglie le storie verificate di Bordighera
  con le fonti. Non introdurre date, personaggi o eventi non documentati.
- **Niente luoghi inventati**: tutte le coordinate devono riferirsi ai POI e
  alle polilinee di `references/locations.json` (vedi `coordinates.md`).
- La **cornice misteriosa** (il segreto, il messaggio cifrato, la figura
  narrativa, il colpevole di turno) può essere inventata liberamente: deve
  solo avvolgere fatti e luoghi veri, senza contraddirli.

## Tono dei singoli campi

- `name` (master e tappe): deve **catturare subito l'attenzione**, con un
  tono evocativo ma non ridondante rispetto a `subtitle`. In stile mistero:
  preferisci titoli che promettono un segreto (es. "Il Dattero Scomparso",
  "Gli Otto Sguardi", "Il Muro del Pirata").
- `subtitle`: una singola frase breve e misteriosa che **lascia aperta una
  domanda** — non anticipa mai la soluzione. Per la master, invita ad
  accettare la quest.
- `description`: un paragrafetto di 2-4 righe che **evoca un'atmosfera** e
  motiva il giocatore a raggiungere la tappa; ogni riga può aggiungere un
  dettaglio del mistero (un indizio, un nome, una data vera). Per le tappe
  `photo`, indica chiaramente cosa fotografare ("scatta una foto del...").
  Per le tappe `word`, pone la domanda precisa a cui il giocatore deve
  rispondere.
- `hint`: un **indizio enigmatico**, una o due frasi, che orienta il
  giocatore verso il punto preciso **senza mai svelarlo esplicitamente**
  (niente nomi di vie o indicazioni troppo dirette: preferisci immagini,
  metafore, dettagli sensoriali legati al luogo reale).

## Coinvolgimento del giocatore

- **Curiosity gap**: ogni tappa termina con un gancio (il messaggio, il
  criptogramma, la promessa della rivelazione) che rende impossibile
  fermarsi.
- **Piccola vittoria per tappa**: ogni tappa `word`/`photo` dà un feedback
  immediato ("Il codice combacia...").
- **Esperienza divertente**: usa tono leggero, piccoli anacronismi giocosi,
  riferimenti ai cannoni dai nomi buffi (Tiralogni, Cacastrasse, Butafoegu),
  ai parmureli, ai punti di vista di Garnier e ai vicoli del borgo.
- **Risposte `word` testabili sul posto**: la risposta giusta deve essere
  trovable osservando il luogo (iscrizione, statua, forma, insegna) o
  leggendo la `description`/`hint` della tappa.

## Coerenza con i luoghi reali

- Ogni tappa deve rimandare a un luogo reale di Bordighera presente in
  `locations.json` (lungomare, capo Sant'Ampelio, borgo antico e le sue
  porte, piazze, ville e musei).
- Non ripetere lo stesso POI per due tappe diverse; i ~20 POI verificati
  permettono un percorso variegato.

## Sponsor e premio

- Scegli uno `sponsorId` plausibile e coerente con il tono della storia (es.
  un locale, un negozio, un bar del centro o del lungomare).
- `reward.price` è **opzionale**: costo in monete per acquistare il
  collezionabile senza completare il percorso (omesso o `0` = solo con la
  quest). Il campo `sponsorPin` **non** esiste.
- `reward.description` spiega cosa e come riscattare il premio, e può usare
  `<strong>` per evidenziare l'oggetto del premio.
- `reward.share.text` usa sempre i placeholder `{path}`, `{name}`, `{url}`,
  `{tags}` così come mostrato nell'esempio di riferimento.
- `reward.share.hashtags` include sempre almeno `["BordigheraQuest","Bordighera"]`.

## Lunghezze indicative

| Campo | Lunghezza |
| --- | --- |
| `name` | poche parole, titolo |
| `subtitle` | una frase |
| `description` | 2-4 righe |
| `hint` | una o due frasi |

## Prompt delle immagini `hintImage` (per "nano banana")

Per ogni tappa `word`/`moving` bisogna scrivere in `images.json` il `prompt`
(inglese) di generazione della sua immagine `hintImage`, pensato per
**"nano banana"** (Gemini image model): accetta prompt narrativi, natural
language, dettagliati — non liste di keyword.

### Regole di scrittura

- **Lingua**: inglese. **Stile**: narrativo e specifico, tipo spec di sceneggiatura.
- **Per le `moving`** (character): descrivi il **personaggio/NPC** che
  pattuglia (aspetto, abbigliamento, atteggiamento) in **azione** nel luogo
  reale della polilinea (banchina, lungomare, borgo, rotonda).
- **Per le `word`** (clue): descrivi la **scena o l'oggetto del clue** (sito,
  iscrizione, statua, porta) in modo atmosferico ma **senza mai rivelare la
  risposta**, e senza scrivere alcun testo/parola nell'immagine.
- **Struttura consigliata**: soggetto → azione → luogo/contesto → composizione
  → luce → stile. Usa framing positivo (descrivi cosa vuoi, non cosa non
  vuoi), termini di camera/illuminazione concreti e chiusura con vincoli
  ("no text", "no watermark").
- **Coerenza tra le immagini**: stessa famiglia stilistica (es. illustrazione
  narrativa da gioco di avventura), stessa palette dominante (tonalità
  mediterranee: pietra chiara, turchese, ambra) e aspect ratio coerente
  (es. 16:9) in tutti i prompt della masterquest.
- **Coerenza con la narrazione**: i dettagli visivi (luoghi, personaggio,
  orari di luce) devono venire da `description`/`hint` della tappa e dalle
  storie verificate di `history.md`; mai elementi che contraddicono la storia.

## Cosa evitare

- Non uscire mai dal contratto di output: il risultato sono i file
  `masterquest.json` e `images.json` nella cartella corrente (vedi `SKILL.md`),
  senza testo esterno.
- Non introdurre campi non previsti dallo schema, anche se "utili" per la
  narrazione (es. `story`, `chapter`, `difficulty` non esistono).
- Non rendere gli `hint` troppo espliciti: devono richiedere osservazione,
  non essere indicazioni stradali dirette.
- Non ripetere lo stesso luogo per due tappe diverse.
- **Non inventare fatti storici** (date, biografie, eventi) e **non usare
  coordinate fuori da `locations.json`**: entrambi sono errori bloccanti.