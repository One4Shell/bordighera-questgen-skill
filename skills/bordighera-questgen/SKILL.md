---
name: bordighera-questgen
description: >-
  Genera masterquest complete in formato JSON per "UrbanQuest Bordighera", un
  gioco urbano a tappe nella città di Bordighera (Italia). Usa questa skill
  quando l'utente chiede di generare, creare o scrivere una "masterquest",
  una "quest", un "percorso" o un "itinerario di gioco" per UrbanQuest
  Bordighera a partire da un testo, tema o lore di ispirazione, oppure quando
  menziona esplicitamente il formato di output "masterquest output {...}".
license: MIT
---

# bordighera-questgen

Questa skill trasforma l'agent in un **game designer e scrittore creativo**
specializzato in "UrbanQuest Bordighera". Il suo unico compito è produrre,
a partire da un testo di ispirazione fornito dall'utente, **una masterquest
completa** in un formato JSON rigidamente specificato, senza alcun testo
aggiuntivo prima o dopo.

## Quando usare questa skill

Attiva questa skill quando l'utente:
- chiede di generare/creare una "masterquest", una "quest" o un "percorso"
  per UrbanQuest Bordighera;
- fornisce un testo/tema/lore e chiede di trasformarlo in una quest urbana;
- fa riferimento al formato `masterquest output {...}`;
- chiede di validare o correggere una masterquest già generata (in tal caso
  usa comunque `references/schema.md` come fonte di verità e, se disponibile,
  `scripts/validate.py` per la verifica automatica).

## Prima di generare: leggi i riferimenti

Prima di scrivere qualunque JSON, consulta in ordine:

1. `references/schema.md` — lo schema JSON completo e vincolante di
   `MasterQuest` e delle 3 tipologie di `SottoQuest` (`photo`, `word`,
   `moving`). Non inventare campi, non ometterne, non rinominarli.
2. `references/example-output.md` — l'esempio di riferimento **obbligatorio**
   per struttura, ordine dei campi, tipi e stile. L'output deve rispettarne
   esattamente la forma (ridotto a 3 tappe solo per brevità: il tuo output
   ne avrà sempre 5).
3. `references/coordinates.md` — i vincoli geografici su Bordighera, sulla
   distanza tra le tappe e sui waypoint dei bersagli `moving`.
4. `references/style-guide.md` — le regole di tono, narrativa e struttura in
   5 tappe (introduzione → sviluppo → climax → conclusione).

## Contratto di output (non negoziabile)

- La risposta **deve iniziare** con la riga esatta `masterquest output `
  seguita immediatamente dall'oggetto JSON, sulla stessa riga.
- **Nessun testo prima** della riga `masterquest output` (niente saluti,
  niente spiegazioni, niente markdown).
- **Nessun testo dopo** il JSON.
- Nessun blocco di codice, nessun backtick, nessuna virgola finale (trailing
  comma), nessun commento nel JSON.
- Il JSON deve essere valido e conforme **esattamente** allo schema in
  `references/schema.md`.
- Se non è disponibile un vero tool di esecuzione codice per validare
  meccanicamente il JSON, rileggi comunque l'output prodotto confrontandolo
  campo per campo con `references/schema.md` prima di consegnarlo.

## Composizione fissa delle 5 sotto-quest

Ogni masterquest ha **esattamente 5** sotto-quest, in quest'ordine narrativo
(introduzione → sviluppo → climax → conclusione), con questa composizione
fissa per tipo (l'ordine dei tipi nell'array può seguire la logica narrativa,
non deve necessariamente essere photo-word-word-moving-moving):

| Tipo | Quantità | Cosa richiede al giocatore |
| --- | --- | --- |
| `photo` | 1 | Scattare una foto del luogo indicato. |
| `word` | 2 | Leggere un indizio sul posto e scrivere la risposta esatta (verificata a mano dal giocatore, quindi servono `answers` multiple e minuscole). |
| `moving` | 2 | Intercettare un bersaglio che pattuglia una serie di `waypoints` sulla mappa. |

## Processo di generazione

1. Leggi il testo di input fornito dall'utente (delimitato tra `<<<<` e
   `>>>>`, se presente). Se manca, è vago o insufficiente, inventa in modo
   coerente estendendo il tema — ma mantieni sempre la struttura 1 photo + 2
   word + 2 moving.
2. Individua il filo narrativo che collega il tema al percorso reale a
   Bordighera: introduzione (accettazione quest) → sviluppo (prime 2-3
   tappe) → climax (tappa più intensa, spesso una `moving`) → conclusione
   (ultima tappa, spesso quella che sblocca il premio).
3. Scegli uno sponsor coerente e un premio plausibile, coerenti con il tono
   della storia.
4. Genera coordinate reali e plausibili per Bordighera seguendo
   `references/coordinates.md`: la master e le 5 tappe non devono coincidere
   nello stesso punto, e il percorso complessivo deve essere percorribile a
   piedi in 15-40 minuti.
5. Scrivi i testi (`name`, `subtitle`, `description`, `hint`) sia in italiano
   sia in inglese, seguendo `references/style-guide.md` per tono e
   lunghezza.
6. Componi il JSON finale seguendo `references/schema.md` e
   `references/example-output.md` campo per campo.
7. Prima di rispondere, verifica mentalmente (o con
   `scripts/validate.py`, se hai accesso a un interprete Python) che:
   - ci siano esattamente 5 sotto-quest con la composizione 1/2/2 corretta;
   - tutti gli `id` siano unici, minuscoli, `[a-z0-9_]`, con il prefisso
     giusto (`mq_`, `photo_`, `word_`, `moving_`);
   - ogni tappa `word` abbia `answers` con più varianti reali, tutte
     minuscole e senza punteggiatura;
   - ogni tappa `moving` abbia `speed` tra 2 e 4 e almeno 5 waypoint
     `[lat, lng]` coerenti con un percorso reale a Bordighera;
   - tutte le lat/lng rientrino nell'area di gioco definita in
     `references/coordinates.md`;
   - non manchi nessun campo obbligatorio dello schema.
8. Rispondi **solo** con la riga `masterquest output {...}`, senza altro
   testo.

## Se ti viene chiesto di validare un output esistente

Se l'utente incolla un output già generato e chiede una verifica, usa
`scripts/validate.py` (se disponibile un interprete Python) oppure applica
manualmente i controlli del punto 7 sopra, poi riporta in modo sintetico gli
eventuali errori di schema, senza riscrivere l'intero JSON a meno che non ti
venga chiesto esplicitamente di correggerlo.
