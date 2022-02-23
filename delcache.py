import os
import shutil
import sys

def offFivem():
    os.system('TASKKILL /F /IM Steam.exe')
    os.system('TASKKILL /F /IM Fivem.exe')

def delCache():
    shutil.rmtree(r'C:\Users\User\AppData\Local\FiveM\FiveM.app\cache', ignore_errors=True) # Wpisz swoją sciezke do cache (User)

print('''
 ,--.         .         .-,--.      .      .          
| `-' ,-. ,-. |-. ,-.   ' |   \ ,-. |  ,-. |- ,-. ,-. 
|   . ,-| |   | | |-'   , |   / |-' |  |-' |  |-' |   
`--'  `-^ `-' ' ' `-'   `-^--'  `-' `' `-' `' `-' '  
''')

print('Chcesz usunąć Cache?')

odp = input('[tak/nie]: ')

if odp == 'tak':
    offFivem()
    delCache()
    print('Usunięty!')
    sys.exit('Naciśnij Enter aby wyjść!')
else:
    sys.exit('Naciśnij Enter aby wyjść!')
