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

email = input("What is your email?")
email = email + "+"

month = 1
day = 1

root = Tk() 
fake = Faker('en_US')
ran = 0
safety = 0
root.title("Krispe_Kreme")



fname = fake.first_name()
lname = fake.last_name()
postc = fake.postcode()
phone = str(fake.phone_number())
password = fake.password()

def tab():
    k.press(Key.tab)
    k.release(Key.tab)
def details_input():
  global safety, fname, lname, postc, phone, password
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
        tab()
    k.type(fname)
    tab()
    k.type(lname)
    tab()
    k.press(Key.space)
    k.release(Key.space)
    for month_input in range (month+1):
        k.press(Key.down)
        k.release(Key.down)
    tab()
    tab()
    k.press(Key.space)
    k.release(Key.space)
    for day_input in range (month+1):
        k.press(Key.down)
        k.release(Key.down)
    tab()
    tab()
    k.type(postc)
    tab()
    k.type(phone[:2])
    tab()
    k.type(phone[3:5])
    tab()
    k.type(phone[6:9])
    tab()
    k.type(email,(month, day ))
    safety +=1
    print("safety updated")
    safety_text.configure(text = "Ready for Post-Captcha")

  else:
    print("Run post-captcha, Post-Captcha has not been run yet")
  
  

def barcode_retriever():
  global safety, fname, lname, postc, phone, password
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
pre_captcha = Button(root, width = 10, height=5, text = "Pre-captcha",font = "sans 20", command =lambda: details_input(), background = "white")
pre_captcha.grid(row = 1, column = 1)

post_captcha = Button(root, width = 10, height=5, text = "Post-captcha",font = "sans 20", command =lambda: barcode_retriever(), background = "white")
post_captcha.grid(row = 2, column = 1)


counter0 = Label(root, text = ran, font = "sans 20", foreground = "red", background = "white")
counter0.grid(row = 2, column = 2)

safety_text = Label(root, text = "Ready for Pre-Captcha", font = "sans 20", foreground = "red", background = "white")
safety_text.grid(row = 1, column = 2)

mainloop()
