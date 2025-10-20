
'''Heterogenous Automated Block Version 0 = HABv0'''

import time, subprocess, hashlib, cryptography, string, random
from cryptography.fernet import Fernet
import ipaddress

class DownLoader:
    
    def __init__(self):
        
        DownLoadingList = ["sudo apt update -y", "sudo apt full-upgrade -y", "sudo apt install code"]
        DownLoadingName = ["UPDATE", "UPGRADE", "VSCODE"]

        def Worker(Commands, Names):

            shelling = subprocess.run(f"{Commands}", shell=True,
                        capture_output=True, text=True)
            
            if shelling.stdout:
                print(shelling.stdout)
            elif shelling.stderr:
                with open("Error.txt", 'a') as file:
                    file.write(Commands + '\n')

        for i in range(len(DownLoadingList)):
            Worker(DownLoadingList[i], DownLoadingName[i])

class Encrypt:
    
    def __init__(self, Message):
        
        key = '60846a2369ad408101216c7f952be7019559acfa146e6b5c51d0a18424a620a22e937e5650ed332cbdb9ebe21f03f86207078958e0ef7b60bb285851cf9f9a32'

class Decrypt:
    
    def __init__(self, Enc_Message):
        pass

class Hashing:

    def __init__(self, text):

        HASH = hashlib.sha256()
        text = text.encode()
        HASH.digest()
        
        print(f"This Is The Hash : {HASH.hexdigest()}")

class PassWdGenerator:

    def __init__(self):
        
        The_PassWd = ''

        for i in range(3):

            self.letters = string.ascii_letters[random.randint(0, 51)]
            self.symbols = string.punctuation[random.randint(0, 31)]
            self.numbers = str(random.randint(0, 3500))
            The_PassWd += self.letters + self.numbers + self.symbols

        print("The PassWord Is : ",The_PassWd)
        Run = Hashing(The_PassWd)

        count = 0
        for j in The_PassWd:
            count+=1

        print(f"The Length OF Your Password Is: {count}")


class TakingBreak:

    def __init__(self):
        
        while True:
            
            count = 0

            for i in range(2700):
                
                time.sleep(1)
                count += 1
                print(f"{2700-count} Seconds Left In Break")

class ScanNet:

    def __init__(self, ip):

        listOfCommands = ["nmap --top-ports 100 -T4 ", "sudo nmap -sV -sC -T4 ", "sudo nmap -sS -p- -T4 -Pn ",]

        try:
            self.target = str(ipaddress.ip_address(ip))
        except ValueError:
            raise ValueError(f"Invalid IP address: {ip}")

        for command in listOfCommands:
            Run = subprocess.run(f"{command} {self.target}", capture_output=True, text=True, shell=True)

            if Run.stdout:
                print(f'The OutPut : {Run.stdout}')
            


while True:
    user_input = input("""What Do You Want Buddy : 

    IF Wanna Download Packages Write Download
    IF Wanna Encrypt Message Or File Write Encrypt
    IF Wanna Decrypt Message Or File Write Decrypt
    IF Wanna Generate PassWord Write Password
    IF Wanna Set Time Write ForBreak
    IF Wanna Scan The Network Write ScanNetwork
                        
                    Write Here :  """)


    print('\n')

    if user_input.lower() == "download":
        Run = DownLoader()

    elif user_input.lower() == "encrypt":
        Run = Encrypt()

    elif user_input.lower() == "password":
        Run = PassWdGenerator()

    elif user_input.lower() == "forbreak":
        Run = TakingBreak()

    elif user_input.lower() == "scannetwork":
        ip = input("ENTER THE IP ADDRESS FOR SCANNING NETWORK : ")
        Run = ScanNet(ip)

    elif user_input == "hashing":
        user_hash = input("Enter The Text Which You Want To Turn It Into Hash : ")
        Run = Hashing(user_hash)

    else:
        raise ValueError("Bro Please Write Correctly")