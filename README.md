# Entorno de Estudio: prototipo de realidad virtual para mejorar la atención en estudiantes universitarios

Material de apoyo de la tesis de maestría **"Diseño e Implementación de un Entorno para Mejorar la Atención en Estudiantes Universitarios durante Sesiones de Estudio"**
(Luis Mario Espinosa Ortiz, Maestría en Medios Interactivos, Universidad Tecnológica de la Mixteca).
Director: Dr. Mario Alberto Moreno Rocha. Codirector: Dr. Miguel García-Ruiz.

El prototipo es una aplicación web en **A-Frame / WebXR** pensada para el **Meta Quest 3S**. Incluye tres escenarios inmersivos (bosque, biblioteca, espacio), paisajes sonoros, temporizador Pomodoro, un panel de lectura y un cuestionario de comprensión.

## Contenido

| Carpeta | Qué contiene |
|---|---|
| `prototipo_v1/` | Versión usada en la **primera prueba de usabilidad** (7 de julio de 2026, 5 participantes). Lectura mediante visor PDF (PDF.js). |
| `prototipo_v2/` | Versión usada en la **segunda prueba** (19 de septiembre y 3 de octubre de 2026, 10 participantes). Panel de lectura nativo en 3D. `index_brexit.html` e `index_spacex.html` son el mismo código y solo difieren en el texto de lectura y su cuestionario. |
| `documentos/` | Instrumentos de las pruebas y de las encuestas, en blanco: cuestionario de hábitos, sondeo inicial, focus group (consentimiento y presentación condensada), guion del facilitador, consentimientos y protocolo de la segunda prueba. |
| `datos/` | Reporte de la encuesta de hábitos (`datos/encuesta_habitos/`) y resultados **agregados** de las dos pruebas de usabilidad (`resumen_agregado.csv`). Ver `datos/README.md`. |
| `recursos/` | Lista de los archivos pesados que el prototipo necesita (modelos, panorámicas, audio) y su procedencia. |
| `scripts/` | Scripts para reproducir el resumen y para anonimizar registros. |

## Cómo ejecutarlo

1. Reúne los recursos que indica `recursos/README.md` y colócalos junto al `index.html` correspondiente, con los mismos nombres.
2. Descarga las bibliotecas en una carpeta `vendor/` (ver `recursos/README.md`).
3. Sirve la carpeta con cualquier servidor estático, por ejemplo `python3 -m http.server`, y abre `http://localhost:8000/index.html`.
4. Para usar el modo VR en el Quest, publica la carpeta con HTTPS (por ejemplo en Netlify) y ábrela desde el navegador del visor.

Las versiones desplegadas durante el estudio fueron:
- v1: https://pruebadeusabilidad1.netlify.app
- v2, texto de SpaceX: https://entornospacex.netlify.app/
- v2, texto del Brexit: https://entornorm.netlify.app

## Aviso: el ritmo cardiaco es simulado

El panel de métricas muestra un "Ritmo cardiaco" en latidos por minuto. **Es un valor simulado**: no proviene de ningún sensor, sino de un número aleatorio entre 68 y 77 que cambia cada segundo. No se registró ni se analizó en el estudio y no debe interpretarse como una medición.

## Datos y privacidad

El consentimiento informado de los participantes autoriza el uso académico de la información y garantiza la confidencialidad de su identidad, pero **no contempla la publicación de datos individuales**. Por eso este repositorio solo publica resultados agregados. Los registros por participante (SUS, VRSUQ, comprensión, observaciones) y las respuestas del sondeo inicial no se publican. Las fotografías y el video de las sesiones requieren autorización aparte y no se incluyen.

## Licencias

- Código del prototipo y scripts: **MIT** (`LICENSE`).
- Documentos y datos agregados: **CC BY 4.0** (`LICENSE-docs.md`).
- Bibliotecas de terceros (A-Frame, meshoptimizer: MIT; PDF.js: Apache 2.0) y recursos gráficos o sonoros: conservan su licencia original. Ver `recursos/README.md`.

## Cómo citar

Ver `CITATION.cff`.
