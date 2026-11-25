#!/usr/bin/env bash
# Installe tout ce qu'il faut pour générer les vidéos (polices, voix Kokoro, paquets Python).
# Idempotent : relançable sans risque. Les fichiers vont dans $MSQ_ASSETS (défaut ~/msq-assets).
set -euo pipefail
A="${MSQ_ASSETS:-$HOME/msq-assets}"
mkdir -p "$A/fonts" "$A/voices"

pip install --break-system-packages -q kokoro-onnx soundfile pillow sympy fonttools scipy numpy

cd "$A/fonts"
if [ ! -f package/files/poppins-latin-800-normal.woff ]; then
  npm pack @fontsource/poppins@5 --silent >/dev/null && tar xzf fontsource-poppins-*.tgz
fi
if [ ! -f inter/package/files/inter-latin-400-normal.woff ]; then
  mkdir -p inter && npm pack @fontsource/inter@5 --silent >/dev/null && tar xzf fontsource-inter-*.tgz -C inter
fi

cd "$A/voices"
BASE=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "$f" ] || curl -sSL --retry 3 -o "$f" "$BASE/$f"
done
command -v ffmpeg >/dev/null || { echo "ffmpeg manquant"; exit 1; }
echo "OK : assets dans $A"
