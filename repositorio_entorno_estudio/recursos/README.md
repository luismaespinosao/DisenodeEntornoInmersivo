# Recursos que el prototipo necesita

Estos archivos **no están en el repositorio**: son pesados o su licencia de redistribución no está confirmada. Se esperan en la misma carpeta que el `index.html`.

## Archivos propios del prototipo

| Archivo | Tamaño aprox. | Uso | Procedencia / licencia |
|---|---|---|---|
| `asistente.glb` | 12 MB | Modelo 3D del asistente KodKod | PENDIENTE: indicar autoría y licencia |
| `fondo-bosque.jpg` | 1.4 MB | Panorámica 360° del escenario Bosque | PENDIENTE: confirmar licencia de redistribución (origen: Freepik) |
| `fondo-biblioteca.jpg` | 0.4 MB | Panorámica 360° del escenario Biblioteca | PENDIENTE: confirmar licencia (origen: Freepik) |
| `fondo-espacio.jpg` | 1.3 MB | Panorámica 360° del escenario Espacio | PENDIENTE: confirmar licencia (origen: Freepik) |
| `sonido-lofi.mp3` | 35 MB | Paisaje sonoro lofi | PENDIENTE: indicar fuente y licencia |
| `sonido-naturaleza.mp3` | 12 MB | Paisaje sonoro de naturaleza | PENDIENTE: indicar fuente y licencia |
| `lectura.pdf` (solo v1) | 0.2 MB | Texto del visor PDF de la primera prueba | PENDIENTE: confirmar autorización para redistribuir |

## Bibliotecas (`vendor/`)

| Archivo | Biblioteca | Licencia |
|---|---|---|
| `aframe.min.js` | A-Frame 1.5.0 (https://aframe.io) | MIT |
| `meshopt_decoder.js` | meshoptimizer (https://github.com/zeux/meshoptimizer) | MIT |
| `pdf.min.js` y `pdf.worker.min.js` (solo v1) | PDF.js (https://mozilla.github.io/pdf.js/) | Apache 2.0 |

Las tipografías (Inter, Montserrat, EB Garamond, Hanken Grotesk) se cargan desde Google Fonts, por lo que hace falta conexión a Internet.

Nota: la carpeta de trabajo también contenía `kodkod-v2.glb`, un modelo posterior que ninguna de las dos versiones del prototipo carga; no se usó en el estudio.
