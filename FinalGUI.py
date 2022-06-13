import tkinter
from tkinter import *
from tkinter import messagebox
import random,mysql.connector
import datetime
import time

main_win = Tk()
main_win.geometry("2000x1000")
main_win.iconbitmap('images\profile.ico')
main_win.title("COFFEE SHOP")
localtime = time.localtime()
top_frame = Frame(main_win, borderwidth=6,width=2000,height=150,bg="#0de6ed").place(x=0,y=0)
left_frame = Frame(main_win, borderwidth=6,width=150,height=850,bg="white").place(x=0,y=150)
right_frame = Canvas(main_win, borderwidth=6,width=550,height=850,bg="#fffee7").place(x=1365,y=150)
mid_frame = Canvas(main_win, borderwidth=6,width=1200,height=850,bg="#fffee7").place(x=150,y=150)

prof_frame =Frame(left_frame,width=150,height=170,relief=RIDGE,borderwidth=10,bg="white").place(x=0,y=800)


global total_display
total_dis=Label(right_frame,text="",padx=5,pady=5,bg="#fffee7",font="calibri 16 bold")
total_dis.place(x=1687,y=781)
    
Label(prof_frame,text="TIME & DATE",font=" Arial 9 bold",bg="white").place(x=20,y=815)
Label(prof_frame,text=datetime.date.today(),font=" Arial 9 bold",bg="white").place(x=20,y=860)


time1 = ''
clock = Label(main_win, font=('Arial', 9, 'bold'),bg="white")
clock.place(x=20,y=890)
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()

img = PhotoImage(file="images\menu.png")
Button(top_frame,image=img,bg="#0de6ed",relief=FLAT).place(x=10,y=30)

img2 = PhotoImage(file="images\logo.png")
Label(top_frame,image=img2,bg="#0de6ed",relief=FLAT).place(x=800,y=0)

img3 = PhotoImage(file="images\cartoon1.png")
Label(top_frame,image=img3,bg="#0de6ed").place(x=1700,y=0)


cf_s=['Mint Chocolate 25/-',"Espresso 30/-",'Americano 20/-','Cafe Latte 45/-','Cappuccino 50/-','Cafe Mocha 55/-','Caramel 40/-','Vanilla Latte 35/-']
cofe_var=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        cofe_var[i]=IntVar()
mc=[0,0,0,0,0,0,0,0,0,0,0]
cofe_txt=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        cofe_txt[i]=StringVar()


snk_s=['Vada Pav 20/-','Samosa 15/-','Sandwich 20/-','Burger 40/-','Pizza 80/-','Pasta 60/-','Manchurian 80/-','Pav Bhaji 40/-']   
snk_var=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        snk_var[i]=IntVar()
ms=[0,0,0,0,0,0,0,0,0,0,0]
snk_txt=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        snk_txt[i]=StringVar()


ice_s=['Mango 35/-','Mava 20/-','Coco 25/-','Kiwi 35/-','Anjeer 40/-','Rajbhog 20/-','Guava 30/-','Dry Fruit 45/-']
ice_var=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        ice_var[i]=IntVar()
mi=[0,0,0,0,0,0,0,0,0,0,0]
ice_txt=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        ice_txt[i]=StringVar()


cold_s=['Iced Coffee 20/-','Iced Tea 20/-','Mango Slice 25/-','Mastani 40/-','MilkShake 45/-','Cola 30/-','Sprite 40/-','Mirinda 30/-']
cold_var=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        cold_var[i]=IntVar()
md=[0,0,0,0,0,0,0,0,0,0,0]
cold_txt=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        cold_txt[i]=StringVar()


