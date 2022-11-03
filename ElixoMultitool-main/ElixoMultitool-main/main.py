import random
import time
import colorama
import pyautogui as spam
import os
from os import system
from colorama import Back, Fore, Style

def gen():
    system("title " + "ELIXO GEN BY eldoxx#5549")

    caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    nitrocode = ''

    with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"Merci d'utiliser Elixo Gen !\n")

            nitroFile.close()

    colorama.init(autoreset=True)

    print("""███████╗██╗     ██╗██╗  ██╗ ██████╗      ██████╗ ███████╗███╗   ██╗    ██╗   ██╗██╗  ██╗
██╔════╝██║     ██║╚██╗██╔╝██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║    ██║   ██║██║  ██║
█████╗  ██║     ██║ ╚███╔╝ ██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║    ██║   ██║███████║
██╔══╝  ██║     ██║ ██╔██╗ ██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║    ╚██╗ ██╔╝╚════██║
███████╗███████╗██║██╔╝ ██╗╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║     ╚████╔╝      ██║
╚══════╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝      ╚═══╝       ╚═╝""")
    print(Fore.RED + '                                                       by eldoxx#5549\n                                                    WE SUPPORT RUSSIANS HACKERS...')
    time.sleep(1.5)

    while True:
        nitrocode = ''
        
        time.sleep(0.2)

        for i in range(24):
            nitrocode = f"{nitrocode}{random.choice(caracteres)}"

        print(Fore.BLUE + "Status : " + Fore.RED + "[INVALIDE] " + Fore.RED + f"               https://discord.gift/{nitrocode}")

        with open("NITROS EZ.txt", "a+") as nitroFile:

            nitroFile.write(f"https://discord.gift/{nitrocode}\n")

            nitroFile.close()

def mdp():


    system("title " + "Générateur de mot de passe facile !")

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOP¨QRSTUVWXYZ"
    number = "0123456789"
    symbols = "@#$%&*/\?"

    Use_for = lower_case + upper_case + number + symbols
    lenght_for_pass = 10                                         # Changez ceci pour changer la longueur ! (par exemple 8)



    while True:
        print("""███████╗██╗     ██╗██╗  ██╗ ██████╗     ███╗   ███╗██████╗ ██████╗     ██╗   ██╗ ██╗
██╔════╝██║     ██║╚██╗██╔╝██╔═══██╗    ████╗ ████║██╔══██╗██╔══██╗    ██║   ██║███║
█████╗  ██║     ██║ ╚███╔╝ ██║   ██║    ██╔████╔██║██║  ██║██████╔╝    ██║   ██║╚██║
██╔══╝  ██║     ██║ ██╔██╗ ██║   ██║    ██║╚██╔╝██║██║  ██║██╔═══╝     ╚██╗ ██╔╝ ██║
███████╗███████╗██║██╔╝ ██╗╚██████╔╝    ██║ ╚═╝ ██║██████╔╝██║          ╚████╔╝  ██║
╚══════╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═╝     ╚═╝╚═════╝ ╚═╝           ╚═══╝   ╚═╝""")
        password = "".join(random.sample(Use_for, lenght_for_pass))
        print(f"[?] Votre mot de passe est {password}")
        enter_ttt = input("[!] Appuie sur entrée pour regénérer...")
        system("cls")

def spam():
    limite = "5"

    print("""███████╗██╗     ██╗██╗  ██╗ ██████╗     ███████╗██████╗  █████╗ ███╗   ███╗    ██╗   ██╗ ██╗
██╔════╝██║     ██║╚██╗██╔╝██╔═══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██║   ██║███║
█████╗  ██║     ██║ ╚███╔╝ ██║   ██║    ███████╗██████╔╝███████║██╔████╔██║    ██║   ██║╚██║
██╔══╝  ██║     ██║ ██╔██╗ ██║   ██║    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ╚██╗ ██╔╝ ██║
███████╗███████╗██║██╔╝ ██╗╚██████╔╝    ███████║██║     ██║  ██║██║ ╚═╝ ██║     ╚████╔╝  ██║
╚══════╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝      ╚═══╝   ╚═╝
                                                                by eldoxx#5549
                                                                elixo team
                                                       paypal.me/ElixoTeam""")

    message = input("Quel mess tu veut spam bg ? ")
    print("Va dans la zone de texte et attend 5 sec stp")

    i = 0

    time.sleep(5)

    print("""RIP TA VICTIME
SPAMMED BY ELIXO
Fait nous un don ! : paypal.me/ElixoTeam""")

    while i<int(limite):
        spam.typewrite(message)
        spam.press("Enter")

def genr():
    print("""███████╗██╗     ██╗██╗  ██╗ ██████╗     ██████╗ ██████╗ ██╗  ██╗     ██████╗ ███████╗███╗   ██╗    ██╗   ██╗ ██╗
██╔════╝██║     ██║╚██╗██╔╝██╔═══██╗    ██╔══██╗██╔══██╗╚██╗██╔╝    ██╔════╝ ██╔════╝████╗  ██║    ██║   ██║███║
█████╗  ██║     ██║ ╚███╔╝ ██║   ██║    ██████╔╝██████╔╝ ╚███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║    ██║   ██║╚██║
██╔══╝  ██║     ██║ ██╔██╗ ██║   ██║    ██╔══██╗██╔══██╗ ██╔██╗     ██║   ██║██╔══╝  ██║╚██╗██║    ╚██╗ ██╔╝ ██║
███████╗███████╗██║██╔╝ ██╗╚██████╔╝    ██║  ██║██████╔╝██╔╝ ██╗    ╚██████╔╝███████╗██║ ╚████║     ╚████╔╝  ██║
╚══════╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝      ╚═══╝   ╚═╝""")

    caracteres = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    time.sleep(3)

    while True:
        rbxcode1 = ''
        rbxcode2 = ''
        rbxcode3 = ''
        rbxcode4 = ''
        
        time.sleep(0.2)

        for i in range(5):
            rbxcode1 = f"{rbxcode1}{random.choice(caracteres)}"
            rbxcode2 = f"{rbxcode2}{random.choice(caracteres)}"
            rbxcode3 = f"{rbxcode3}{random.choice(caracteres)}"
            rbxcode4 = f"{rbxcode4}{random.choice(caracteres)}"

        print(Fore.RED + f"{rbxcode1}-{rbxcode2}-{rbxcode3}-{rbxcode4}")

        with open("robux.txt", "a+") as rbxFile:

            rbxFile.write(f"{rbxcode1}-{rbxcode2}-{rbxcode3}-{rbxcode4}\n")

            rbxFile.close()

print("""███████╗██╗     ██╗██╗  ██╗ ██████╗     ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
██╔════╝██║     ██║╚██╗██╔╝██╔═══██╗    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
█████╗  ██║     ██║ ╚███╔╝ ██║   ██║    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
██╔══╝  ██║     ██║ ██╔██╗ ██║   ██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
███████╗███████╗██║██╔╝ ██╗╚██████╔╝    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

[1] Elixo Gen Nitro                                     [3] Elixo Gen Robux (NEW!)
[2] Elixo Spam                                          [4] Elixo mdp gen""")

choix = input(">")
system("cls")


if choix == "1":
    gen()

if choix == "2":
    spam()

if choix == "3":
    genr()

if choix == "4":
    mdp()