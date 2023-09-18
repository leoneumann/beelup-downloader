# Beelup Video Downloader

Este repositorio contiene un script de Python para descargar un video subido por [Beelup](https://beelup.com/).

## Requisitos

Este script utiliza el modulo `requests` (ya integrado en Python 3.7+) para obtener los segmentos de video mediante `GET requests`. 

## Iniciar descarga

Para iniciar la descarga de un  video deseado, primero se debe abrir el reproductor desde la web en el partido que se quiera descargar, solo para obtener el `id` necesario para completar en el script.

La dirección URL generada por el reproductor será del estilo:

```https://beelup.com/player.php?id=8890989```

En el script se debe reemplazar `BEELUP_ID` por el `id` que figura en la dirección URL, y listo!

## Formato de salida

Primero se generará un archivo `video.segments.json` que contiene el listado de todos los segmentos de video a descargar.

Al final la descarga el video queda almacenado en el archivo `video.ts` (Transport Stream) que puede ser reproducido con VLC o transformado a otro formato como MP4 con cualquier herramienta de conversión (como Format Factory).