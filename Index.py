from tkinter import *
import tkinter
from tkinter import messagebox

log_win = Tk()
log_win.configure(background='#ef9a9a')
log_win.geometry("400x400")
log_win.title("COFEE SHOP")
log_win.iconbitmap('images\profile.ico')
log_frame = Frame(log_win,width=250,height=220,bg="#ef9a9a",borderwidth=5,relief = RIDGE).place(x=80,y=100)
img = PhotoImage(file="images\logIn_logo.png")
Label(log_win,image=img,borderwidth=0).place(x=140,y=10)
img1 = PhotoImage(file="images\logIn_coffee.png")
Label(log_win,image=img1,borderwidth=0).place(x=280,y=270)

global user,pwd
user = StringVar()
pwd = StringVar()
Label(log_frame,text="Username",font="appHighLightFont 8",bg="#ef9a9a").place(x=100,y=150)
Entry(log_frame,width=15,textvariable=user).place(x=170,y=150)
Label(log_frame,text="Password",font="appHighLightFont 8",bg="#ef9a9a").place(x=101,y=200)
Entry(log_frame,width=15,textvariable=pwd,show='*').place(x=171,y=200)
Label(log_win,text="Enter Credentials",font="appHighLightFont 8",bg="#ef9a9a").place(x=90,y=92)


#-----------------------------------------------------------------------------------------------------------------
def log():
    import mysql.connector
    try:
        con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shop")
        cur = con.cursor()
        u=user.get()
        s1=pwd.get()
        s='select password,id from login where username="'+u+'"'
        cur.execute(s)          
        pw=cur.fetchone()
        
        if pw==None:
            messagebox.showinfo("","User Not Found")
        if pw[0]!=s1:
            messagebox.showinfo("","Wrong Password!!!!")
        else:
            log_win.destroy()
            import FinalGUI
            
    except mysql.connector.DatabaseError as err:
        if con!=None:
            print(err)
    finally:        
        con.close()
        cur.close()
#--------------------------------------------------------------------------------------------------------------------        
Button(log_win,text="LogIn",font="appHighLightFont 8 bold ",command=log,padx=15,pady=5).place(x=170,y=250)

log_win.mainloop()

