""""
ffmpg -i "Entrada" -i "Legenda" -c:v libx264 -crf 23 -present ultrawfast
-c:a aac -b:a 320k -c:s srt -map a -map 1:0 "SAIDA" -SS 00:00:00 -TO 00:00:10
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'C:\ffmpeg\bin\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = ''

caminho_origem = r'C:\Users\jucel\Desktop\ar1'
caminho_destinho = r'C:\Users\jucel\Desktop\ar2'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        nome_novo_arquivo = nome_arquivo + '_novo' + extensao_arquivo
        arquivo_saida = f'{caminho_destinho}/{nome_arquivo}_NOVO.mp3'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda}' \
                  f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio}' \
                  f'{debug} {map_legenda}"{arquivo_saida}"'
        os.system(comando)

        print(comando)
