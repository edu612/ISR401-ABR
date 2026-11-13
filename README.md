# ISR401 · GA-PRAC-01

En este repositorio estamos armando en grupo la comparación de modelos de proceso de requisitos aplicada a los cuatro escenarios de la guía. 

## Archivos del informe

- `FORM-PC-01/main.tex`: fuente LaTeX del avance.
- `FORM-PC-01/referencias.bib`: referencias editables en formato BibTeX.
- `FORM-PC-01/main.pdf`: informe compilado.
- `FORM-PC-01/compilar.py`: script de compilación.

## Compilar el PDF

Se necesita Python 3. El script usa Tectonic para compilar LaTeX. Desde la carpeta raíz del repositorio ejecuta:

```powershell
python .\FORM-PC-01\compilar.py
```

Si Tectonic ya está instalado, el script compila el archivo y actualiza `FORM-PC-01/main.pdf`. Si no lo encuentra, pregunta si quieres instalarlo; al aceptar, descarga el ejecutable oficial, lo agrega al `PATH` del usuario y continúa con la compilación. En compilaciones posteriores detecta la instalación y solo genera el PDF.

También puedes ejecutar el script desde la carpeta `FORM-PC-01`:

```powershell
cd .\FORM-PC-01
python .\compilar.py
```

La primera compilación puede necesitar conexión a Internet para que Tectonic descargue los paquetes LaTeX que falten. Para usar Tectonic en otro sistema operativo, consulta https://tectonic-typesetting.github.io/install.html.

## Alcance actual

Este es un avance de trabajo: incluye los criterios de comparación y la matriz, elección y riesgos para los dos primeros escenarios. El grupo completará los otros escenarios y el apartado de actores y framework antes de cerrar la entrega.
