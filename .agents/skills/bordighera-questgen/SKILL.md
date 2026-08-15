---
name: bordighera-questgen
description: >-
  Genera masterquest complete in formato JSON per "UrbanQuest Bordighera", un
  gioco urbano a tappe nella città di Bordighera (Italia), scrivendo il
  risultato nei file "masterquest.json" e "images.json" nella cartella
  corrente. Usa questa skill quando l'utente chiede di generare, creare o
  scrivere una "masterquest", una "quest", un "percorso" o un "itinerario di
  gioco" per UrbanQuest Bordighera a partire da un testo, tema o lore di
  ispirazione, oppure quando menziona i file "masterquest.json" o
  "images.json".
license: MIT
---

# bordighera-questgen

Questa skill trasforma l'agent in un **game designer e scrittore creativo**
specializzato in "UrbanQuest Bordighera". Il suo unico compito è produrre,
a partire da un testo di ispirazione fornito dall'utente, **una masterquest
completa** in un formato JSON rigidamente specificato e scriverla nel file
**`masterquest.json`** nella cartella corrente di lavoro, insieme al file
**`images.json`** che raccoglie, per ogni tappa `word` (clue) e `moving`
(character), il prompt ottimizzato (per il generatore d'immagini "nano
banana") della rispettiva immagine `hintImage`. Nessun testo aggiuntivo.

## Quando usare questa skill

Attiva questa skill quando l'utente:
- chiede di generare/creare una "masterquest", una "quest" o un "percorso"
  per UrbanQuest Bordighera;
- fornisce un testo/tema/lore e chiede di trasformarlo in una quest urbana;
- chiede di scrivere o aggiornare i file `masterquest.json` / `images.json`;
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
3. `references/locations.json` — **il database dei luoghi verificati** di
   Bordighera (POI con coordinate reali e polilinee di strade reali per i
   `moving`). **È l'unica fonte ammessa per le coordinate.** Mai inventare
   lat/lng.
4. `references/history.md` — **le storie verificate** di Bordighera con le
   fonti. È l'unica fonte ammessa per i fatti storici: mai inventare date,
   biografie o eventi.
5. `references/coordinates.md` — i vincoli geografici su Bordighera, sulla
   distanza tra le tappe e sui waypoint dei bersagli `moving`.
6. `references/style-guide.md` — le regole di tono, narrativa e struttura in
   5 tappe (introduzione → sviluppo → climax → conclusione), in stile
   "caccia al segreto della città", più le regole per i prompt delle immagini
   `hintImage` per "nano banana".

## Contratto di output (non negoziabile)

La generazione produce **due file JSON** nella **cartella corrente di
lavoro**: `masterquest.json` e `images.json`.

- **`masterquest.json`** — l'unico risultato della master quest: un **unico
  oggetto JSON** (la `MasterQuest` diretta, senza wrapper `masterQuests`).
- **`images.json`** — un **array di oggetti** `{id, hintImage, prompt}`, con
  **una entry per ogni sotto-quest di tipo `word` o `moving`** (cioè 2 `word`
  + 2 `moving` = 4 entry): il nome dell'immagine `hintImage` della tappa e il
  `prompt` ottimizzato in inglese per generarla con "nano banana". Nessuna
  entry per le tappe `photo` (senza `hintImage`) né per la master.
- Entrambi i file devono contenere **solo JSON**: nessun blocco di codice,
  nessun backtick, nessun commento, nessuna virgola finale (trailing comma),
  nessun testo aggiuntivo dentro o fuori dal JSON.
- I JSON devono essere validi e conformi **esattamente** allo schema in
  `references/schema.md`.
- Non rispondere con testo narrativo nella chat oltre a una brevissima
  conferma (es. "`masterquest.json` e `images.json` scritti"); **mai**
  stampare il JSON nel messaggio.

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
   `>>>>`, se presente). Se manca, è vago o insufficiente, estendilo in modo
   coerente **ancorandolo alle storie verificate di `references/history.md`**
   — ma mantieni sempre la struttura 1 photo + 2 word + 2 moving.
