import os
import time
import shutil
import sys

# Discord: harypota#3867

def wylaczFivem():
    os.system('TASKKILL /F /IM Steam.exe')
    os.system('TASKKILL /F /IM Fivem.exe')

def usunCache():
    print('Usuwanie folderu cache...')
    time.sleep(3)
    shutil.rmtree(r'C:\Users\User\AppData\Local\FiveM\FiveM.app\cache', ignore_errors=True) # Wpisz swoją sciezke do cache (User)

print('''Czy na pewno chcesz usunąć cache?
      \n---------------------------------
      \nWyłączy to także Fivema oraz Steama
''')
time.sleep(1)
x = input('tak/nie: ')
if x == 'tak':
    wylaczFivem()    # Wylaczanie Steama i Fivema
    usunCache()     # Usuwanie folderu Cache
    time.sleep(2)
    sys.exit('Usunięty!')
else:
    sys.exit('Nie udane!')