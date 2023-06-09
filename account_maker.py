import tkinter as tk
from tkinter.simpledialog import askstring
import tkinter.messagebox as messagebox

import random
from faker import Faker
from pynput.mouse import Button as MouseButton, Controller
m = Controller()

from pynput.keyboard import Key, Controller as KeyboardController
k = KeyboardController()

import time as t

import csv

import sys

import datetime

'''
pip install faker
pip install pynput
'''

def intro():
  print("               AAA                                                                                                                     tttt          ")
  print("              A:::A                                                                                                                 ttt:::t          ")
  print("             A:::::A                                                                                                                t:::::t          ")
  print("            A:::::::A                                                                                                               t:::::t          ")
  print("           A:::::::::A             cccccccccccccccc     cccccccccccccccc    ooooooooooo    uuuuuu    uuuuuu nnnn  nnnnnnnn     ttttttt:::::ttttttt    ")
  print("          A:::::A:::::A          cc:::::::::::::::c   cc:::::::::::::::c  oo:::::::::::oo  u::::u    u::::u n:::nn::::::::nn   t:::::::::::::::::t    ")
  print("         A:::::A A:::::A        c:::::::::::::::::c  c:::::::::::::::::c o:::::::::::::::o u::::u    u::::u n::::::::::::::nn  t:::::::::::::::::t    ")
  print("        A:::::A   A:::::A      c:::::::cccccc:::::c c:::::::cccccc:::::c o:::::ooooo:::::o u::::u    u::::u nn:::::::::::::::n tttttt:::::::tttttt    ")
  print("       A:::::A     A:::::A     c::::::c     ccccccc c::::::c     ccccccc o::::o     o::::o u::::u    u::::u   n:::::nnnn:::::n       t:::::t          ")
  print("      A:::::AAAAAAAAA:::::A    c:::::c              c:::::c              o::::o     o::::o u::::u    u::::u   n::::n    n::::n       t:::::t          ")
  print("     A:::::::::::::::::::::A   c:::::c              c:::::c              o::::o     o::::o u::::u    u::::u   n::::n    n::::n       t:::::t          ")
  print("    A:::::AAAAAAAAAAAAA:::::A  c::::::c     ccccccc c::::::c     ccccccc o::::o     o::::o u:::::uuuu:::::u   n::::n    n::::n       t:::::t    tttttt")
  print("   A:::::A             A:::::A c:::::::cccccc:::::c c:::::::cccccc:::::c o:::::ooooo:::::o u:::::::::::::::uu n::::n    n::::n       t::::::tttt:::::t")
  print("  A:::::A               A:::::A c:::::::::::::::::c  c:::::::::::::::::c o:::::::::::::::o  u:::::::::::::::u n::::n    n::::n       tt::::::::::::::t")
  print(" A:::::A                 A:::::A cc:::::::::::::::c   cc:::::::::::::::c  oo:::::::::::oo    uu::::::::uu:::u n::::n    n::::n         tt:::::::::::tt")
  print("AAAAAAA                   AAAAAAA  cccccccccccccccc     cccccccccccccccc    ooooooooooo        uuuuuuuu  uuuu nnnnnn    nnnnnn           ttttttttttt  ")
  print()
  print()
  space = "                                                                                                                                                        "
  print(space + "MMMMMMMM               MMMMMMMM                    kkkkkkkk                                                ")
  print(space + "M:::::::M             M:::::::M                    k::::::k                                                ")
  print(space + "M::::::::M           M::::::::M                    k::::::k                                                ")
  print(space + "M:::::::::M         M:::::::::M                    k::::::k                                                ")
  print(space + "M::::::::::M       M::::::::::M   aaaaaaaaaaaaa    k:::::k    kkkkkkk  eeeeeeeeeeee       rrrrr   rrrrrrrrr   ")
  print(space + "M:::::::::::M     M:::::::::::M   a::::::::::::a   k:::::k   k:::::k ee::::::::::::ee     r::::rrr:::::::::r  ")
  print(space + "M:::::::M::::M   M::::M:::::::M   aaaaaaaaa:::::a  k:::::k  k:::::k e::::::eeeee:::::ee   r:::::::::::::::::r ")
  print(space + "M::::::M M::::M M::::M M::::::M            a::::a  k:::::k k:::::k e::::::e     e:::::e   rr::::::rrrrr::::::r")
  print(space + "M::::::M  M::::M::::M  M::::::M     aaaaaaa:::::a  k::::::k:::::k  e:::::::eeeee::::::e   r:::::r     r:::::r")
  print(space + "M::::::M   M:::::::M   M::::::M   aa::::::::::::a  k:::::::::::k   e:::::::::::::::::e    r:::::r     rrrrrrr")
  print(space + "M::::::M    M:::::M    M::::::M  a::::aaaa::::::a  k:::::::::::k   e::::::eeeeeeeeeee     r:::::r            ")
  print(space + "M::::::M     MMMMM     M::::::M a::::a    a:::::a  k::::::k:::::k  e:::::::e              r:::::r            ")
  print(space + "M::::::M               M::::::M a::::a    a:::::a  k::::::k k:::::k e::::::::e            r:::::r            ")
  print(space + "M::::::M               M::::::M a:::::aaaa::::::a  k::::::k  k:::::k e::::::::eeeeeeee    r:::::r            ")
  print(space + "M::::::M               M::::::M  a::::::::::aa:::a k::::::k   k:::::k ee:::::::::::::e    r:::::r            ")
  print(space + "MMMMMMMM               MMMMMMMM   aaaaaaaaaa  aaaa kkkkkkkk    kkkkkkk  eeeeeeeeeeeeee    rrrrrrr            ")

