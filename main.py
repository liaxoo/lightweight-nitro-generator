import ctypes
import string
import os
import time
from colorama import Fore

## MODULE CHECK FUNCTION
def moduleCheck():
    try:  
        import requests  # Try to import requests
    except ImportError:  # If it has not been installed
        # Tell the user it has not been installed and how to install it
        input(
            f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
        exit()  # Exit the program
    try:  
        import colorama  # Try to import requests
    except ImportError:  # If it has not been installed
        # Tell the user it has not been installed and how to install it
        input(
            f"Module colorama not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install colorama'\nPress enter to exit")
        exit()  # Exit the program


## WIFI CHECK
def wifiCheck():
    print('[' '\033[33m' + '!' + '\033[39m' ']' + '\033[39m' ' Checking your internet connection, please wait...')
    url = "https://google.com"
    try:
        response = requests.get(url)  # Get the responce from the url
        time.sleep(.4)
        print('[' '\033[32m' + '+' + '\033[39m' ']' + '\033[39m' ' You are connected to the internet!')
    except requests.exceptions.ConnectionError:
        time.sleep(.4)
        print('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' Internet check failed, please try again!')
        exit() 

#print('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' Initializing, please wait...')
print('\033[39m') # and reset to default color