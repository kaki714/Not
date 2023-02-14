import platform
import os

def run():
    print('###### # # # #######')
    print('#### # #  # # ######')
    print('#### ##    ## ######')
    print('#####  #  #  #######')
    print('###### ### #########')
    print('# OS name: ', platform.system())
    if "Linux" in platform.system():
        print('Comand nc linux')
    elif "Windows" in platform.system():
        print('Comand nc windows')
    print('####################')
