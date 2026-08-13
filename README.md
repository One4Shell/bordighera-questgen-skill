# bordighera-questgen-skill

[#bordighera-questgen-skill](#bordighera-questgen-skill)

Installa la skill agent **bordighera-questgen** in qualsiasi progetto: `SKILL.md`,
i documenti in `references/` (schema JSON, esempio di riferimento, regole di
coordinate e stile narrativo) e `scripts/validate.py` per validare l'output
generato prima di consegnarlo.

La skill insegna al tuo coding agent (Claude Code, OpenCode, Codex, Cursor e
altri) a generare **masterquest** complete per "UrbanQuest Bordighera", un
gioco urbano a tappe nella città di Bordighera (Italia) — rispettando sempre
lo stesso schema JSON, scrivendo il risultato nel file `masterquest.json`
nella cartella corrente di lavoro. Vedi `skills/bordighera-questgen/SKILL.md`
per il pattern completo.

## Install (consigliata)

[#install-consigliata](#install-consigliata)

Questo repo segue la [Agent Skills specification](https://agentskills.io),
quindi si installa con un solo comando via [`npx skills`](https://github.com/vercel-labs/skills)
— nessun clone, nessuna configurazione:

```
npx skills add https://github.com/One4Shell/bordighera-questgen-skill --skill bordighera-questgen
```

`npx skills` rileva automaticamente quali coding agent hai installato e copia
(o crea un symlink del)la skill nella cartella giusta per ciascuno — `.agents/skills/`
per OpenCode/Codex/Cursor/Amp, `.claude/skills/` per Claude Code, e così via.
Aggiungi `-a <agent>` per puntare a un agente specifico, o `-g` per installare
globalmente invece che per progetto. Vedi [vercel-labs/skills](https://github.com/vercel-labs/skills)
per l'elenco completo delle opzioni.

## Install (senza npm)

[#install-senza-npm](#install-senza-npm)

Se preferisci non dipendere dalla CLI `skills`, usa l'installer shell incluso
in questo repo:

```
curl -fsSL https://raw.githubusercontent.com/One4Shell/bordighera-questgen-skill/main/install.sh | bash
```

Per passare opzioni attraverso la pipe, usa `bash -s --`:

```
curl -fsSL https://raw.githubusercontent.com/One4Shell/bordighera-questgen-skill/main/install.sh | bash -s -- --claude
```

Oppure clona ed esegui localmente (nessun accesso di rete necessario
all'installazione):

```
git clone https://github.com/One4Shell/bordighera-questgen-skill.git
cd bordighera-questgen-skill
./install.sh --dir /path/to/your/project
```

### Opzioni di `install.sh`

[#opzioni-di-installsh](#opzioni-di-installsh)

```
--dir <path>     Root del progetto in cui installare (default: cartella corrente)
--path <path>    Percorso di installazione custom, relativo a --dir
                  (default: .agents/skills/bordighera-questgen)
--claude         Scorciatoia per --path .claude/skills/bordighera-questgen
--force          Sovrascrive i file esistenti (default: salta i file già presenti)
-h, --help       Mostra l'help
```

Variabili d'ambiente (usate solo nel caso `curl | bash`, cioè senza checkout
locale):

```
BORDIGHERA_QUESTGEN_REPO     "owner/repo" GitHub da cui scaricare (default: incorporato in install.sh)
BORDIGHERA_QUESTGEN_BRANCH   Branch/ref da usare (default: main)
```

Entrambi i metodi non sovrascrivono mai i file esistenti a meno che non venga
passato `--force`, quindi è sicuro rieseguirli.

## Cosa viene installato

[#cosa-viene-installato](#cosa-viene-installato)

```
skills/bordighera-questgen/       # layout del repo — scopribile anche come .agents/skills/bordighera-questgen
├── SKILL.md                      # entry point che l'agent legge
├── scripts/
│   └── validate.py               # valida un file masterquest.json contro lo schema
└── references/
    ├── schema.md                 # schema JSON completo di MasterQuest e SottoQuest
    ├── example-output.md         # esempio di riferimento (struttura, ordine campi, stile)
    ├── coordinates.md            # regole geografiche per Bordighera e per i waypoint moving
    └── style-guide.md            # regole di narrativa, tono e struttura in 5 tappe
```

## Dopo l'installazione

[#dopo-linstallazione](#dopo-linstallazione)

Punta il tuo agent su un progetto che contiene la skill, poi chiedi di
generare una masterquest a partire da un testo/tema:

```
Genera una masterquest per UrbanQuest Bordighera a partire da questo testo:
<<<< ... testo di ispirazione ... >>>>
```

L'agent leggerà `SKILL.md`, applicherà lo schema e le regole in `references/`
e scriverà il risultato nel file **`masterquest.json`** nella cartella
corrente di lavoro.

Per validare il file generato prima di importarlo nel gioco:

```
python3 .agents/skills/bordighera-questgen/scripts/validate.py masterquest.json
```

## License

[#license](#license)

MIT
