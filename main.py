import ctypes
import string
import os
import time
from xml.etree.ElementTree import tostring

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

## MODULE CHECK 
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
    try:  
        import numpy  # Try to import requests
    except ImportError:  # If it has not been installed
        # Tell the user it has not been installed and how to install it
        input(
            f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
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

## FILE CHECK
def fileCheck():
    import os.path
    fileExists = os.path.exists('Generated Codes.txt')
    if fileExists:
        slowType('[' '\033[32m' + '+' + '\033[39m' ']' + '\033[39m' ' File check successful!', 0.005)
    else:
        slowType('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' Could not find a file to write the codes in. Please create a "Generated Codes.txt" file in the directory or reinstall.', 0.005)
        time.sleep(10)
        exit()
    
## CLEAR SCREEN 
def clearScreen(sleepTime: float):
    if sleepTime != 0:   
        time.sleep(sleepTime)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    else:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            
## CODE CHECKER
def codeChecker(nitro:str, checkType:int):  # Used to check a single code at a time
        import requests
        ## If the user wants to generate and check
        # Generate the request url
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  # Get the response from discord

        if response.status_code == 200:  # If the responce went through
            # Notify the user the code was valid
            print(f" Valid | {nitro} ", flush=True,
                end="" if os.name == 'nt' else "\n")
            with open("Generated Codes.txt", "w") as file:  # Open file to write
                # Write the nitro code to the file it will automatically add a newline
                file.write(nitro)
            return True  # Tell the main function the code was found
        # If the responce got ignored or is invalid ( such as a 404 or 405 )
        else:
            # Tell the user it tested a code and it was invalid
            print("[" '\033[31m' + "INVALID CODE" + '\033[39m' "] " + '\033[39m' + f"{nitro}")
            #print(f" Invalid | {nitro} ", flush=True,
                    #end="" if os.name == 'nt' else "\n")
            return False  # Tell the main function there was not a code found

print('\033[39m') # and reset to default color

class NitroGen:  # Initialise the class
    def __init__(self):  # The initaliseaiton function
        self.fileName = "Generated Codes.txt"  # Set the file name the codes are stored in

    def main(self):  # The main function contains the most important code
        clearScreen(0);

        # Initializing message
        slowType('[' '\033[33m' + '!' + '\033[39m' ']' + '\033[39m' ' Initializing...', 0.05);

        ##time.sleep(2) 

        # Run checks 
        moduleCheck();
        ##time.sleep(1);
        wifiCheck();
        ##time.sleep(1);
        fileCheck();
        time.sleep(1);
        clearScreen(2);

        import requests
        import numpy

        print("""┏━┓╋┏┓┏┓╋╋╋╋╋╋┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋╋┏━━━┳┓╋╋╋╋╋╋╋┏┓
┃┃┗┓┃┣┛┗┓╋╋╋╋╋┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓╋╋╋╋╋╋╋╋╋┃┏━┓┃┃╋╋╋╋╋╋╋┃┃
┃┏┓┗┛┣┓┏╋━┳━━┓┃┃╋┗╋━━┳━┓┏━━┳━┳━┻┓┏╋━━┳━┓╋┏┓╋┃┃╋┗┫┗━┳━━┳━━┫┃┏┳━━┳━┓
┃┃┗┓┃┣┫┃┃┏┫┏┓┃┃┃┏━┫┃━┫┏┓┫┃━┫┏┫┏┓┃┃┃┏┓┃┏┛┏┛┗┓┃┃╋┏┫┏┓┃┃━┫┏━┫┗┛┫┃━┫┏┛
┃┃╋┃┃┃┃┗┫┃┃┗┛┃┃┗┻━┃┃━┫┃┃┃┃━┫┃┃┏┓┃┗┫┗┛┃┃╋┗┓┏┛┃┗━┛┃┃┃┃┃━┫┗━┫┏┓┫┃━┫┃
┗┛╋┗━┻┻━┻┛┗━━┛┗━━━┻━━┻┛┗┻━━┻┛┗┛┗┻━┻━━┻┛╋╋┗┛╋┗━━━┻┛┗┻━━┻━━┻┛┗┻━━┻┛""")

        time.sleep(1);

        slowType('[' '\033[33m' + '?' + '\033[39m' ']' + '\033[39m' ' Enter how much codes you want to generate: ', 0.005, newLine=False)
        
        ## GET NUMBER OF CODES & TYPE
        try:
            ##Number of codes user wants 
            num = int(input(''))  # Ask the user for the amount of codes
        except ValueError:
            input(slowType('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' What you entered wasn\'t a number! Press enter to exit and try again.', 0.005))
            exit()  # Exit program

        slowType('[' '\033[33m' + '?' + '\033[39m' ']' + '\033[39m' ' Got it, generating ' +  str(num) + ' codes. Do you want to [1] generate, or [2] generate and check codes? ', 0.005, newLine=False)
        
        try:
            genType = int(input(''))  # Ask what type of codes will be generated 
        except ValueError:
            input(slowType('[' '\033[31m' + '-' + '\033[39m' ']' + '\033[39m' ' What you entered wasn\'t a number! Press enter to exit and try again.', 0.005))
            exit()  # Exit

        ## GENERATE CODES
        successfulCodes = []  # Valid codes are stored here 
        invalidCodes = 0  # Keep track of how many invalid codes was detected
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        ##GENERATE CODES
        if genType == 1:
            c = numpy.random.choice(chars, size=[num, 16])
            for s in c:
                    code = ''.join(x for x in s)
                    url = f"https:discord.gift/{code}"
                    with open("Generated Codes.txt", "a") as file:  # Open file to write
                                    # Write the nitro code to the file it will automatically add a newline
                                    file.write(url + "\n")
                                    print("[" '\033[32m' + "GENERATED CODE" + '\033[39m' "] " + '\033[39m' + f"{url}") 
        ##GENERATE AND CHECK CODES
        else:
            c = numpy.random.choice(chars, size=[num, 16])
            for s in c:
                try:
                    code = ''.join(x for x in s)
                    url = f"https:discord.gift/{code}"
                    
                    result = codeChecker(url, genType)

                    if result:
                        successfulCodes.append(url)
                    else:
                        invalidCodes += 1
                except KeyboardInterrupt:
                    # If the user interrupted the program
                    print("\nInterrupted by user")
                    break  # Break the loop
        
        if num != 1: print("Finished generating codes.")
        else: print(f"""
Results:
 Valid: {len(successfulCodes)}
 Invalid: {invalidCodes}
 Valid Codes: {', '.join(successfulCodes)}""")  # Give a report of the results of the check

if __name__ == '__main__':
    Gen = NitroGen()  # Create the nitro generator object
    Gen.main()  # Run the main code