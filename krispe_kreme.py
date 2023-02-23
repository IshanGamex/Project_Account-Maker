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


'''
pip install faker
pip install pynput
'''
root = tk.Tk()

# set the window size
root.geometry("200x200")

email = tk.simpledialog.askstring("Krispe Kreme", "What is your email?(type out the part before the @ sign)")
tk.messagebox.showinfo('Hello', 'Hello, {}'.format(email))

# start the main event loop
root.mainloop()

ifconsoleshow = False
# console?
import tkinter as tk
from tkinter import messagebox

# Create the main window

root = tk.Tk()
window_width = 500
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))


# Set the window title
root.title("Select an option")

# Define a function to handle Option One

question_label = tk.Label(root, text="Do you want to see the console outputs?")
question_label.pack(side=tk.TOP, pady=10)

def handle_option_one():
    messagebox.showinfo("Yes", "You selected Yes")
    ifconsoleshow = True

# Define a function to handle Option Two
def handle_option_two():
    messagebox.showinfo("No", "You selected No")
    ifconsoleshow = False
# Create the two buttons
button_one = tk.Button(root, text="Yes", command=handle_option_one, width=10, height=3, bd=0, bg="green", fg="white", activebackground="lightgreen", activeforeground="white", relief="ridge", cursor="hand2")
button_two = tk.Button(root, text="No", command=handle_option_two, width=10, height=3, bd=0, bg="red", fg="white", activebackground="tomato", activeforeground="white", relief="ridge", cursor="hand2")
# Pack the buttons into the window
button_one.pack(side=tk.LEFT, padx=10, pady=10)
button_two.pack(side=tk.RIGHT, padx=10, pady=10)

# Run the main event loop
root.mainloop()

#

email = email + "+"
email_date = ""
month = 1
day = 1
prerun = False
root = tk.Tk() 
fake = Faker('en_US')
ran = 0
safety = 0
root.title("Krispe_Kreme")




def tab():
    k.press(Key.tab)
    t.sleep(0.01)
    k.release(Key.tab)
    t.sleep(0.01)
def details_input():
  global safety, prerun
  if(prerun == False):
    t.sleep(1)
    k.press(Key.ctrl)
    k.press('t')
    k.release(Key.ctrl)
    k.release('t')
    t.sleep(1)
    prerun +=1
    print("Prerun set to true")
  elif(prerun == True):
    t.sleep(1)
    k.press(Key.ctrl)
    k.press('w')
    k.release(Key.ctrl)
    k.release('w')
    t.sleep(1)
  if(safety % 2 == 0):
    #DETAILS
    fname = fake.first_name()
    lname = fake.last_name()
    postc = fake.postcode()
    phone = str(fake.phone_number())
    password = fake.password()


    header = ['email', 'password', 'day', 'month']

    with open('LoginDetails.csv', 'a') as file:
      writer = csv.writer(file)
    
      if file.tell() == 0:
        writer.writerow(header)
    
      writer.writerow([email + "(" + str(day) + "/" + str(month) + ")", password , day , month])

    print("Data generated and added to the CSV file successfully!")

    #INPUTS
    t.sleep(2)
    k.press(Key.ctrl)
    k.press('t')
    k.release(Key.ctrl)
    k.release('t')
    k.type("https://www.krispykreme.com/account/create-account")
    k.press(Key.enter)
    k.release(Key.enter)
    t.sleep(2)
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
    k.type('740')
    tab()
    numbers1 = [str(random.randint(0, 9)) for _ in range(3)]
    number_string1 = "".join(numbers1)
    k.type(number_string1)
    tab()
    numbers2 = [str(random.randint(0, 9)) for _ in range(4)]
    number_string2 = "".join(numbers2)
    k.type(number_string2)
    tab()
    safety +=1
    print("safety updated")
    safety_text.configure(text = "Ready for Post-Captcha")

  else:
    print("Run post-captcha, Post-Captcha has not been run yet")
  

counter0 = tk.Label(root, text = ran, font = "sans 20", foreground = "red", background = "white")
counter0.grid(row = 2, column = 2)


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
pre_captcha = tk.Button(root, width = 10, height=5, text = "Pre-captcha",font = "sans 20", command =lambda: details_input(), background = "white")
pre_captcha.grid(row = 1, column = 1)

post_captcha = tk.Button(root, width = 10, height=5, text = "Post-captcha",font = "sans 20", command =lambda: barcode_retriever(), background = "white")
post_captcha.grid(row = 2, column = 1)



safety_text = tk.Label(root, text = "Ready for Pre-Captcha", font = "sans 20", foreground = "red", background = "white")
safety_text.grid(row = 1, column = 2)

if ifconsoleshow :
  class ConsoleOutput(tk.Frame):
      def __init__(self, parent):
          tk.Frame.__init__(self, parent)
          self.text = tk.Text(self, wrap="word", state="disabled")
          self.text.pack(side="bottom", fill="both", expand=True)
          sys.stdout = self

      def write(self, message):
          self.text.configure(state="normal")
          self.text.insert("end", message)
          self.text.configure(state="disabled")

  root = tk.Tk()
  root.title("Krispe_Kreme - Console Outputs")

  console = ConsoleOutput(root)
  console.pack(side="bottom", fill="both", expand=True)

  root.mainloop()
tk.mainloop()
