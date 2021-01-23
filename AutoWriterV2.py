import pyautogui
import time
user_input = input("Enter a word you would like to spam: ")
user_input1 = input("How many times would you like the word to be spammed: ")
user_input2 = input("After how many seconds should the spam be ececuted: ")
def files():
    l = open("x.txt","w")
    l.write(user_input)
    l.close()
def click():
    time.sleep(float(user_input2))
    for i in range(int(user_input1)):
        pyautogui.write(user_input)
        pyautogui.press("enter")
files()
click()