# intro()



# root = tk.Tk()

# set the window size
# root.geometry("200x200")

# emailbeforeat = tk.simpledialog.askstring("Account Maker", "What is your email?(Type out the part before the @ sign!!!)")
emailbeforeat = "ishanpatra9alt"
emailafterat_counter = 1

emailafterat = "gmail.com"
# emailafterat = tk.simpledialog.askstring("Account Maker", "What is the last part of your email?(Type out the part after the @ sign, dont include the @ sign!!!)")

# if "@" in emailafterat:
#   if (emailafterat_counter == 3):
#     emailafterat = tk.simpledialog.askstring("Account Maker", "Third times a charm you got this. What is the last part of your email?(Type out the part after the @ sign, dont include the @ sign)")
#   elif(emailafterat_counter != 3 and emailafterat != 1):
#     while(emailafterat_counter != 3 and emailafterat != 1):
#       emailafterat = tk.simpledialog.askstring("Account Maker", "I said don't add a @ sign. What is the last part of your email?")

emailafterat = "@" + emailafterat
emailbeforeat += "+"

now = datetime.datetime.now()

email_date = ""
month = 6
day = 5
root = tk.Tk() 
fake = Faker('en_US')
safety = 0
root.title("Account Maker")




def tab():
    k.press(Key.tab)
    t.sleep(0.01)
    k.release(Key.tab)
    t.sleep(0.01)



def krespe_kreme():
  global month, day
  t.sleep(1)
  #DETAILS
  fname = fake.first_name()
  print(fname)
  lname = fake.last_name()
  print(lname)
  postc = fake.postcode()
  print(postc)
  password = fake.password()
  print(password)
  inp_email = emailbeforeat + "(" + str(day) + "/" + str(month) + ")" + emailafterat
  
  #INPUTS
  t.sleep(2)
  k.press(Key.ctrl)
  k.press('t')
  k.release(Key.ctrl)
  k.release('t')
  t.sleep(1)
  k.type("https://www.krispykreme.com/account/create-account")
  k.press(Key.enter)
  k.release(Key.enter)
  t.sleep(3)
  for tab_to_start in range(3):
      tab()
  k.type(fname) #FIRST NAME
  t.sleep(0.1)
  tab()
  k.type(lname) #LAST NAME
  t.sleep(0.1)
  tab()
  k.press(Key.space)
  k.release(Key.space)
  for month_input in range (month): #MONTH INPUT
      k.press(Key.down)
      k.release(Key.down)
  t.sleep(0.1)
  tab()
  tab()
  k.press(Key.space)
  k.release(Key.space)
  for day_input in range (day): # DAY INPUT
      k.press(Key.down)
      k.release(Key.down)
  t.sleep(0.1)
  tab()
  tab()
  k.type(postc) #POSTAL CODE
  t.sleep(0.1)
  tab()
  k.type('740') #PHONE NUMBER P1
  # tab()
  numbers1 = [str(random.randint(0, 9)) for _ in range(3)]
  number_string1 = "".join(numbers1)
  k.type(number_string1) #PHONE NUMBER P2
  t.sleep(0.1)
  # tab()
  numbers2 = [str(random.randint(0, 9)) for _ in range(4)]
  number_string2 = "".join(numbers2)
  k.type(number_string2) #PHONE NUMBER P3
  t.sleep(0.1)
  tab()
  if(month == 1):
     k.type(emailbeforeat + "Jan" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 2):
     k.type(emailbeforeat + "Feb" + "/" + str(day)  + emailafterat) #EMAIL
  elif(month == 3):
     k.type(emailbeforeat + "Mar" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 4):
     k.type(emailbeforeat + "Apr" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 5):
     k.type(emailbeforeat + "May" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 6):
     k.type(emailbeforeat + "June" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 7):
     k.type(emailbeforeat + "July" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 8):
     k.type(emailbeforeat + "Aug" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 9):
     k.type(emailbeforeat + "Sept" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 10):
     k.type(emailbeforeat + "Oct" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 11):
     k.type(emailbeforeat + "Nov" + "/" + str(day) + emailafterat) #EMAIL
  elif(month == 12):
     k.type(emailbeforeat + "Dec" + "/" + str(day) + emailafterat) #EMAIL
  # k.type(emailbeforeat + str(month) + "/" + str(day) + emailafterat) #EMAIL
  t.sleep(0.1)
  tab()
  k.type(password) #PASSWORD P1
  t.sleep(0.1)
  tab()
  tab()
  k.type(password) #PASSWORD P2
  t.sleep(0.1)
  tab()
  tab()
  k.press(Key.space) #TERMS OF USE AND PRIVACY POLICY
  k.release(Key.space)
  t.sleep(0.1)
  tab()
  tab()
  t.sleep(0.5)
  k.press(Key.space) #I aM nOt A rObOt *proceedes to be a bot making the account
  k.release(Key.space)
  t.sleep(3)
  tab()
  tab()
  tab()
  k.press(Key.space) #BY PASS THE TERRIBLE SECURITY AND SIGN UP
  k.release(Key.space)
  day +=1
  if (day == 31):
    day = 1
    month+=1




root = tk.Tk()
root.title("Buttons")

krespekreme = tk.Button(root, width=10, height=5, text="Krespe Kreme", font="sans 20", command=krespe_kreme, background="white")
krespekreme.grid(row=1, column=1)


root.mainloop()
