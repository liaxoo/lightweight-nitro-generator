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

## SLOW TYPE EFFECT
def slowType(text: str, speed: float, newLine=True):
    for i in text:  # Loop over the message
        # Print the one charecter, flush is used to force python to print the char
        print(i, end="", flush=True)
        time.sleep(speed)  # Sleep a little before the next one
    if newLine:  # Check if the newLine argument is set to True
        print()  # Print a final newline to make it act more like a normal print statement

## WIFI CHECK
def wifiCheck():
    slowType('[' '\033[33m' + '!' + '\033[39m' ']' + '\033[39m' ' Checking your internet connection, please wait...', 0.005)
    url = "https://google.com"
    try:
        import requests
        response = requests.get(url)  # Get the responce from the url
        time.sleep(.4)
        slowType('[' '\033[32m' + '+' + '\033[39m' ']' + '\033[39m' ' You are connected to the internet!', 0.005)
    except requests.exceptions.ConnectionError:
        time.sleep(.4)
        slowType('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' Internet check failed, please restart & try again!', 0.005)
        exit() 

def clearScreen(sleepTime: float):
    if sleepTime != 0:   
        time.sleep(sleepTime)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    else:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            

#print('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' Initializing, please wait...')
print('\033[39m') # and reset to default color



class NitroGen:  # Initialise the class
    def __init__(self):  # The initaliseaiton function
        self.fileName = "Generated Codes.txt"  # Set the file name the codes are stored in

    def main(self):  # The main function contains the most important code
        clearScreen(0);

        # Initializing message
        slowType('[' '\033[33m' + '!' + '\033[39m' ']' + '\033[39m' ' Initializing...', 0.05);

        time.sleep(2) 

        # Run checks 
        moduleCheck();
        wifiCheck();

        clearScreen(2);

        print("""┏━┓╋┏┓┏┓╋╋╋╋╋╋┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋╋┏━━━┳┓╋╋╋╋╋╋╋┏┓
┃┃┗┓┃┣┛┗┓╋╋╋╋╋┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓╋╋╋╋╋╋╋╋╋┃┏━┓┃┃╋╋╋╋╋╋╋┃┃
┃┏┓┗┛┣┓┏╋━┳━━┓┃┃╋┗╋━━┳━┓┏━━┳━┳━┻┓┏╋━━┳━┓╋┏┓╋┃┃╋┗┫┗━┳━━┳━━┫┃┏┳━━┳━┓
┃┃┗┓┃┣┫┃┃┏┫┏┓┃┃┃┏━┫┃━┫┏┓┫┃━┫┏┫┏┓┃┃┃┏┓┃┏┛┏┛┗┓┃┃╋┏┫┏┓┃┃━┫┏━┫┗┛┫┃━┫┏┛
┃┃╋┃┃┃┃┗┫┃┃┗┛┃┃┗┻━┃┃━┫┃┃┃┃━┫┃┃┏┓┃┗┫┗┛┃┃╋┗┓┏┛┃┗━┛┃┃┃┃┃━┫┗━┫┏┓┫┃━┫┃
┗┛╋┗━┻┻━┻┛┗━━┛┗━━━┻━━┻┛┗┻━━┻┛┗┛┗┻━┻━━┻┛╋╋┗┛╋┗━━━┻┛┗┻━━┻━━┻┛┗┻━━┻┛""")



if __name__ == '__main__':
    Gen = NitroGen()  # Create the nitro generator object
    Gen.main()  # Run the main code




