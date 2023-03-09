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
    root.title("foodx")
    root.option_add('*font','Garamond 24 bold')
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=2)
    return root

def createconnection():
    global conn, cursor 
    conn = sqlite3.connect('project01.db') 
    cursor = conn.cursor()

def loginlayout():
    global userentry , userinfo
    global pwdentry  
    loginframe = Frame(root,bg='pink')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    Label(loginframe, text="Username ", bg='pink', fg='black', padx=10).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe, bg='#FFA07A', fg='black', width=20, textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    Label(loginframe, text="Password ", bg='pink', fg='black', padx=20).grid(row=2,column=0,sticky='e')
    pwdentry = Entry(loginframe, bg='#FFA07A', fg='black', width=20, textvariable=pwdinfo, show='*')
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Button(loginframe, text="Login", compound=RIGHT, width=10, command=loginclick).grid(row=3, column=1, padx=20, pady=20, ipady=15, sticky=E)
    Button(loginframe, text="Register",  compound=LEFT, width=10, command=regislayout).grid(row=3, column=1, padx=20, pady=20, ipady=15, sticky=W)
    loginframe.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='NEWS')

    
    
def regislayout():

    global fullname,lastname,newuser,newpwd,cfpwd,adr
    global regis_frm
    
    root.title("Register")
    regis_frm = Frame(root,bg='pink') 
    regis_frm.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
    regis_frm.columnconfigure((0,1),weight=1)
    regis_frm.place(x=0,y=0,width=w,height=h)
    
    Label(regis_frm, bg='pink').grid(row=0,columnspan=2)
    Label(regis_frm, text="Username : ", bg='pink', fg='black', padx=10).grid(row=1,column=0,sticky='e')
    newuser = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=newuser)
    newuser.grid(row=1,column=1,sticky='w',padx=20)


    Label(regis_frm, text="Password : ", bg='pink', fg='black', padx=10).grid(row=5,column=0,sticky='e')
    newpwd = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=newpwd,show='*')
    newpwd.grid(row=5,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Firstname : ", bg='pink', fg='black', padx=10).grid(row=2,column=0,sticky='e')
    fullname = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=fname)
    fullname.grid(row=2,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Lastname : ", bg='pink', fg='black', padx=10).grid(row=3,column=0,sticky='e')
    lastname = Entry(regis_frm, bg='#FFA07A', fg='black', width=20, textvariable=lname)
    lastname.grid(row=3,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Confirm password : ", bg='pink', fg='black', padx=10).grid(row=6,column=0,sticky='e')
    cfpwd = Entry(regis_frm,width=20,bg='#FFA07A',textvariable=cfinfo,show='*')
    cfpwd.grid(row=6,column=1,sticky='w',padx=20)

    Label(regis_frm, text="Adress: ", bg='pink', fg='black', padx=10).grid(row=4,column=0,sticky='e')
    adr = Entry(regis_frm,width=20,bg='#FFA07A', fg='black',textvariable=ads)
    adr.grid(row=4,column=1,sticky='w',padx=20)



    Button(regis_frm, text="Complete",  compound=LEFT, width=200,command=registration).grid(row=7, columnspan=2, padx=20, pady=20, ipady=15, sticky=E)

def loginclick():
    global result
    

    if userinfo.get() == "": 
        messagebox.showwarning("Admin","Enter username first.")
        userentry.focus_force()
    
    else:
        if pwdinfo.get() == "":
            messagebox.showwarning("Admin","Enter password first.")
            pwdentry.focus_force()
        else :
            sql = "SELECT* From userinfo WHERE user=? AND pwd=? " 
            cursor.execute(sql,[userinfo.get(),pwdinfo.get()]) 
            result = cursor.fetchall()
             
            if result : 
                messagebox.showinfo("Admin","Login succesfully")
                main() 
            else :
                
                messagebox.showwarning("Admin","Incorrect Username or password")


def registration() :
    if fname.get() == "":
        messagebox.showwarning("Admin",'Please enter fristname')
        fullname.focus_force()
    elif lname.get() == "":
        messagebox.showwarning("Admin",'Please enter lastname')
        lastname.focus_force()
    elif newuser.get()== "":
        messagebox.showwarning("Admin",'Please enter username')
        newuser.focus_force()
    elif adr.get()== "" :
        messagebox.showwarning("Admin",'Please enter Adress')
        adr.focus_force()
    elif newpwd.get()== "":
        messagebox.showwarning("Admin",'Please enter password')
        newpwd.focus_force()
    elif cfpwd.get()== "":
        messagebox.showwarning("Admin",'Please enter confirm password')
        cfpwd.focus_force()

def main():
    global profile_frm
    global result
    root.title("Profile")
    profile_frm = Frame(root,bg='#D8BFD8') 
    profile_frm.columnconfigure((0,1),weight=1)
    profile_frm.rowconfigure((0,1,2,3,4,5),weight=1)
    profile_frm.place(x=0,y=0,width=w,height=h)




w = 1000
h = 700
root=mainwindow()
userinfo = StringVar()
pwdinfo = StringVar()
ads = StringVar()
fname = StringVar()
lname = StringVar()
newuser = StringVar()
newpwd = StringVar()
cfinfo=StringVar()

createconnection()
loginlayout()
root.mainloop()