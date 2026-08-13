# Regole tecniche sulle coordinate

## Area di gioco

Tutte le coppie `lat`/`lng` (della `MasterQuest`, delle `SottoQuest` e dei
`waypoints` delle tappe `moving`) devono cadere nella zona reale e giocabile
di Bordighera (centro città):

- `lat`: circa **43.777 – 43.781**
- `lng`: circa **7.668 – 7.677**

Non generare mai coordinate fuori da questo intervallo, anche se il tema
suggerirebbe un luogo lontano (es. il mare aperto, altre città): ambienta
sempre la narrazione su un punto reale e plausibile dentro quest'area
(lungomare, pineta, piazze, vicoli del centro storico, monumenti).

## Distanza tra le tappe

- Le 5 tappe più il punto di accettazione della master devono formare un
  percorso ragionevolmente compatto, percorribile interamente a piedi in
  **15-40 minuti totali**.
- Il punto della `MasterQuest` e le posizioni delle 5 `SottoQuest` **non**
  devono coincidere tutte nello stesso punto: distribuiscile lungo un
  tragitto sensato, coerente con lo sviluppo narrativo (introduzione →
  sviluppo → climax → conclusione).
- Evita di posizionare due tappe esattamente sulle stesse coordinate.

## Waypoints delle tappe `moving`

- Ogni tappa `moving` ha **almeno 5** coppie `[lat, lng]` in `waypoints`.
- I waypoint devono descrivere un **percorso lineare credibile** (una
  strada, il lungomare, il perimetro di una piazza), non punti sparsi a
  caso.
- La distanza tra due waypoint consecutivi deve essere di **poche decine di
  metri** (niente salti bruschi da un capo all'altro della città).
- Tutti i waypoint devono rientrare nell'area di gioco definita sopra.
- `speed` realistico: valori tra **2 e 4**.

## Checklist rapida prima di consegnare l'output

- [ ] Tutte le lat/lng (master + 5 tappe + tutti i waypoint) sono dentro
      `lat 43.777–43.781`, `lng 7.668–7.677`.
- [ ] Nessuna sovrapposizione totale tra master e tappe.
- [ ] Percorso complessivo plausibile a piedi in 15-40 minuti.
- [ ] Ogni `moving` ha almeno 5 waypoint con salti di poche decine di metri.
