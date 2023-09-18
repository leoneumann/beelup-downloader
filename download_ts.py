# -----------------------------------------------------------------------------
# download_ts.py module
#
# author: Leonel Neumann (mailto: neumann.leonel@gmail.com)
# -----------------------------------------------------------------------------

import requests
import time

BEELUP_ID = "8890989" # Beelup ID obtenido desde URL del reproductor web

# URL para descargar JSON con listado de segmentos .ts
beelup_json_url = "https://beelup.com/obtener.video.playlist.php?id="+BEELUP_ID+"&formato=json"

print("Descargando lista de segmentos...")
json_r = requests.get(beelup_json_url)

segment_list = json_r.content

with open('video.segments.json', 'wb') as f:
    f.write(segment_list)
f.close()

print("Lista de segmentos obtenida con exito")
segment_list = json_r.json()

print("Iniciando descarga")
with open('video.ts', 'wb') as f:
    segment_cnt = len(segment_list["segmentos"])
    print("Cantidad de segmentos para descargar: "+str(segment_cnt))
    print("Descargando...")
    print("", end="")
    tik = tok = time.time()
    tiempo_restante = 0
    for i, v in enumerate(segment_list["segmentos"]):
        if i != 0:
            tiempo_restante =  (segment_cnt-i)*(tok-tik)/i
        percent = i*100/segment_cnt
        print("\r", end="")
        print("Segmento "+str(i)+"/"+str(segment_cnt)+" ("+f'{percent:.2f}'+"%). Tiempo estimado: "+f'{tiempo_restante:.0f}'+" segundos.", end="")
        url = v["url"]
        r = requests.get(url,stream=True)
        f.write(r.content)
        tok = time.time()

f.close()

print("Descarga finalizada.")