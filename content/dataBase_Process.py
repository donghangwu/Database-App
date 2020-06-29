from tkinter import*
from PIL import ImageTk,Image
import sqlite3
from Gui import*




'''
#create a table
cur.execute(""" CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text, 
            zipcode integer
            )""")
'''
def submit():
#connect to a database or create one
    con = sqlite3.connect('my_data.db')
#create a cursor
    cur = con.cursor()
   

#excute command
    cur.execute("INSERT INTO addresses VALUES (:fname,:lname,:address,:city,:state,:zipcode)",
                {
                    'fname':firstName.get(),
                    'lname':lastName.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zipcode':zipcode.get()
                }
                
                )
#commit chnages
    con.commit()

#close connection
    con.close()

    firstName.delete(0,END)
    lastName.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
#connect to a database or create one
    con = sqlite3.connect('my_data.db')
#create a cursor
    cur = con.cursor()
#query the data  oid is the primary key for each record, sqlite3 generated it for us
    cur.execute("SELECT *,oid FROM addresses")
    alldata = cur.fetchall()
    #cur.fetmany(50) fetch 50 records
    display=''
    counter=1
    for records in alldata:
        display+=str(counter)
        display+='. '
        counter+=1
        for each in records:
            display += str(each)+' '
        display+='\n'
    showRecord = Toplevel()
    showRecord.geometry('300x200')
    showRecord.title('records in database')
    dataLabel= Label(showRecord,text=display).pack()

#commit chnages
    con.commit()

#close connection
    con.close()




#delete a record
def select():
    global oidEntry   
    select_window= Toplevel()
    select_window.title('Operating on A Record')
    select_window.config(bg='#3399FF')
    select_window.geometry('400x300')
    oidlabel = Label(select_window,text='enter ID number',font=1,bg='#3399FF').pack(padx=10,pady=10)
    oidEntry = Entry(select_window,borderwidth=5)
    oidEntry.pack(pady=(10),ipady=5,ipadx=10)
    deleteRocord_btn = Button(select_window,text='Delete Record',command=deleteRecord,borderwidth=0,image=delete_im,bg='#3399FF').pack(pady=(5,20))
    update_button = Button(select_window,text='update Record',command=updateRecord,borderwidth=0,image=update_im,bg='#3399FF').pack(pady=(5,20))

def deleteRecord():
    #connect to a database or create one
        con = sqlite3.connect('my_data.db')
    #create a cursor
        global oidEntry
        cur = con.cursor() 
        target=''
        target=oidEntry.get()
        (oidEntry).delete(0,END)
        cur.execute("DELETE from addresses where oid = "+target)
    #commit chnages
        con.commit()

    #close connection
        con.close()   

