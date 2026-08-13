# Guida di stile narrativo

## Principio generale

La storia deve essere **avvincente e coerente**, intrecciata con il
tema/lore del testo di input fornito dall'utente. Il testo di input deve
"sfociare" naturalmente nel percorso: le 5 tappe raccontano uno sviluppo
narrativo con un arco completo:

1. **Introduzione** — la masterquest (accettazione della quest) e la prima
   tappa piantano il seme della storia.
2. **Sviluppo** — le tappe centrali approfondiscono il mistero o l'avventura.
3. **Climax** — il momento di massima tensione, spesso una tappa `moving`
   (un inseguimento, un'intercettazione).
4. **Conclusione** — l'ultima tappa chiude il cerchio narrativo e porta al
   riscatto del premio presso lo sponsor.

## Tono dei singoli campi

- `name` (master e tappe): deve **catturare subito l'attenzione**, con un
  tono evocativo ma non ridondante rispetto a `subtitle`.
- `subtitle`: una singola frase breve. Per la master, invita ad accettare la
  quest. Per le tappe, è breve e misteriosa — non anticipa la soluzione.
- `description`: un paragrafetto di 2-4 righe che **evoca un'atmosfera** e
  motiva il giocatore a raggiungere la tappa. Per le tappe `photo`, indica
  chiaramente cosa fotografare ("scatta una foto del..."). Per le tappe
  `word`, pone la domanda precisa a cui il giocatore deve rispondere.
- `hint`: un **indizio enigmatico**, una o due frasi, che orienta il
  giocatore verso il punto preciso senza mai svelarlo esplicitamente (niente
  nomi di vie o indicazioni troppo dirette: preferisci immagini, metafore,
  dettagli sensoriali legati al luogo reale).

## Coerenza con i luoghi reali

- Ogni tappa deve rimandare a un luogo o elemento reale di Bordighera
  (lungomare, pineta, monumenti, mare, palme, vicoli del centro storico,
  piazze) — atmosfera ricca ma senza inventare localizzazioni impossibili.
- Se il testo di input è vago o insufficiente, estendilo in modo coerente
  mantenendo sempre l'ambientazione reale di Bordighera.

## Sponsor e premio

- Scegli uno `sponsorId` plausibile e coerente con il tono della storia
  (es. un locale, un negozio, un bar del centro).
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

## Cosa evitare

- Non uscire mai dal contratto di output (nessun testo fuori dal JSON, vedi
  `SKILL.md`).
- Non introdurre campi non previsti dallo schema, anche se "utili" per la
  narrazione (es. campi come `story`, `chapter`, `difficulty` non esistono).
- Non rendere gli `hint` troppo espliciti: devono richiedere osservazione,
  non essere indicazioni stradali dirette.
- Non ripetere lo stesso luogo per due tappe diverse.
