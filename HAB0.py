import time, subprocess, hashlib, cryptography, string, random
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import Label

class DownLoader:
    
    def __init__(self):
        
        DownLoadingList = [""]
        DownLoadingName = [""]

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


class PassWdGenerator:

    def __init__(self):
        
        The_PassWd = ''

        for i in range(6):

            self.letters = string.ascii_letters[random.randint(0, 51)]
            self.symbols = string.punctuation[random.randint(0, 31)]
            self.numbers = str(random.randint(0, 3500))
            The_PassWd += self.letters + self.numbers + self.symbols

        print("The PassWord Is : ",The_PassWd)

class TakingBreak:

    def __init__(self):
        
        while True:
            
            time.sleep(2700)
            root = tk.Tk()
            root.geometry("350x350")
            root.minsize(350, 350)
            root.maxsize(350, 350)

            root.title("Take A Break Bro Its Not Important Than Health")
            self.Text = Label(text="Bro Its Not Important Than Health", background='red', font=30)
            self.Text.pack()

            root.mainloop()

user_input = input("""What Do You Want Buddy : 

IF Wanna Download Packages Write Download
IF Wanna Encrypt Message Or File Write Encrypt
IF Wanna Decrypt Message Or File Write Decrypt
IF Wanna Generate PassWord Write Password
IF Wanna Set Time Write SettingTimer
                   
                   Write Here :  """)

user_input.lower()

if user_input == "download":
    Run = DownLoader()

elif user_input == "encrypt":
    Run = Encrypt()

elif user_input == "password":
    Run = PassWdGenerator()

elif user_input == "settingtimer":
    Run = TakingBreak()

else:
    raise ValueError("Bro Please Write Correctly")