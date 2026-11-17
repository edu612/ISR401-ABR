#!/usr/bin/env python3
"""Compila main.tex a PDF usando Tectonic.

Requiere que tectonic esté instalado y disponible en el PATH.
Uso: python compilar.py
"""
from pathlib import Path
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "main.tex"
OUTPUT = BASE / "main.pdf"

def main() -> int:
    if not SOURCE.is_file():
        print(f"No se encontró el archivo: {SOURCE}", file=sys.stderr)
        return 1
    tectonic = shutil.which("tectonic")
    if tectonic is None:
        print("No se encontró Tectonic. Instálalo y vuelve a ejecutar este script.", file=sys.stderr)
        return 1
    result = subprocess.run(
        [tectonic, "--keep-logs", "--keep-intermediates", "-o", str(BASE), str(SOURCE)],
        cwd=BASE,
        check=False,
    )
    if result.returncode != 0:
        print("La compilación falló. Revisa los mensajes anteriores.", file=sys.stderr)
        return result.returncode
    if OUTPUT.is_file():
        print(f"PDF generado correctamente: {OUTPUT}")
        return 0
    print("Tectonic terminó, pero no se encontró main.pdf.", file=sys.stderr)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
