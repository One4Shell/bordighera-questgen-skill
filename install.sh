#!/usr/bin/env bash
# install.sh — installa la skill "bordighera-questgen" in un progetto.
#
# Uso:
#   ./install.sh [--dir <path>] [--path <path>] [--claude] [--force]
#
# Oppure via curl (senza checkout locale):
#   curl -fsSL https://raw.githubusercontent.com/<owner>/<repo>/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/<owner>/<repo>/main/install.sh | bash -s -- --claude

set -euo pipefail

SKILL_NAME="bordighera-questgen"
REPO="${BORDIGHERA_QUESTGEN_REPO:-<owner>/bordighera-questgen-skill}"
BRANCH="${BORDIGHERA_QUESTGEN_BRANCH:-main}"

TARGET_DIR="$(pwd)"
INSTALL_PATH=".agents/skills/${SKILL_NAME}"
FORCE=0

usage() {
  cat <<EOF
Uso: install.sh [opzioni]

  --dir <path>     Root del progetto in cui installare (default: cartella corrente)
  --path <path>    Percorso di installazione custom, relativo a --dir
                    (default: .agents/skills/${SKILL_NAME})
  --claude         Scorciatoia per --path .claude/skills/${SKILL_NAME}
  --force          Sovrascrive i file esistenti (default: salta i file già presenti)
  -h, --help       Mostra questo help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dir)
      TARGET_DIR="$2"; shift 2 ;;
    --path)
      INSTALL_PATH="$2"; shift 2 ;;
    --claude)
      INSTALL_PATH=".claude/skills/${SKILL_NAME}"; shift ;;
    --force)
      FORCE=1; shift ;;
    -h|--help)
      usage; exit 0 ;;
    *)
      echo "Opzione sconosciuta: $1" >&2; usage; exit 1 ;;
  esac
done

DEST="${TARGET_DIR%/}/${INSTALL_PATH}"
mkdir -p "${DEST}"

copy_tree() {
  local src="$1" dst="$2"
  if [[ "${FORCE}" -eq 1 ]]; then
    cp -rf "${src}/." "${dst}/"
  else
    # Copia solo i file che non esistono già a destinazione.
    (cd "${src}" && find . -type f) | while read -r rel; do
      mkdir -p "${dst}/$(dirname "${rel}")"
      if [[ -e "${dst}/${rel}" ]]; then
        echo "skip (già presente): ${INSTALL_PATH}/${rel}"
      else
        cp "${src}/${rel}" "${dst}/${rel}"
        echo "installato: ${INSTALL_PATH}/${rel}"
      fi
    done
  fi
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"

if [[ -d "${SCRIPT_DIR}/skills/${SKILL_NAME}" ]]; then
  # Checkout locale già disponibile (git clone o esecuzione dal repo).
  copy_tree "${SCRIPT_DIR}/skills/${SKILL_NAME}" "${DEST}"
else
  # Nessun checkout locale (caso `curl | bash`): scarica il tarball del branch.
  TMP_DIR="$(mktemp -d)"
  trap 'rm -rf "${TMP_DIR}"' EXIT

  echo "Scaricamento ${REPO}@${BRANCH}..."
  curl -fsSL "https://codeload.github.com/${REPO}/tar.gz/refs/heads/${BRANCH}" \
    | tar -xz -C "${TMP_DIR}"

  SRC_DIR="$(find "${TMP_DIR}" -maxdepth 1 -type d -name '*-*' | head -n1)/skills/${SKILL_NAME}"
  if [[ ! -d "${SRC_DIR}" ]]; then
    echo "Errore: skill '${SKILL_NAME}' non trovata nel repo scaricato." >&2
    exit 1
  fi
  copy_tree "${SRC_DIR}" "${DEST}"
fi

echo ""
echo "Skill '${SKILL_NAME}' installata in: ${DEST}"
echo "Il tuo coding agent la scoprirà automaticamente in ${INSTALL_PATH}."