desrt_s=['Cake 50/-','Cup Cake 40/-','Pastries 30/-','Doughnut 25/-','Pudding 20/-','Choco Balls 45/-','Biscuit 20/-','Charlotte 40/-']
desrt_var=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        desrt_var[i]=IntVar()
mds=[0,0,0,0,0,0,0,0,0,0,0]
desrt_txt=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,8):
        desrt_txt[i]=StringVar()
        

            


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def des_cof():
    global total

    b1.config(bg="#0de6ed")
    b2.config(bg='white')
    b3.config(bg='white')
    b4.config(bg='white')
    b5.config(bg='white')

    l=[0,0,0,0,0,0,0,0,0,0,0]
    
    l[0] = Checkbutton(mid_frame, text="Mint Chocolate\t\t 25/-   \tQty",variable=cofe_var[0], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[0].place(x=300,y=200)
    mc[0]=Entry(mid_frame,width=5,textvariable=cofe_txt[0])
    mc[0].place(x=900,y=215)
    mc[0].config(state='disabled')

    l[1] = Checkbutton(mid_frame, text="Espresso\t\t\t 30/-   \tQty",variable=cofe_var[1], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[1].place(x=300,y=300)
    mc[1]=Entry(mid_frame,textvariable=cofe_txt[1],width=5)
    mc[1].place(x=900,y=315)
    mc[1].config(state='disabled')
    
    l[2] = Checkbutton(mid_frame, text="Americano\t\t 20/-   \tQty",variable=cofe_var[2], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[2].place(x=300,y=400)
    mc[2]=Entry(mid_frame,textvariable=cofe_txt[2],width=5)
    mc[2].place(x=900,y=415)
    mc[2].config(state='disabled')
    
    l[3] = Checkbutton(mid_frame, text="Cafe Latte\t\t 45/-   \tQty",variable=cofe_var[3], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[3].place(x=300,y=500)
    mc[3]=Entry(mid_frame,textvariable=cofe_txt[3],width=5)
    mc[3].place(x=900,y=515)
    mc[3].config(state='disabled')
    
    l[4] = Checkbutton(mid_frame, text="Cappuccino\t\t 50/-   \tQty",variable=cofe_var[4], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[4].place(x=300,y=600)
    mc[4]=Entry(mid_frame,textvariable=cofe_txt[4],width=5)
    mc[4].place(x=900,y=615)
    mc[4].config(state='disabled')
    
    l[5] = Checkbutton(mid_frame, text="Cafe Mocha\t\t 55/-   \tQty",variable=cofe_var[5], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[5].place(x=300,y=700)
    mc[5]=Entry(mid_frame,textvariable=cofe_txt[5],width=5)
    mc[5].place(x=900,y=715)
    mc[5].config(state='disabled')

    l[6] = Checkbutton(mid_frame, text="Caramel \t\t 40/-   \tQty",variable=cofe_var[6], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[6].place(x=300,y=800)
    mc[6]=Entry(mid_frame,textvariable=cofe_txt[6],width=5)
    mc[6].place(x=900,y=815)
    mc[6].config(state='disabled')

    l[7] = Checkbutton(mid_frame, text="Vanilla Latte\t\t 35/-   \tQty",variable=cofe_var[7], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_cof)
    l[7].place(x=300,y=900)
    mc[7]=Entry(mid_frame,textvariable=cofe_txt[7],width=5)
    mc[7].place(x=900,y=915)
    mc[7].config(state='disabled')

    def plc_ord():
        for i in range(0,8):
            if cofe_var[i].get()!=0:
                if cofe_txt[i].get()!="":
                    lsb1.insert(END,cf_s[i][:-4])
                    lsb3.insert(END,cofe_txt[i].get())
                    lsb2.insert(END,int(cf_s[i][-4:-2]))
                    lsb4.insert(END,int(cf_s[i][-4:-2])*int(cofe_txt[i].get()))
                    l[i].deselect()
                    chk_cof()
                else:
                    l[i].config(bg="red")
                    l[i].flash()
                    messagebox.showerror("",f"Quantity is not Given for {cf_s[i]}")
                    l[i].config(bg="#fffee7")
        amt=[0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        j,total=0,0
        p3=lsb4.get(2,lsb1.size()-1)
        for i in p3:
            amt[j]=i
            total+=amt[j]
            j+=1

        total_dis.config(text=total)
        
    ord_btn=Button(mid_frame,text="Add Item",font="Arial 10 bold ",width=15,height=2,command=plc_ord)
    ord_btn.place(x=1050,y=500)

    def reset():
        for i in range(0,8):
            l[i].deselect()
        chk_cof()

    reset_btn=Button(mid_frame,text="Reset",font="Arial 10 bold",width=15,height=2,command=reset)
    reset_btn.place(x=1050,y=700)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def des_snk():

    b1.config(bg="white")
    b2.config(bg='#0de6ed')
    b3.config(bg='white')
    b4.config(bg='white')
    b5.config(bg='white')
    
    l=[0,0,0,0,0,0,0,0,0,0,0]
    
    l[0] =Checkbutton(mid_frame, text="Vada Pav\t\t 20/-   \tQty",variable=snk_var[0], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[0].place(x=300,y=200)
    ms[0]=Entry(mid_frame,width=5,textvariable=snk_txt[0])
    ms[0].place(x=900,y=215)
    ms[0].config(state='disabled')

    l[1] =Checkbutton(mid_frame, text="Samosa\t\t\t 15/-   \tQty",variable=snk_var[1], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[1].place(x=300,y=300)
    ms[1]=Entry(mid_frame,textvariable=snk_txt[1],width=5)
    ms[1].place(x=900,y=315)
    ms[1].config(state='disabled')
    
    l[2] =Checkbutton(mid_frame, text="Sandwich\t\t 20/-   \tQty",variable=snk_var[2], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[2].place(x=300,y=400)
    ms[2]=Entry(mid_frame,textvariable=snk_txt[2],width=5)
    ms[2].place(x=900,y=415)
    ms[2].config(state='disabled')
    
    l[3] =Checkbutton(mid_frame, text="Burger\t\t\t 40/-   \tQty",variable=snk_var[3], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[3].place(x=300,y=500)
    ms[3]=Entry(mid_frame,textvariable=snk_txt[3],width=5)
    ms[3].place(x=900,y=515)
    ms[3].config(state='disabled')
    
    l[4] =Checkbutton(mid_frame, text="Pizza\t\t\t 80/-   \tQty",variable=snk_var[4], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[4].place(x=300,y=600)
    ms[4]=Entry(mid_frame,textvariable=snk_txt[4],width=5)
    ms[4].place(x=900,y=615)
    ms[4].config(state='disabled')
    
    l[5] =Checkbutton(mid_frame, text="Pasta\t\t\t 60/-   \tQty",variable=snk_var[5], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[5].place(x=300,y=700)
    ms[5]=Entry(mid_frame,textvariable=snk_txt[5],width=5)
    ms[5].place(x=900,y=715)
    ms[5].config(state='disabled')

    l[6] =Checkbutton(mid_frame, text="Manchurian \t\t 80/-   \tQty",variable=snk_var[6], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[6].place(x=300,y=800)
    ms[6]=Entry(mid_frame,textvariable=snk_txt[6],width=5)
    ms[6].place(x=900,y=815)
    ms[6].config(state='disabled')

    l[7] =Checkbutton(mid_frame, text="Pav Bhaji\t\t 40/-   \tQty",variable=snk_var[7], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_snk)
    l[7].place(x=300,y=900)
    ms[7]=Entry(mid_frame,textvariable=snk_txt[7],width=5)
    ms[7].place(x=900,y=915)
    ms[7].config(state='disabled')

    def plc_ord():
        for i in range(0,8):
            if snk_var[i].get()!=0:
                if snk_txt[i].get()!="":
                    lsb1.insert(END,snk_s[i][:-4])
                    lsb3.insert(END,snk_txt[i].get())
                    lsb2.insert(END,int(snk_s[i][-4:-2]))
                    lsb4.insert(END,int(snk_s[i][-4:-2])*int(snk_txt[i].get()))
                    l[i].deselect()
                    chk_snk()
                else:
                    l[i].config(bg="red")
                    l[i].flash()
                    messagebox.showerror("",f"Quantity is not Given for {snk_s[i]}")
                    l[i].config(bg="#fffee7")
        amt=[0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        j,total=0,0
        p3=lsb4.get(2,lsb1.size()-1)
        for i in p3:
            amt[j]=i
            total+=amt[j]
            j+=1

        total_dis.config(text=total)
    
    ord_btn=Button(mid_frame,text="Add Item",font="Arial 10 bold",width=15,height=2,command=plc_ord)
    ord_btn.place(x=1050,y=500)

    def reset():
        for i in range(0,8):
            l[i].deselect()
        chk_snk()

    reset_btn=Button(mid_frame,text="Reset",font="Arial 10 bold",width=15,height=2,command=reset)
    reset_btn.place(x=1050,y=700)


def des_ice():

    b1.config(bg="white")
    b2.config(bg='white')
    b3.config(bg='#0de6ed')
    b4.config(bg='white')
    b5.config(bg='white')

    l=[0,0,0,0,0,0,0,0,0,0,0]
    
    l[0] =Checkbutton(mid_frame, text="Mango\t\t\t 35/-   \tQty",variable=ice_var[0], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[0].place(x=300,y=200)
    mi[0]=Entry(mid_frame,width=5,textvariable=ice_txt[0])
    mi[0].place(x=900,y=215)
    mi[0].config(state='disabled')

    l[1] =Checkbutton(mid_frame, text="Mava\t\t\t 20/-   \tQty",variable=ice_var[1], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[1].place(x=300,y=300)
    mi[1]=Entry(mid_frame,textvariable=ice_txt[1],width=5)
    mi[1].place(x=900,y=315)
    mi[1].config(state='disabled')
    
    l[2] =Checkbutton(mid_frame, text="Coco\t\t\t 25/-   \tQty",variable=ice_var[2], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[2].place(x=300,y=400)
    mi[2]=Entry(mid_frame,textvariable=ice_txt[2],width=5)
    mi[2].place(x=900,y=415)
    mi[2].config(state='disabled')
    
    l[3] =Checkbutton(mid_frame, text="Kiwi\t\t\t 35/-   \tQty",variable=ice_var[3], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[3].place(x=300,y=500)
    mi[3]=Entry(mid_frame,textvariable=ice_txt[3],width=5)
    mi[3].place(x=900,y=515)
    mi[3].config(state='disabled')
    
    l[4] =Checkbutton(mid_frame, text="Anjeer\t\t\t 40/-   \tQty",variable=ice_var[4], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[4].place(x=300,y=600)
    mi[4]=Entry(mid_frame,textvariable=ice_txt[4],width=5)
    mi[4].place(x=900,y=615)
    mi[4].config(state='disabled')
    
    l[5] =Checkbutton(mid_frame, text="Rajbhog\t\t\t 20/-   \tQty",variable=ice_var[5], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[5].place(x=300,y=700)
    mi[5]=Entry(mid_frame,textvariable=ice_txt[5],width=5)
    mi[5].place(x=900,y=715)
    mi[5].config(state='disabled')

    l[6] =Checkbutton(mid_frame, text="Guava \t\t\t 30/-   \tQty",variable=ice_var[6], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[6].place(x=300,y=800)
    mi[6]=Entry(mid_frame,textvariable=ice_txt[6],width=5)
    mi[6].place(x=900,y=815)
    mi[6].config(state='disabled')

    l[7] =Checkbutton(mid_frame, text="Dry Fruit\t\t 45/-   \tQty",variable=ice_var[7], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_ice)
    l[7].place(x=300,y=900)
    mi[7]=Entry(mid_frame,textvariable=ice_txt[7],width=5)
    mi[7].place(x=900,y=915)
    mi[7].config(state='disabled')

    def plc_ord():
        for i in range(0,8):
            if ice_var[i].get()!=0:
                if ice_txt[i].get()!="":
                    lsb1.insert(END,ice_s[i][:-4])
                    lsb3.insert(END,ice_txt[i].get())
                    lsb2.insert(END,int(ice_s[i][-4:-2]))
                    lsb4.insert(END,int(ice_s[i][-4:-2])*int(ice_txt[i].get()))
                    l[i].deselect()
                    chk_ice()
                else:
                    l[i].config(bg="red")
                    l[i].flash()
                    messagebox.showerror("",f"Quantity is not Given for {ice_s[i]}")
                    l[i].config(bg="#fffee7")
        amt=[0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        j,total=0,0
        p3=lsb4.get(2,lsb1.size()-1)
        for i in p3:
            amt[j]=i
            total+=amt[j]
            j+=1
        total_dis.config(text=total)
        
    ord_btn=Button(mid_frame,text="Add Item",font="Arial 10 bold",width=15,height=2,command=plc_ord)
    ord_btn.place(x=1050,y=500)

    def reset():
        for i in range(0,8):
            l[i].deselect()
        chk_ice()

    reset_btn=Button(mid_frame,text="Reset",font="Arial 10 bold",width=15,height=2,command=reset)
    reset_btn.place(x=1050,y=700)


def des_drnk():

    b1.config(bg="white")
    b2.config(bg='white')
    b3.config(bg='white')
    b4.config(bg='#0de6ed')
    b5.config(bg='white')

    l=[0,0,0,0,0,0,0,0,0,0,0]

    l[0] =Checkbutton(mid_frame, text="Iced Coffee\t\t 20/-   \tQty",variable=cold_var[0], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[0].place(x=300,y=200)    
    md[0]=Entry(mid_frame,width=5,textvariable=cold_txt[0])
    md[0].place(x=900,y=215)
    md[0].config(state='disabled')

    l[1] =Checkbutton(mid_frame, text="Iced Tea\t\t\t 20/-   \tQty",variable=cold_var[1], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[1].place(x=300,y=300)
    md[1]=Entry(mid_frame,textvariable=cold_txt[1],width=5)
    md[1].place(x=900,y=315)
    md[1].config(state='disabled')
    
    l[2] =Checkbutton(mid_frame, text="Mango Slice\t\t 25/-   \tQty",variable=cold_var[2], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[2].place(x=300,y=400)
    md[2]=Entry(mid_frame,textvariable=cold_txt[2],width=5)
    md[2].place(x=900,y=415)
    md[2].config(state='disabled')
    
    l[3] =Checkbutton(mid_frame, text="Mastani\t\t\t 40/-   \tQty",variable=cold_var[3], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[3].place(x=300,y=500)
    md[3]=Entry(mid_frame,textvariable=cold_txt[3],width=5)
    md[3].place(x=900,y=515)
    md[3].config(state='disabled')
    
    l[4] =Checkbutton(mid_frame, text="MilkShake\t\t 45/-   \tQty",variable=cold_var[4], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[4].place(x=300,y=600)
    md[4]=Entry(mid_frame,textvariable=cold_txt[4],width=5)
    md[4].place(x=900,y=615)
    md[4].config(state='disabled')
    
    l[5] =Checkbutton(mid_frame, text="Cola\t\t\t 30/-   \tQty",variable=cold_var[5], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[5].place(x=300,y=700)
    md[5]=Entry(mid_frame,textvariable=cold_txt[5],width=5)
    md[5].place(x=900,y=715)
    md[5].config(state='disabled')

    l[6] =Checkbutton(mid_frame, text="Sprite \t\t\t 40/-   \tQty",variable=cold_var[6], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[6].place(x=300,y=800)
    md[6]=Entry(mid_frame,textvariable=cold_txt[6],width=5)
    md[6].place(x=900,y=815)
    md[6].config(state='disabled')

    l[7] =Checkbutton(mid_frame, text="Mirinda\t\t\t 30/-   \tQty",variable=cold_var[7], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_drnk)
    l[7].place(x=300,y=900)
    md[7]=Entry(mid_frame,textvariable=cold_txt[7],width=5)
    md[7].place(x=900,y=915)
    md[7].config(state='disabled')
        
    def plc_ord():
        for i in range(0,8):
            if cold_var[i].get()!=0:
                if cold_txt[i].get()!="":
                    lsb1.insert(END,cold_s[i][:-4])
                    lsb3.insert(END,cold_txt[i].get())
                    lsb2.insert(END,int(cold_s[i][-4:-2]))
                    lsb4.insert(END,int(cold_s[i][-4:-2])*int(cold_txt[i].get()))
                    l[i].deselect()
                    chk_drnk()
                else:
                    l[i].config(bg="red")
                    l[i].flash()
                    messagebox.showerror("",f"Quantity is not Given for {cold_s[i]}")
                    l[i].config(bg="#fffee7")
        amt=[0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        j,total=0,0
        p3=lsb4.get(2,lsb1.size()-1)
        for i in p3:
            amt[j]=i
            total+=amt[j]
            j+=1
        total_dis.config(text=total)
        
    ord_btn=Button(mid_frame,text="Add Item",font="Arial 10 bold",width=15,height=2,command=plc_ord)
    ord_btn.place(x=1050,y=500)

    def reset():
        for i in range(0,8):
            l[i].deselect()
        chk_drnk()

    reset_btn=Button(mid_frame,text="Reset",font="Arial 10 bold",width=15,height=2,command=reset)
    reset_btn.place(x=1050,y=700)


def des_desrt():

    b1.config(bg="white")
    b2.config(bg='white')
    b3.config(bg='white')
    b4.config(bg='white')
    b5.config(bg='#0de6ed')

    l=[0,0,0,0,0,0,0,0,0,0,0]

    l[0] =Checkbutton(mid_frame, text="Cake\t\t\t 50/-   \tQty",variable=desrt_var[0], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[0].place(x=300,y=200)    
    mds[0]=Entry(mid_frame,width=5,textvariable=desrt_txt[0])
    mds[0].place(x=900,y=215)
    mds[0].config(state='disabled')

    l[1] =Checkbutton(mid_frame, text="Cup Cake\t\t 40/-   \tQty",variable=desrt_var[1], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[1].place(x=300,y=300)
    mds[1]=Entry(mid_frame,textvariable=desrt_txt[1],width=5)
    mds[1].place(x=900,y=315)
    mds[1].config(state='disabled')
    
    l[2] =Checkbutton(mid_frame, text="Pastries\t\t\t 30/-   \tQty",variable=desrt_var[2], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[2].place(x=300,y=400)
    mds[2]=Entry(mid_frame,textvariable=desrt_txt[2],width=5)
    mds[2].place(x=900,y=415)
    mds[2].config(state='disabled')
    
    l[3] =Checkbutton(mid_frame, text="Doughnut\t\t 25/-   \tQty",variable=desrt_var[3], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[3].place(x=300,y=500)
    mds[3]=Entry(mid_frame,textvariable=desrt_txt[3],width=5)
    mds[3].place(x=900,y=515)
    mds[3].config(state='disabled')
    
    l[4] =Checkbutton(mid_frame, text="Pudding\t\t\t 20/-   \tQty",variable=desrt_var[4], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[4].place(x=300,y=600)
    mds[4]=Entry(mid_frame,textvariable=desrt_txt[4],width=5)
    mds[4].place(x=900,y=615)
    mds[4].config(state='disabled')
    
    l[5] =Checkbutton(mid_frame, text="Choco Balls\t\t 45/-   \tQty",variable=desrt_var[5], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[5].place(x=300,y=700)
    mds[5]=Entry(mid_frame,textvariable=desrt_txt[5],width=5)
    mds[5].place(x=900,y=715)
    mds[5].config(state='disabled')

    l[6] =Checkbutton(mid_frame, text="Biscuit \t\t\t 20/-   \tQty",variable=desrt_var[6], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[6].place(x=300,y=800)
    mds[6]=Entry(mid_frame,textvariable=desrt_txt[6],width=5)
    mds[6].place(x=900,y=815)
    mds[6].config(state='disabled')

    l[7] =Checkbutton(mid_frame, text="Charlotte \t\t 40/-   \tQty",variable=desrt_var[7], font="rockwell 16 bold", fg="#795755",bg="#fffee7",command=chk_desrt)
    l[7].place(x=300,y=900)
    mds[7]=Entry(mid_frame,textvariable=desrt_txt[7],width=5)
    mds[7].place(x=900,y=915)
    mds[7].config(state='disabled')

    def plc_ord():
        for i in range(0,8):
            if desrt_var[i].get()!=0:
                if desrt_txt[i].get()!="":
                    lsb1.insert(END,desrt_s[i][:-4])
                    lsb3.insert(END,desrt_txt[i].get())
                    lsb2.insert(END,int(desrt_s[i][-4:-2]))
                    lsb4.insert(END,int(desrt_s[i][-4:-2])*int(desrt_txt[i].get()))
                    l[i].deselect()
                    chk_desrt()
                else:
                    l[i].config(bg="red")
                    l[i].flash()
                    messagebox.showerror("",f"Quantity is not Given for {desrt_s[i]}")
                    l[i].config(bg="#fffee7")
        amt=[0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        j,total=0,0
        p3=lsb4.get(2,lsb1.size()-1)
        for i in p3:
            amt[j]=i
            total+=amt[j]
            j+=1
        total_dis.config(text=total)

    ord_btn=Button(mid_frame,text="Add Item",font="Arial 10 bold",width=15,height=2,command=plc_ord)
    ord_btn.place(x=1050,y=500)

    def reset():
        for i in range(0,8):
            l[i].deselect()
        chk_desrt()

    reset_btn=Button(mid_frame,text="Reset",font="Arial 10 bold",width=15,height=2,command=reset)
    reset_btn.place(x=1050,y=700)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------    

b1 = Button(left_frame, text="COFFEE",padx=45,pady=10,relief=FLAT,activebackground="#fffee7",bg="white",command=des_cof)
b1.place(x=0,y=220)

b2 = Button(left_frame, text="SNACKS",padx=42,pady=10,relief=FLAT,activebackground="#0de6ed",bg="white",command=des_snk)
b2.place(x=0,y=320)

b3 = Button(left_frame, text="ICE-CREAM",padx=32,pady=10,relief=FLAT,activebackground="#0de6ed",bg="white",command=des_ice)
b3.place(x=0,y=420)

b4 = Button(left_frame, text="COLD DRINK",padx=27,pady=10,relief=FLAT,activebackground="#0de6ed",bg="white",command=des_drnk)
b4.place(x=0,y=520)

b5 = Button(left_frame, text="DESERT",padx=44,pady=10,relief=FLAT,activebackground="#0de6ed",bg="white",command=des_desrt)
b5.place(x=0,y=620)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def chk_cof():
    for i in range(0,8):
        if cofe_var[i].get()==1:
            mc[i].config(state='normal')
        elif cofe_var[i].get()==0:
            mc[i].config(state='disabled')
            cofe_txt[i].set("")
        

def chk_snk():
    for i in range(0,8):
        if snk_var[i].get()==1:
            ms[i].config(state='normal')
        elif snk_var[i].get()==0:
            ms[i].config(state='disabled')
            snk_txt[i].set("")
        

def chk_ice():
    for i in range(0,8):
        if ice_var[i].get()==1:
            mi[i].config(state='normal')
        elif ice_var[i].get()==0:
            mi[i].config(state='disabled')
            ice_txt[i].set("")
            


def chk_drnk():
    for i in range(0,8):
        if cold_var[i].get()==1:
            md[i].config(state='normal')
        elif cold_var[i].get()==0:
            md[i].config(state='disabled')
            cold_txt[i].set("")
            
            
        

def chk_desrt():
    for i in range(0,8):
        if desrt_var[i].get()==1:
            mds[i].config(state='normal')
        elif desrt_var[i].get()==0:
            mds[i].config(state='disabled')
            desrt_txt[i].set("")
    
def Del():
               k=lsb1.index(ANCHOR)
               if k<2:
                   messagebox.showinfo("Not Valid","Cannot Remove!!!!!!")
                   return
               lsb1.delete(ANCHOR)
               lsb4.delete(k)
               p3=lsb4.get(2,lsb1.size()-1)
               na3=[0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,]
               j,total=0,0
               for i in p3:
                   na3[j]=i
                   total+=na3[j]
                   j+=1
               total_dis.config(text=total)
               lsb2.delete(k)              
               lsb3.delete(k)
               


def bil():
    p=lsb1.get(2,lsb1.size()-1)
    if not p:
            messagebox.showinfo("Empty Cart","Sorry!!! there is no item added")
            return
    pop=Tk()
    pop.config(bg="white")
    pop.title("Billing")
    pop.iconbitmap('images\profile.ico')
    pop.geometry("800x700")
    lb1=Listbox(pop,width=30,height=22,bg="white",relief=FLAT)
    lb1.place(x=65,y=9)

    lb2=Listbox(pop,width=18,height=22,bg="white",relief=FLAT)
    lb2.place(x=308,y=9)

    lb3=Listbox(pop,width=18,height=22,bg="white",relief=FLAT)
    lb3.place(x=455,y=9)

    lb4=Listbox(pop,width=18,height=22,bg="white",relief=FLAT)
    lb4.place(x=602,y=9)


    lb1.insert(END,'                        Name')
    lb1.insert(END,"="*40)
    lb2.insert(END,'                Unit')
    lb2.insert(END,"="*40)
    lb3.insert(END,'            Quantity')
    lb3.insert(END,"="*40)
    lb4.insert(END,'            Amount')
    lb4.insert(END,"="*40)

    p=lsb1.get(2,lsb1.size()-1)
    na=[5,322,3,33,3,3,3,3,3,3,3,34,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    na1=[5,322,3,33,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    na2=[5,322,3,33,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    na3=[5,322,3,33,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    j=0
    total,ID,total_gst=0,0,0
    for i in p:
        na[j]=i
        j+=1
    p1=lsb2.get(2,lsb1.size()-1)
    j=0
    for i in p1:
            na1[j]=i
            j+=1
    p2=lsb3.get(2,lsb1.size()-1)
    j=0
    for i in p2:
            na2[j]=i
            j+=1
    p3=lsb4.get(2,lsb1.size()-1)
    j=0
    for i in p3:
            na3[j]=i
            total+=na3[j]
            j+=1

    total_dis1=Label(pop,text="Total Amount With 18% GST : - ",padx=5,pady=5,font="calibri 16 bold",bg="white")
    total_dis1.place(x=66,y=475)
    
    total_gst=total+(total*0.18)
    
    t_dis=Label(pop,text=str(total_gst)+"/-",padx=5,pady=5,font="calibri 16 bold",bg="white")
    t_dis.place(x=426,y=475)
    
    j=0
    for i in range(0,lsb1.size()-2):
        lb1.insert(END,na[j])
        lb2.insert(END,na1[j])
        lb3.insert(END,na2[j])
        lb4.insert(END,na3[j])
        j+=1
    def order():
        mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='Shop')
        cur=mycon.cursor()
        ID=int(str(random.randrange(111,999))+str(random.randrange(11,99)))
        for i in range(0,lsb1.size()-2):        
            q=f"insert into bill values({ID},'{na[i]}',{na1[i]},{na2[i]},{na3[i]})"
            cur.execute(q)
            mycon.commit()
        mycon.close()
        cur.close()
        lsb1.delete(2,END)
        lsb2.delete(2,END)
        lsb3.delete(2,END)
        lsb4.delete(2,END)
        pop.destroy()
        messagebox.showinfo("Ordered",f" Your Order has been placed\nOrder ID : {ID}")
    def cancel_order():
        lb1.delete(2,END)
        lb2.delete(2,END)
        lb3.delete(2,END)
        lb4.delete(2,END)
        messagebox.showinfo("Canceled","Order is Canceled")
        lsb1.delete(2,END)
        lsb2.delete(2,END)
        lsb3.delete(2,END)
        lsb4.delete(2,END)
        total_dis.config(text="")
        pop.destroy()
    Button(pop,text="Order",padx=20,pady=10,command=order).place(x=150,y=600)
    Button(pop,text="Cancel Order",padx=10,pady=10,command=cancel_order).place(x=450,y=600)
    
    pop.mainloop()
#--------------------------------------------------------------
global Id
Id=IntVar()
def search_order():
    pop=Tk()
    pop.config(bg="white")
    pop.title("Billing")
    pop.iconbitmap('images\profile.ico')
    pop.geometry("800x700")
    lb1=Listbox(pop,width=30,height=22,bg="white",relief=FLAT)
    lb1.place(x=65,y=9)

    lb2=Listbox(pop,width=18,height=22,bg="white",relief=FLAT)
    lb2.place(x=308,y=9)

    lb3=Listbox(pop,width=18,height=22,bg="white",relief=FLAT)
    lb3.place(x=455,y=9)

    lb4=Listbox(pop,width=18,height=22,bg="white",relief=FLAT)
    lb4.place(x=602,y=9)
    
    lb1.insert(END,'                        Name')
    lb1.insert(END,"="*40)
    lb2.insert(END,'                Unit')
    lb2.insert(END,"="*40)
    lb3.insert(END,'            Quantity')
    lb3.insert(END,"="*40)
    lb4.insert(END,'            Amount')
    lb4.insert(END,"="*40)

    total_dis1=Label(pop,text="Total Amount With 18% GST : - ",padx=5,pady=5,font="calibri 16 bold",bg="white")
    total_dis1.place(x=66,y=475)

    
    
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='root',database='Shop')
    cur=mycon.cursor()
    n=Id.get()
    q =f"select order_id,p_name,price,quan,amnt from bill where order_id ={n}"
    cur.execute(q)
    row = cur.fetchall()
    if not row:
        messagebox.showerror("Invalid ID",f" Your ID: {n} is not present")
        pop.destroy()
        return
    else:
        for i in row:
            lb1.insert(END,i[1])
            lb2.insert(END,i[2])
            lb3.insert(END,i[3])
            lb4.insert(END,i[4])
    mycon.close()
    cur.close()
    
    data=[0,0,0,0,0,00,0,0,0,0,0,0,0,]
    dat=lb4.get(2,lb1.size()-1)
    t,j=0,0
    for i in dat:
            data[j]=i
            t+=data[j]
            j+=1

    total_gst=t+(t*0.18)
    
    t_dis=Label(pop,text=str(total_gst)+"/-",padx=5,pady=5,font="calibri 16 bold",bg="white")
    t_dis.place(x=426,y=475)
    pop.mainloop()
      
Label(right_frame,text="Order ID :",bg="#fffee7",font="calibri 14").place(x=1370,y=150)

text1=Entry(right_frame,width=10,textvariable=Id,borderwidth=2)
text1.place(x=1450,y=151)

Button(right_frame,text="Search",command=search_order,padx=2,pady=2,font="Arial 8 bold").place(x=1800,y=151)

total_display=Label(right_frame,text="Total : - ",padx=5,pady=5,bg="#fffee7",font="calibri 16 bold")
total_display.place(x=1583,y=781)

            
lsb1=Listbox(right_frame,width=27,height=28,bg="#e6ed75")
lsb1.place(x=1365,y=180)

lsb2=Listbox(right_frame,width=13,height=28,bg="#e6ed75")
lsb2.place(x=1585,y=180)

lsb3=Listbox(right_frame,width=14,height=28,bg="#e6ed75")
lsb3.place(x=1694,y=180)

lsb4=Listbox(right_frame,width=12,height=28,bg="#e6ed75")
lsb4.place(x=1809,y=180)

lsb1.insert(END,"                    Name")
lsb1.insert(END,"="*40)
lsb2.insert(END,"       Unit")
lsb2.insert(END,"="*18)
lsb3.insert(END,"        Quantity")
lsb3.insert(END,"="*18)
lsb4.insert(END,"        Amount")
lsb4.insert(END,"="*18)

bl1=Button(right_frame,text="Choose & Remove Item",padx=5,pady=15,font="Arial 10 bold",command=lambda:Del())
bl1.place(x=1370,y=875)

bl2=Button(right_frame,text="BILL",padx=26,pady=15,font="Arial 10 bold",command=lambda:bil())
bl2.place(x=1800,y=875)



    

main_win.mainloop()











