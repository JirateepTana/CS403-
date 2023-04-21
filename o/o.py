from cProfile import label
from itertools import count
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.font import names

def mainwindow():
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='pink')
    root.title("User UI")
    root.option_add('*font','Garamond 24 bold')
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=2)
    return root

def createconnection():
    global conn, cursor 
    conn = sqlite3.connect('o.db') 
    cursor = conn.cursor()

def loginlayout():
    global userentry , userinfo
    global pwdentry  
    loginframe = Frame(root,bg='pink')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    Label(loginframe, image=img1, bg='pink').grid(row=0,columnspan=2)
    Label(loginframe, text="Email ", bg='pink', fg='black', padx=10).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe, bg='#FFA07A', fg='black', width=20, textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    Label(loginframe, text="Password ", bg='pink', fg='black', padx=20).grid(row=2,column=0,sticky='e')
    pwdentry = Entry(loginframe, bg='#FFA07A', fg='black', width=20, textvariable=pwdinfo, show='*')
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Button(loginframe, text="Login", image=img3, compound=RIGHT, width=200, command=loginclick).grid(row=3, column=1, padx=20, pady=20, ipady=15, sticky=E)
    Button(loginframe, text="Register", image=img4, compound=LEFT, width=200, command=regislayout).grid(row=3, column=1, padx=20, pady=20, ipady=15, sticky=W)
    loginframe.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='NEWS')
    

