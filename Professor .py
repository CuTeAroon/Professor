import os, platform
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
from Professor import menu
    menu()