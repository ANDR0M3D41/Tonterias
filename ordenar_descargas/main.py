import os, sys
import shutil

dir_descargas = os.path.expanduser('~') + "/Descargas/"

formatos_documentos = ['.pdf', '.odt', '.xls', '.torrent']
formatos_videos = ['.mp4', '.mkv']
formatos_audios = ['.mp3', '.flac', '.wav']
formatos_comprimidos = ['.zip', '.rar', '.tar', '.xz', '.gz', '.tgz']
formatos_ejecutables = ['.AppImage', '.sh']
formatos_iso = ['.iso']
formatos_doom = ['.wad', '.pk3']

def enlistar(contenido_directorio):
    cantidad_contenido = len(contenido_directorio)
    archivos_directorio = list(contenido_directorio)

    for i in range(cantidad_contenido):
        if os.path.isdir(dir_descargas + contenido_directorio[i]) == True:
            archivos_directorio.remove(contenido_directorio[i])

    return archivos_directorio

def ordenar(archivos):
    for i in range(len(archivos)):
        extension = os.path.splitext(archivos[i])[1]

        for x in formatos_documentos:
            if extension == x:
                shutil.move(dir_descargas + archivos[i], dir_descargas + "DOCUMENTOS/" + archivos[i])

        for x in formatos_comprimidos:
            if extension == x:
                shutil.move(dir_descargas + archivos[i], dir_descargas + "COMPRIMIDOS/" + archivos[i])
        
        for x in formatos_ejecutables:
            if extension == x:
                shutil.move(dir_descargas + archivos[i], dir_descargas + "EXEC/" + archivos[i])
        
        for x in formatos_videos:
            if extension == x:
                shutil.move(dir_descargas + archivos[i], dir_descargas + "VIDEOS/" + archivos[i])

        for x in formatos_audios:
            if extension == x:
                shutil.move(dir_descargas + archivos[i], dir_descargas + "AUDIOS/" + archivos[i])
            
        for x in formatos_doom:
            if extension == x:
                shutil.move(dir_descargas + archivos[i], dir_descargas + "roms/doom/" + archivos[i])

        for x in formatos_iso:
            if extension == x:
                shutil.move(dir_descargas + archivos[i], dir_descargas + "ISOS/" + archivos[i])

def main():
    contenido_directorio = os.listdir(dir_descargas)
    directorios_destino = ("COMPRIMIDOS", "EXEC", "DOCUMENTOS", "AUDIOS", "VIDEOS", "ISOS")
    cont = 0
    
    for i in contenido_directorio:
        for x in directorios_destino:
            if i == x:
                cont += 1

    if cont == len(directorios_destino):
        archivos_enlistados = enlistar(contenido_directorio)
        ordenar(archivos_enlistados)

    else:
        print("¿Desea crear los Directorios Necesarios?")
        select = input("S/N > ")
        if select.lower() == 's':
            for i in range(len(directorios_destino)):
                try:
                    os.mkdir(dir_descargas + directorios_destino[i])
                except FileExistsError:
                    continue 
            main()
        else:
            sys.exit()


if __name__ == "__main__":
    main()
