# Regole tecniche sulle coordinate

## Fonte esclusiva: `locations.json`

**Non inventare mai coordinate.** L'unica fonte ammessa è il database
`references/locations.json`, che elenca:

- **`pois`**: POI verificati (via OpenStreetMap/Wikipedia) con `lat`/`lng`,
  categoria, nota storica e fonte;
- **`paths`**: polilinee **reali** di strade e marciapiedi (dal tracciato
  OSM) da usare per i waypoint delle tappe `moving`.

Ogni tappa (`photo`, `word`, `start`/`end` della master) deve cadere presso
un POI del database; ogni waypoint `moving` deve seguire una polilinea del
database. Il validatore `scripts/validate.py` applica questi controlli.

## Area di gioco

Tutte le coppie `lat`/`lng` (della `MasterQuest`, delle `SottoQuest` e dei
`waypoints` delle tappe `moving`) devono cadere nella zona reale e giocabile
di Bordighera (centro città, lungomare, borgo antico, quartiere dei giardini,
capo Sant'Ampelio):

- `lat`: circa **43.777 – 43.784**
- `lng`: circa **7.667 – 7.677**

Non generare mai coordinate fuori da questo intervallo: ambienta sempre la
narrazione su un punto reale presente in `locations.json` dentro quest'area.

## Distanza tra le tappe

- Le 5 tappe più il punto di accettazione della master (`start`) e il punto
  di arrivo (`end`) devono formare un percorso ragionevolmente compatto,
  percorribile interamente a piedi in **15-40 minuti totali**.
- `start`, le 5 tappe e `end` **non** devono coincidere nello stesso punto:
  distribuiscili lungo un tragitto sensato e coerente con lo sviluppo
  narrativo (introduzione → sviluppo → climax → conclusione).
- Evita di posizionare due punti a meno di poche decine di metri l'uno
  dall'altro; i POI di `locations.json` sono distanti tra loro proprio per
  questo.

## Waypoint delle tappe `moving`

- Ogni tappa `moving` ha **almeno 5** coppie `[lat, lng]` in `waypoints`.
- I waypoint devono descrivere un **percorso lineare credibile** lungo una
  delle polilinee di `locations.json` (`paths`), non punti sparsi a caso.
- La distanza tra due waypoint consecutivi deve essere di **poche decine di
  metri** (niente salti bruschi da un capo all'altro della città).
- Tutti i waypoint devono rientrare nell'area di gioco definita sopra.
- `speed` realistico: valori tra **2 e 4**.

## Checklist rapida prima di consegnare l'output

- [ ] `start`/`end` e ogni tappa `photo`/`word` distano **≤ ~25 m** da un POI
      di `locations.json` (il validatore emette errori oltre).
- [ ] Ogni `waypoints` di una `moving` segue una polilinea di `locations.json`
      (`lungomare_argentina`, `rotonda_sant_ampelio`,
      `banchina_schiavi_del_mare`, `via_romana`, `borgo_antico`), con salti
      tra waypoint di poche decine di metri.
- [ ] Tutte le lat/lng sono dentro `lat 43.777–43.784`, `lng 7.667–7.677`.
- [ ] Nessuna sovrapposizione totale tra `start`, tappe ed `end`.
- [ ] Percorso complessivo plausibile a piedi in 15-40 minuti.