def regislayout():

    global fullname,lastname,newuser,newpwd,ads,phone
    global regis_frm
    
    root.title("Register")
    regis_frm = Frame(root,bg='pink') 
    regis_frm.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    regis_frm.columnconfigure((0,1),weight=1)
    regis_frm.place(x=0,y=0,width=w,height=h)
    
    Label(regis_frm, image=img2, bg='pink').grid(row=0,columnspan=2)
    Label(regis_frm, text="Email : ", bg='pink', fg='black', padx=10).grid(row=1,column=0,sticky='e')
    newuser = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=newuser)
    newuser.grid(row=1,column=1,sticky='w',padx=20)


    Label(regis_frm, text="Password : ", bg='pink', fg='black', padx=10).grid(row=4,column=0,sticky='e')
    newpwd = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=newpwd,show='*')
    newpwd.grid(row=4,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Firstname : ", bg='pink', fg='black', padx=10).grid(row=2,column=0,sticky='e')
    fullname = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=fname)
    fullname.grid(row=2,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Lastname : ", bg='pink', fg='black', padx=10).grid(row=3,column=0,sticky='e')
    lastname = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=lname)
    lastname.grid(row=3,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Adress : ", bg='pink', fg='black', padx=10).grid(row=5,column=0,sticky='e')
    ads = Entry(regis_frm,width=20,bg='#FFA07A',textvariable=ads)
    ads.grid(row=5,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Phone Number : ", bg='pink', fg='black', padx=10).grid(row=6,column=0,sticky='e')
    phone = Entry(regis_frm,width=20,bg='#FFA07A',textvariable=phone)
    phone.grid(row=6,column=1,sticky='w',padx=20)

    Button(regis_frm, text="Complete", image=img5, compound=LEFT, width=200, command=registration).grid(row=7, columnspan=2, padx=20, pady=20, ipady=15, sticky=E)

def registration() :
    if newuser.get()== "":
        messagebox.showwarning("Admin",'Please enter email')
        newuser.focus_force()
    
    elif fname.get() == "":
        messagebox.showwarning("Admin",'Please enter fristname')
        fullname.focus_force()
    elif lname.get() == "":
        messagebox.showwarning("Admin",'Please enter lastname')
        lastname.focus_force()
   
    elif newpwd.get()== "":
        messagebox.showwarning("Admin",'Please enter password')
        newpwd.focus_force()
    elif ads.get()== "":
        messagebox.showwarning("Admin",'Please enter Adress')
        ads.focus_force()
    elif phone.get()== "":
        messagebox.showwarning("Admin",'Please enter Phone number')
        phone.focus_force()
    #check blank other field
    else:
        sql_chk = "SELECT * FROM login WHERE email=?"
        cursor.execute(sql_chk,[newuser.get()])
        chk_result = cursor.fetchall()
        if chk_result:
            messagebox.showwarning("Admin",'username is already exists')
            newuser.focus_force()
            newuser.select_range(0,END)
        else:
            if newpwd.get() == newpwd.get():
                sql_ins = 'INSERT INTO login (email,pwd,fname,lname,ads,phone) values (?,?,?,?,?,?)'
                cursor.execute(sql_ins,[newuser.get(),newpwd.get(),fname.get(),lname.get(),ads.get(),phone.get()])
                conn.commit()
                messagebox.showinfo("Admin",'REGISTER SUCCESSFULLY')
                newuser.delete(0,END)
                newpwd.delete(0,END)
                
                fullname.delete(0,END)
                lastname.delete(0,END)
                exittologin()
                
            
            else:
                messagebox.showwarning("Admin",'CONFIRM PASSWORD IS NOT MATCHED')


def loginclick():
    global result

    if userinfo.get() == "": 
        messagebox.showwarning("Admin","Enter email first.")
        userentry.focus_force()
    
    else:
        if pwdinfo.get() == "":
            messagebox.showwarning("Admin","Enter password first.")
            pwdentry.focus_force()
        else :
            sql = "SELECT* From login WHERE email=? AND pwd=? " 
            cursor.execute(sql,[userinfo.get(),pwdinfo.get()]) 
            result = cursor.fetchall()
             
            if result : 
                messagebox.showinfo("ADmin","Login succesfully")
                main() 
            else :
                
                messagebox.showwarning("Admin","Incorrect Username or password")

def main():
    global main_frm 
    root.title("mains")
    main_frm = Frame(root,bg='#D8BFD8') 
    main_frm.columnconfigure((0,1,2,4,5),weight=1)
    main_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    main_frm.place(x=0,y=0,width=w,height=h)
    
    

    
    Label(main_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(main_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(main_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)
    Label(main_frm, text= "Kapow " , bg='#D8BFD8', fg='black', padx=10).grid(row=2,column=1, padx=10,stick=W)
    Label(main_frm, text= "Hamberger " , bg='#D8BFD8', fg='black', padx=10).grid(row=2,column=2, padx=10,stick=W)

    
    ff1= Entry(main_frm, bg='#FFA07A', fg='black', width=20, textvariable=f1)
    ff1.grid(row=5,column=1,sticky='w',padx=20)
    
    ff2 = Entry(main_frm, bg='#FFA07A', fg='black', width=20, textvariable=f2)
    ff2.grid(row=5,column=2,sticky='w',padx=20)
    


    Button(main_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)
    


def kid():
    global total
    


    try :
        a1 = int(f1.get())
    except:
        a1=0

    try :
        a2 = int(f2.get())
    except:
        a2=0 

    try :
        a3 = int(f3.get())
    except:
        a3=0 
    
    try :
        a4 = int(f4.get())
    except:
        a4=0 

    try :
        a5 = int(f5.get())
    except:
        a5=0

    try :
        a6 = int(f6.get())
    except:
        a6=0 

    try :
        a7 = int(f7.get())
    except:
        a7=0 
    
    try :
        a8 = int(f8.get())
    except:
        a8=0     
    
    try :
        a9 = int(f9.get())
    except:
        a9=0

    try :
        a10 = int(f10.get())
    except:
        a10=0 

    try :
        a11 = int(f11.get())
    except:
        a11=0 
    
    try :
        a12 = int(f12.get())
    except:
        a12=0 
    
    try :
        a13= int(f13.get())
    except:
        a13=0

    try :
        a14 = int(f14.get())
    except:
        a14=0 

    try :
        a15 = int(f15.get())
    except:
        a15=0 
    
    try :
        a16 = int(f16.get())
    except:
        a16=0 
    
    try :
        a17 = int(f17.get())
    except:
        a17=0

    try :
        a18 = int(f18.get())
    except:
        a18=0 



    c1=100*a1
    c2=200*a2
    c3=300*a3
    c4=240*a4
    c5=300*a5
    c6=230*a6
    c7=190*a7
    c8=300*a8
    c9=230*a9
    c10=210*a10
    c11=450*a11
    c12=230*a12
    c13=300*a13
    c14=450*a14
    c15=360*a15
    c16=340*a16
    c17=210*a17
    c18=230*a18
    total=c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18
    print(total)
    if total == 0 :
        messagebox.showwarning("Admin",'Please Select Food')
    else :
      payment()
    return total
    




def cfood():

    root.title("CHEF SPECIAL")
    c_frm = Frame(root,bg='#D8BFA2') 
    c_frm.columnconfigure((0,1),weight=1)
    c_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    c_frm.place(x=0,y=0,width=w,height=h)

    Label(c_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(c_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(c_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)

    
    ff3= Entry(c_frm, bg='#FFA07A', fg='black', width=20, textvariable=f3)
    ff3.grid(row=5,column=1,sticky='w',padx=20)
    
    ff4 = Entry(c_frm, bg='#FFA07A', fg='black', width=20, textvariable=f4)
    ff4.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(c_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)


def afood():
    root.title("APPETiZERS")
    a_frm = Frame(root,bg='#336633') 
    a_frm.columnconfigure((0,1),weight=1)
    a_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    a_frm.place(x=0,y=0,width=w,height=h)

    Label(a_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(a_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(a_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)

    
    ff5= Entry(a_frm, bg='#FFA07A', fg='black', width=20, textvariable=f5)
    ff5.grid(row=5,column=1,sticky='w',padx=20)
    
    ff6 = Entry(a_frm, bg='#FFA07A', fg='black', width=20, textvariable=f6)
    ff6.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(a_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)


def sfood():
    root.title("SOUP")
    s_frm = Frame(root,bg='#0033FF') 
    s_frm.columnconfigure((0,1),weight=1)
    s_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    s_frm.place(x=0,y=0,width=w,height=h)
    Label(s_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(s_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(s_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)


    ff7= Entry(s_frm, bg='#FFA07A', fg='black', width=20, textvariable=f7)
    ff7.grid(row=5,column=1,sticky='w',padx=20)
    
    ff8 = Entry(s_frm, bg='#FFA07A', fg='black', width=20, textvariable=f8)
    ff8.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(s_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)


def bfood():
    root.title("BEVERAGES")
    b_frm = Frame(root,bg='#0000FF') 
    b_frm.columnconfigure((0,1),weight=1)
    b_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    b_frm.place(x=0,y=0,width=w,height=h)
    Label(b_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(b_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(b_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)

    
    ff9= Entry(b_frm, bg='#FFA07A', fg='black', width=20, textvariable=f9)
    ff9.grid(row=5,column=1,sticky='w',padx=20)
    
    ff10 = Entry(b_frm, bg='#FFA07A', fg='black', width=20, textvariable=f10)
    ff10.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(b_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)


def nfood():
    root.title("NOODLES SOUP")
    n_frm = Frame(root,bg='#008800') 
    n_frm.columnconfigure((0,1),weight=1)
    n_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    n_frm.place(x=0,y=0,width=w,height=h)
    Label(n_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(n_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(n_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)

    
    ff11= Entry(n_frm, bg='#FFA07A', fg='black', width=20, textvariable=f11)
    ff11.grid(row=5,column=1,sticky='w',padx=20)
    
    ff12 = Entry(n_frm, bg='#FFA07A', fg='black', width=20, textvariable=f12)
    ff12.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(n_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)


def seafood():
    root.title("SEAFOOD")
    sea_frm = Frame(root,bg='#00BB00') 
    sea_frm.columnconfigure((0,1),weight=1)
    sea_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    sea_frm.place(x=0,y=0,width=w,height=h)
    Label(sea_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(sea_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(sea_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)

    
    ff13= Entry(sea_frm, bg='#FFA07A', fg='black', width=20, textvariable=f13)
    ff13.grid(row=5,column=1,sticky='w',padx=20)
    
    ff14 = Entry(sea_frm, bg='#FFA07A', fg='black', width=20, textvariable=f14)
    ff14.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(sea_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)


def safood():
    root.title("SALAD")
    sa_frm = Frame(root,bg='#CC0099') 
    sa_frm.columnconfigure((0,1),weight=1)
    sa_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    sa_frm.place(x=0,y=0,width=w,height=h)
    Label(sa_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(sa_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(sa_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)

    
    ff15= Entry(sa_frm, bg='#FFA07A', fg='black', width=20, textvariable=f15)
    ff15.grid(row=5,column=1,sticky='w',padx=20)
    
    ff16 = Entry(sa_frm, bg='#FFA07A', fg='black', width=20, textvariable=f16)
    ff16.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(sa_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)


def kfood():
    root.title("KIND")
    k_frm = Frame(root,bg='#333366') 
    k_frm.columnconfigure((0,1),weight=1)
    k_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    k_frm.place(x=0,y=0,width=w,height=h)
    Label(k_frm, text= "MONTHAI " , bg='#D8BFD8', fg='black', padx=10).grid(row=0,column=0, padx=10,stick=W)
    Button(k_frm, text="Lunch special", width=10, command=main).grid(row=1, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="Chef special", width=10, command=cfood).grid(row=2, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="APPETIZERS", width=10, command=afood).grid(row=3, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="Soup", width=10, command=sfood).grid(row=4, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="BEVERAGES", width=10, command=bfood).grid(row=5, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="NOODLES SOUPS", width=10, command=nfood).grid(row=6, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="SEAFOOD", width=10, command=seafood).grid(row=7, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="SALAD", width=10, command=safood).grid(row=8, column=0, padx=10, ipady=10, stick=W)
    Button(k_frm, text="KIDS", width=10, command=kfood).grid(row=9, column=0, padx=10, ipady=10, stick=W)

    
    ff17= Entry(k_frm, bg='#FFA07A', fg='black', width=20, textvariable=f17)
    ff17.grid(row=5,column=1,sticky='w',padx=20)
    
    ff18 = Entry(k_frm, bg='#FFA07A', fg='black', width=20, textvariable=f18)
    ff18.grid(row=5,column=2,sticky='w',padx=20)
    
    Button(k_frm, text="Total", width=10, command=kid).grid(row=9, column=4, padx=10, ipady=10, stick=W)



def payment():
    root.title("PAYMENT")
    pay_frm = Frame(root,bg='#333366') 
    pay_frm.columnconfigure((0,1),weight=1)
    pay_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    pay_frm.place(x=0,y=0,width=w,height=h)

    Label(pay_frm, image=img6, bg='pink').grid(row=0,columnspan=3)
    Label(pay_frm, text=total, bg='pink', fg='black', padx=10).grid(row=1,columnspan=3)

    Button(pay_frm, text="Back", width=10, command=main).grid(row=9, column=0, padx=10, ipady=10, stick=W)
    Button(pay_frm, text="Finish", width=10, command=exit).grid(row=9, column=5, padx=10, ipady=10, stick=W)





def resetclick():
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    userentry.focus_force() #focus widget

w = 1000
h = 650
createconnection()
root = mainwindow()

img1 = PhotoImage(file='img/user.png').subsample(4,4)
img2 = PhotoImage(file='img/resume.png').subsample(3,3)
img3 = PhotoImage(file='img/next.png').subsample(10,10)
img4 = PhotoImage(file='img/adduser.png').subsample(10,10)
img5 = PhotoImage(file='img/check.png').subsample(10,10)
img6 = PhotoImage(file='img/qrcode.png').subsample(10,10)

img_user = PhotoImage(file='img/girl.png').subsample(3,3)

ads = StringVar()
phone = StringVar()
num = StringVar()
userinfo = StringVar()
pwdinfo = StringVar()
fname = StringVar()
lname = StringVar()
newuser = StringVar()
newpwd = StringVar()
f1=IntVar()
f2=IntVar()
f3=IntVar()
f4=IntVar()
f5=IntVar()
f6=IntVar()
f7=IntVar()
f8=IntVar()
f9=IntVar()
f10=IntVar()
f11=IntVar()
f12=IntVar()
f13=IntVar()
f14=IntVar()
f15=IntVar()
f16=IntVar()
f17=IntVar()
f18=IntVar()

tot=IntVar()





def exittologin() :
    regis_frm.destroy()
    loginlayout() 

loginlayout()
root.mainloop()