2. Individua nella storia scelta (max 2 storie combinate) il filo narrativo
   che collega il tema al percorso reale a Bordighera: introduzione
   (accettazione quest) → sviluppo (prime 2-3 tappe) → **climax** (tappa più
   intensa, spesso una `moving`) → conclusione (ultima tappa, spesso quella
   che sblocca il premio). Costruisci la **cornice misteriosa** ("il segreto
   della città") attorno a fatti e luoghi veri.
3. Scegli uno sponsor coerente e un premio plausibile, coerenti con il tono
   della storia. `reward.price` è opzionale (assente/`0` = non acquistabile);
   il campo `sponsorPin` **non esiste**.
4. Scegli le coordinate **solo dal database `references/locations.json`**,
   seguendo `references/coordinates.md`: prendi i POI reali per
   `start`/`end` e per le tappe `photo`/`word` (mai lo stesso POI due volte),
   e una polilinea verificata (`lungomare_argentina`, `rotonda_sant_ampelio`,
   `banchina_schiavi_del_mare`, `via_romana`, `borgo_antico`) per i waypoint
   `moving`. Il percorso complessivo deve essere percorribile a piedi in
   15-40 minuti.
5. Scrivi i testi (`name`, `subtitle`, `description`, `hint`) sia in italiano
   sia in inglese, seguendo `references/style-guide.md` per tono (stile
   mistero/"caccia al segreto") e lunghezza. Le domande `word` devono avere
   risposta osservabile sul posto o derivabile dalla `description`/`hint`.
6. Componi il JSON finale seguendo `references/schema.md` e
   `references/example-output.md` campo per campo. Le sotto-quest `word` e
   `moving` devono avere sempre il campo `hintImage` valorizzato con il
   pattern `public/images/quests/<quest_id>.webp`, così da generare anche la
   corrispondente entry in `images.json`.
7. Prima di scrivere il file, verifica con `scripts/validate.py` (se hai
   accesso a un interprete Python) oppure mentalmente che:
   - ci siano esattamente 5 sotto-quest con la composizione 1/2/2 corretta;
   - tutti gli `id` siano unici, minuscoli, `[a-z0-9_]`;
   - ogni tappa `word` abbia `answers` con più varianti reali, tutte
     minuscole e senza punteggiatura;
   - ogni tappa `moving` abbia `speed` tra 2 e 4 e almeno 5 waypoint
     `[lat, lng]` che seguono una polilinea di `locations.json`;
   - **tutte** le lat/lng (start, end, tappe, waypoint) siano **presso un
     POI o una polilinea verificata** di `locations.json` e rientrino
     nell'area di gioco di `references/coordinates.md`;
   - i fatti storici citati nei testi siano presenti in `references/history.md`;
   - non manchi nessun campo obbligatorio dello schema;
   - ogni tappa `word`/`moving` abbia `hintImage` (pattern
     `public/images/quests/<quest_id>.webp`) e una entry corrispondente in
     `images.json`.
8. Scrivi il JSON validato nel file **`masterquest.json`** nella cartella
   corrente di lavoro, come unico contenuto del file.
9. Genera **`images.json`**: per ogni sotto-quest di tipo `word`/`moving`
   presente in `masterquest.json`, crea una entry `{id, hintImage, prompt}`:
   - `id` = id della tappa (minuscolo, uguale a quello in `masterquest.json`);
   - `hintImage` = identico al campo `hintImage` della tappa in
     `masterquest.json`;
   - `prompt` = prompt ottimizzato in inglese per generare l'immagine con
     "nano banana", seguendo le regole di `references/style-guide.md` (per le
     `moving` il character/NPC che pattuglia; per le `word` la scena/l'oggetto
     del clue, senza mai scrivere la risposta). Usa `references/example-output.md`
     come riferimento per stile e contenuto dei prompt.
10. Scrivi il JSON validato nel file **`images.json`** nella cartella corrente
    di lavoro, come unico contenuto del file. Conferma in chat solo con una
    breve nota (es. "`masterquest.json` e `images.json` scritti"), senza
    stampare i JSON.

## Se ti viene chiesto di validare un output esistente

Se l'utente incolla un output già generato e chiede una verifica, usa
`scripts/validate.py` (se disponibile un interprete Python) oppure applica
manualmente i controlli del punto 7 sopra, poi riporta in modo sintetico gli
eventuali errori di schema **e di posizione** (tappe non vicino a un POI
verificato di `locations.json`, waypoint `moving` lontani dalle polilinee
verificate), senza riscrivere l'intero JSON a meno che non ti venga chiesto
esplicitamente di correggerlo.