#update a record
def updateRecord():
    global update_window
    update_window = Toplevel()
    update_window.config(bg='#3399FF')
    global firstName_update
    global lastName_update
    global address_update
    global city_update
    global state_update
    global zipcode_update
    # create input boxes
    firstName_update = Entry(update_window,width=39,borderwidth=5,bg='#73C5FC')
    firstName_update.grid(row=0,column=1,padx=30,pady=(10,0),ipady = 5)

    lastName_update = Entry(update_window,width=39,borderwidth=5,bg='#73C5FC')
    lastName_update.grid(row=1,column=1,padx=30,ipady = 5)

    address_update = Entry(update_window,width=39,borderwidth=5,bg='#73C5FC')
    address_update.grid(row=2,column=1,padx=30,ipady = 5)

    city_update = Entry(update_window,width=39,borderwidth=5,bg='#73C5FC')
    city_update.grid(row=3,column=1,padx=30,ipady = 5)

    state_update = Entry(update_window,width=39,borderwidth=5,bg='#73C5FC')
    state_update.grid(row=4,column=1,padx=30,ipady = 5)

    zipcode_update = Entry(update_window,width=39,borderwidth=5,bg='#73C5FC')
    zipcode_update.grid(row=5,column=1,padx=30,ipady = 5)
    #create text label
    firstName_label_update = Label(update_window,text='First Name:',bg='#3399FF')
    firstName_label_update.grid(row=0,column=0)

    lastName_label_update = Label(update_window,text='Last Name:',bg='#3399FF')
    lastName_label_update.grid(row=1,column=0)

    address_label_update = Label(update_window,text='Address:',bg='#3399FF')
    address_label_update.grid(row=2,column=0)

    city_label_update = Label(update_window,text='City:',bg='#3399FF')
    city_label_update.grid(row=3,column=0)

    state_label_update = Label(update_window,text='State:',bg='#3399FF')
    state_label_update.grid(row=4,column=0)

    zipcode_label_update = Label(update_window,text='Zip Code:',bg='#3399FF')
    zipcode_label_update.grid(row=5,column=0)

    #create submit button
    submit_button_update = Button(update_window,text='Submite Changes',command = update,image=submit_im,bg='#3399FF',borderwidth=0)
    submit_button_update.grid(row=6,column=0,columnspan=2,pady=10,ipady=5)
    global oidEntry

    #connect to a database or create one
    con = sqlite3.connect('my_data.db')
    #create a cursor
    cur = con.cursor() 
    cur.execute("SELECT * FROM addresses where oid = "+oidEntry.get())
    records = cur.fetchall()

    #loops each elements in the result and modify them ex:name,address,city,state...
    for record in records:
        firstName_update.insert(0,record[0])
        lastName_update.insert(0,record[1])
        address_update.insert(0,record[2])
        city_update.insert(0,record[3])
        state_update.insert(0,record[4])
        zipcode_update.insert(0,record[5])

   # cur.execute("DELETE from addresses where oid = "+target)
    #commit chnages
    con.commit()

    #close connection
    con.close()   
def update():
 #connect to a database or create one
    con = sqlite3.connect('my_data.db')
    #create a cursor
    cur = con.cursor() 
    cur.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :add,
                city = :city_update,
                state = :state_update,
                zipcode = :zipcode_update
                
                WHERE oid = :oid""",
                {'first':firstName_update.get(),
                 'last':lastName_update.get(),
                 'add':address_update.get(),
                 'city_update':city_update.get(),
                 'state_update':state_update.get(),
                 'zipcode_update':zipcode_update.get(),
                 'oid':oidEntry.get()
                }
    
                )
    (oidEntry).delete(0,END)

    #commit chnages
    con.commit()
    first=firstName_update.get()
    second =lastName_update.get()
    update_window.destroy()
    endingInfo = Toplevel()
    endingInfo.geometry('500x150')
    endingLabel = Label(endingInfo,text=first+' '+second+'\'s info has been successfully updated!',font=6)
    endingLabel.pack(pady=(30,0))
    endingButton = Button(endingInfo,text='OK,',command = endingInfo.destroy,image=great_im,borderwidth=0)
    endingButton.pack(pady=(30,0))
    #close connection
    con.close()   


query_im = ImageTk.PhotoImage(Image.open("image/querybutton.png"))  # PIL solution
submit_im = ImageTk.PhotoImage(Image.open("image/submitbutton.png"))  # PIL solution
edit_im = ImageTk.PhotoImage(Image.open("image/editbutton.png"))  # PIL solution
delete_im = ImageTk.PhotoImage(Image.open("image/deletebutton.png"))  # PIL solution
update_im = ImageTk.PhotoImage(Image.open("image/updatebutton.png"))  # PIL solution
great_im = ImageTk.PhotoImage(Image.open("image/greatbutton.png"))  # PIL solution

#create submit button
submit_button = Button(top,command = submit,borderwidth=0,image=submit_im,bg='#3399ff')
submit_button.grid(row=6,column=0,columnspan=2,pady=10)
#create query button
query_button = Button(top,text='Query Records',borderwidth=0,command = query,image=query_im,bg='#3399ff')
query_button.grid(row=7,column=0,columnspan=2)
#delete_button
select_button = Button(top,text='Edit A Record',borderwidth=0,command=select,image=edit_im,bg='#3399ff')
select_button.grid(row = 8,column=0,columnspan=2,pady=25)
