from tkinter import *

import random
from faker import Faker
from pynput.mouse import Button as MouseButton, Controller
m = Controller()

from pynput.keyboard import Key, Controller as KeyboardController
k = KeyboardController()

import time
import csv

'''
pip install faker
pip install pynput
'''

root = Tk()  

ran = 0
safety = 0
root.title("Krispe_Kreme")



def details():
  global safety
  if(safety % 2 == 0):
    time.sleep(2)
    k.press(Key.ctrl)
    k.press('t')
    k.release(Key.ctrl)
    k.release('t')
    k.type("https://www.krispykreme.com/account/create-account")
    k.press(Key.enter)
    k.release(Key.enter)
    time.sleep(2)
    for tab_to_start in range(3):
        k.press(Key.tab)
        k.release(Key.tab)

    k.type('test')
    safety +=1
    print("safety updated")
    safety_text.configure(text = "Ready for Post-Captcha")

  else:
    print("Run post-captcha, Post-Captcha has not been run yet")
  
  

def barcode_retriever():
  global safety
  if(safety % 2 == 1):
    #code for barcode
    safety +=1
    print("safety updated")  
    safety_text.configure(text = "Ready for Pre-Captcha")
    ran += 1
    counter0.configure(text = ran)
    
  else:
    print("Run pre-captcha, Pre-Captcha has not been run yet")

    
  print("Done")
pre_captcha = Button(root, width = 10, height=5, text = "Pre-captcha",font = "sans 20", command =lambda: details(), background = "white")
pre_captcha.grid(row = 1, column = 1)

post_captcha = Button(root, width = 10, height=5, text = "Post-captcha",font = "sans 20", command =lambda: barcode_retriever(), background = "white")
post_captcha.grid(row = 2, column = 1)


counter0 = Label(root, text = ran, font = "sans 20", foreground = "red", background = "white")
counter0.grid(row = 2, column = 2)

safety_text = Label(root, text = "Ready for Pre-Captcha", font = "sans 20", foreground = "red", background = "white")
safety_text.grid(row = 1, column = 2)

mainloop()