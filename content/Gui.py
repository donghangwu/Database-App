from tkinter import*
from PIL import ImageTk,Image
import sqlite3
top = Tk()
top.title('database app')
top.config(bg='#3399FF')
background_im = ImageTk.PhotoImage(Image.open("image/background.png"))  # PIL solution

backgroundLabel = Label(top,image=background_im)
# create input boxes
firstName = Entry(top,width=39,borderwidth=5,bg='#73C5FC')
firstName.grid(row=0,column=1,padx=30,pady=(10,0),ipady = 5)

lastName = Entry(top,width=39,borderwidth=5,bg='#73C5FC')
lastName.grid(row=1,column=1,padx=30,ipady = 5)

address = Entry(top,width=39,borderwidth=5,bg='#73C5FC')
address.grid(row=2,column=1,padx=30,ipady = 5)

city = Entry(top,width=39,borderwidth=5,bg='#73C5FC')
city.grid(row=3,column=1,padx=30,ipady = 5)

state = Entry(top,width=39,borderwidth=5,bg='#73C5FC')
state.grid(row=4,column=1,padx=30,ipady = 5)

zipcode = Entry(top,width=39,borderwidth=5,bg='#73C5FC')
zipcode.grid(row=5,column=1,padx=30,ipady = 5)
#create text label
firstName_label = Label(top,text='First Name :',bg='#3399ff',font='bold')
firstName_label.grid(row=0,column=0,padx=(10,0))

lastName_label = Label(top,text='Last Name :',bg='#3399ff',font='bold')
lastName_label.grid(row=1,column=0,padx=(10,0))

address_label = Label(top,text='Address :',bg='#3399ff',font='bold')
address_label.grid(row=2,column=0,padx=(10,0))

city_label = Label(top,text='City :',bg='#3399ff',font='bold')
city_label.grid(row=3,column=0,padx=(10,0))

state_label = Label(top,text='State :',bg='#3399ff',font='bold')
state_label.grid(row=4,column=0,padx=(10,0))

zipcode_label = Label(top,text='Zip Code :',bg='#3399ff',font='bold')
zipcode_label.grid(row=5,column=0,padx=(10,0))


