import tkinter
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "yesitsaname"
)
cursor = conn.cursor(buffered=True)  #created cursor to handle all sql queries
# check if database available. if not, then create
try:
    cursor.execute(" USE Registration ")
except :
    cursor.execute("CREATE DATABASE Registration")

try:
    cursor.execute("DESCRIBE Users")
except:
    cursor.execute("CREATE TABLE Users (Id int primary key auto_increment, Name varchar(20), Age int(10), Gender varchar(5), Email varchar(30), Mobile varchar(13)) ")


def Registration() :
    cursor.execute(f"insert into Users (Name, Age, Gender, Email,Mobile ) values('{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}')")
    conn.commit()

win = tkinter.Tk() # created window
win.geometry("500x500")
win.title("Registration portal")
# labels to display text
l1 = tkinter.Label(win, text = "Person Details ")
l2 = tkinter.Label(win, text = "Name")
l3 = tkinter.Label(win, text = "Age")
l4 = tkinter.Label(win, text = "Gender")
l5 = tkinter.Label(win, text = "Email")
l6 = tkinter.Label(win, text = "Mob No")    # labels not visible now

l1.grid(row =1 , column=2 )
l2.grid(row =2 , column=2 )
l3.grid(row =3 , column=2 )
l4.grid(row =4 , column=2 )
l5.grid(row =5 , column=2 )
l6.grid(row =6 , column=2 )

# entry boxes to enter data
#e1 = tkinter.Entry(win)
e2 = tkinter.Entry(win)
e3 = tkinter.Entry(win)
e4 = tkinter.Entry(win)
e5 = tkinter.Entry(win)
e6 = tkinter.Entry(win)
# now place the entry boxes.
#e1.grid(row =1 , column=4 )
e2.grid(row =2 , column=4 )
e3.grid(row =3 , column=4 )
e4.grid(row =4 , column=4 )
e5.grid(row =5 , column=4 )
e6.grid(row =6 , column=4 )

B = tkinter.Button(win, text =" Submit Here", command = Registration)
B.grid(row = 7, column= 3)

win.mainloop() # keeps the window open