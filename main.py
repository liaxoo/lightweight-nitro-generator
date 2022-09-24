import ctypes
import string
import os
import time
from colorama import Fore


time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

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
        import requests
        response = requests.get(url)  # Get the responce from the url
        time.sleep(.4)
        print('[' '\033[32m' + '+' + '\033[39m' ']' + '\033[39m' ' You are connected to the internet!')
    except requests.exceptions.ConnectionError:
        time.sleep(.4)
        print('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' Internet check failed, please try again!')
        exit() 

#print('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' Initializing, please wait...')
print('\033[39m') # and reset to default color

class NitroGen:  # Initialise the class
    def __init__(self):  # The initaliseaiton function
        self.fileName = "Nitro Codes.txt"  # Set the file name the codes are stored in

    def main(self):  # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        if os.name == "nt":  # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Made by Drillenissen#4268")  # Change the
        else:  # Or if it is unix
            print(f'\33]0;Nitro Generator and Checker - Made by Drillenissen#4268\a',
                  end='', flush=True)  # Update title of command prompt

        ##RUN CHECKS 
        moduleCheck();
        wifiCheck();



if __name__ == '__main__':
    Gen = NitroGen()  # Create the nitro generator object
    Gen.main()  # Run the main code
