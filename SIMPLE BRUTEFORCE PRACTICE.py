# pip install pyautogui  "https://pyautogui.readthedocs.io/en/latest/quickstart.html"

# if "Unable to import 'pyautogui'", https://stackoverflow.com/questions/31635140/import-error-for-pyautogui

import random 
import pyautogui


mainChars1 = string.printable
# mainChars = "abcdefghijklmnopqrstuvwxyz0123456789" w/o all chars
mainChars_list = list(mainChars)

password = pyautogui.password("INSERT PASSWORD : ")

guessing_pw = ""

while(guessing_pw != password): 
    guessing_pw = random.choices(mainChars, k=len(password))

print("<====================="+ str(guessing_pw)+ "=====================>")


    if(guessing_pw == list(password)):
        print("We've guessed your password : "+ "".join(guessing_pw))
        break




