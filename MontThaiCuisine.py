

import sqlite3
from tkinter import messagebox
from tkinter import *

def createconnection() :
    #global conn,cursor
    db_path = 'database/login.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn,cursor

def mainwindow() :
    root = Tk()
    w = 1000
    h = 600
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#8ac4d0')
    #root.config(bg='#4a3933')
    root.title("Login/Register Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout() :
    global userentry,pwdentry
    global userinfo, pwdinfo
    
    userinfo = StringVar()
    pwdinfo = StringVar()
    
    loginframe = Frame(root,bg='#085E7D')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    
    Label(loginframe,text="Login Application",font="Garamond 26 bold",compound=LEFT,bg='#085E7D',fg='#e4fbff').grid(row=0,columnspan=2)
    Label(loginframe,text="Username : ",bg='#085E7D',fg='#e4fbff',padx=20).grid(row=1,column=0,sticky='e')
    userentry = Entry(loginframe,bg='#e4fbff',width=20,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',padx=20)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=20,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,sticky='w',padx=20)
    Label(loginframe,text="Password  : ",bg='#085E7D',fg='#e4fbff',padx=20).grid(row=2,column=0,sticky='e')
    Button(loginframe,text="Login",width=10,command=lambda:loginclick(userinfo.get(),pwdinfo.get())).grid(row=3,column=1,pady=20,ipady=15,sticky='e',padx=20)
    #Button(loginframe,text="Register",width=10,command=regislayout).grid(row=3,column=1,pady=20,ipady=15,sticky='w',padx=20)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def loginclick(username,pwd) :
    #global result
    if username == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
        userentry.focus_force()
    else :
        
        
        # check username exists on database.
        sql = "select * from login where user = ?"
        cursor.execute(sql,[username])
        result = cursor.fetchone()
        if result :
            # Is password blank?
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                # check username and password 
                sql = "select * from login where user=? and pwd=? "
                # cursor.execute(sql,[username,pwd])   #case1
                cursor.execute(sql,(username,pwd))   #case2
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    print(result)
                    welcomepage(result)
                else :
                    messagebox.showwarning("Admin:","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")
            userentry.select_range(0,END)
            userentry.focus_force()

def regislayout() :
    global fullname,lastname,newuser,newpwd,cfpwd
    root.title("Welcome to User Registration : ")
    root.config(bg='lightblue')
    regisframe = Frame(root,bg='#8ac4d0')
    regisframe.rowconfigure((0,1,2,3,4,5,6),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    Label(regisframe,text="Registration Form",font="Garamond 26 bold",fg='#e4fbff',image=img1,compound=LEFT,bg='#1687a7').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    Label(regisframe,text='First name : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=1,column=0,sticky='e',padx=10)
    fullname = Entry(regisframe,width=20,bg='#d3e0ea')
    fullname.grid(row=1,column=1,sticky='w',padx=10)
    Label(regisframe,text='Last name : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    lastname = Entry(regisframe,width=20,bg='#d3e0ea')
    lastname.grid(row=2,column=1,sticky='w',padx=10)
    Label(regisframe,text="Username : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    newuser = Entry(regisframe,width=20,bg='#d3e0ea')
    newuser.grid(row=3,column=1,sticky='w',padx=10)
    Label(regisframe,text="Password : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=4,column=0,sticky='e',padx=10)
    newpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    newpwd.grid(row=4,column=1,sticky='w',padx=10)
    Label(regisframe,text="Confirm Password : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=5,column=0,sticky='e',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='#a1cae2',show='*')
    cfpwd.grid(row=5,column=1,sticky='w',padx=10)
    regisaction = Button(regisframe,text="Register Submit",command=registration)
    regisaction.grid(row=6,column=0,ipady=5,ipadx=5,pady=5,sticky='e')
    fullname.focus_force()
    loginbtn = Button(regisframe,text="Back to Login",command=loginlayout)
    loginbtn.grid(row=6,column=1,ipady=5,ipadx=5,pady=5,sticky='w',padx=10)
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def registration() :
    #print("Hello from registration")
    # TODO: Validate all data
    if fullname.get() == "" :
        messagebox.showwarning("Admin: ","Please enter firstname")
        fullname.focus_force()
    elif lastname.get() == "" :
        pass
    elif newuser.get() == "" :
        pass
    elif newpwd.get() == "" :
        pass    
    elif cfpwd.get() == "" :
        pass
    else : 

        result = retrieve_profile(newuser.get())

        if result :
            messagebox.showerror("Admin:","The username is already exists")
            print()
        else :
            if newpwd.get() == cfpwd.get() : #verify a new pwd and confirm pwd are equal
                sql = '''
                INSERT INTO login (user, pwd, fname, lname)
                VALUES (?, ?, ?, ?)
                ''' #insert into statement
                #execute sql query 
                conn, curr = createconnection()
                curr.execute(sql, [userinfo.get(), pwdinfo.get(), fullname.get(), lastname.get()])
                conn.commit()
                retrivedata()
                messagebox.showinfo("Admin:","Registration Successfully")                
            else :  #verify a new pwd and confirm pwd are not equal
                messagebox.showwarning("Admin: ","Incorrect a confirm password\n Try again")


def retrivedata() :
    sql = "select * from login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

def welcomepage(result) :
    clear_page()
    Label(root,text="Welcome to Main Page",fg='#534340',bg='#8ac4d0',font='Mali 32 bold').grid(row=0,columnspan=4)
    welcomeframe = Frame(root,bg='#085E7D')
    welcomeframe.rowconfigure((0,1,2,3),weight=1)
    welcomeframe.columnconfigure((0,1,2),weight=1)

    Label(welcomeframe,text="Welcome : "+result[2]+" "+result[3],bg='#085E7D',image=img1,compound=LEFT,fg='white').grid(row=0,columnspan=4)
    welcomeframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    Button(welcomeframe,text="My Profile",width=10,height=1,command=lambda: edit_profile(result)).grid(row=4,column=0,pady=10,padx=15,sticky=E)
    Button(welcomeframe,text="Manage Users",width=10,height=1,command=lambda: manage_users(result)).grid(row=4,column=1,pady=10,padx=15,sticky=E)
    Button(welcomeframe,text="Exit",width=10,height=1,command=root.quit).grid(row=4,column=2,pady=10,padx=15,sticky=E)

def get_users(frame, searchby, keyword):
    if keyword == '':
        messagebox.showwarning("Oops!", "Enter keyword")
        return
    
    clear_select_user()

    conn, cursor = createconnection()
    sql = 'SELECT * FROM login '
    if searchby == 'User Name':
        sql = sql + 'WHERE user like ?'
    elif searchby == 'First Name':
        sql = sql + 'WHERE fname like ?'
    elif searchby == 'Last Name':
        sql = sql + 'WHERE lname like ?'
    cursor.execute(sql, [f'%{keyword}%'])
    search_result = cursor.fetchmany(5)
    conn.close()
    
    for child in frame.winfo_children():
        child.destroy()

    if len(search_result) > 0:
        selected_result.set(search_result[0][0])

    for i, item in enumerate(search_result):
        user = item[0]
        pwd = item[1]
        fname = item[2]
        lname = item[3]
        Radiobutton(frame, bg='lightgreen', 
                    text=f'{user} {pwd} {fname} {lname}', 
                    value=user, 
                    variable=selected_result, 
                    command=lambda user = item: select_user(user)).grid(row=i, sticky=W)

def select_user(user):
    print(user)
    spy_update_fullname.set(user[2] + ' ' + user[3])
    spy_update_user.set(user[0])
    spy_update_pwd.set(user[1])
    spy_update_fname.set(user[2])
    spy_update_lname.set(user[3])

def clear_select_user():
    spy_update_fullname.set('')
    spy_update_user.set('')
    spy_update_pwd.set('')
    spy_update_fname.set('')
    spy_update_lname.set('')

def update_profile(user, pwd, fname, lname):
    if user == '':
        return
    conn, cursor = createconnection()
    sql_update = 'UPDATE login SET pwd = ?, fname = ?, lname = ? WHERE user = ?'
    cursor.execute(sql_update, [pwd, fname, lname, user])
    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        messagebox.showinfo("Update Profile", "Updated profile successfully.")
    else:
        messagebox.showerror("Update Profile", "Cound not update profile at the moment.")

def delete_profile(user):
    print(user)

    if user == '':
        return
    
    if not messagebox.askyesno('Confirm?', f'The {user}\'s profile will be deleted permanently'):
        return 

    conn,cursor = createconnection()
    
    sql = "DELETE FROM login WHERE user = ?"

    cursor.execute(sql,[user])
    conn.commit()
    row = cursor.rowcount
    conn.close()


    if row > 0:
        messagebox.showinfo("Delete Profile", "The profile is successfully deleted.")
    else:
        messagebox.showerror("Delete Profile", "Cound not update profile at the moment.")


def manage_users(profile):
    clear_page()
    Label(root,text="User Management",fg='#534340',bg='#8ac4d0',font='Mali 32 bold').grid(row=0,columnspan=4)
    fm_users = Frame(root,bg='#085E7D')
    fm_users.rowconfigure((0,1),weight=1)
    fm_users.columnconfigure((0,1),weight=1)
    fm_users.grid(row=1,column=1,columnspan=2,sticky='news')

    fm_search = LabelFrame(fm_users, text="Search", bg='lightgreen')
    fm_search.rowconfigure(0, weight=1)
    fm_search.rowconfigure(1, weight=2)
    fm_search.grid(row=0, column=0, sticky=NSEW)

    selected_choice = StringVar(value="User Name")
    spy_keyword = StringVar()

    option = OptionMenu(fm_search,selected_choice,"User Name","First Name","Last Name")
    option.grid(row=0,column=0,pady=20,sticky='e')

    entry_searchbox = Entry(fm_search, textvariable=spy_keyword)
    entry_searchbox.grid(row=0, column=1, sticky=EW)
    entry_searchbox.focus_force()

    fm_search_result = Frame(fm_search, height=180, width=500, bg='lightgreen')
    fm_search_result.grid_propagate(False)
    fm_search_result.rowconfigure((0,1,2,3,4), weight=1)
    fm_search_result.columnconfigure(0, weight=1)
    fm_search_result.grid(row=1, columnspan=3, rowspan=5)

    btn_search = Button(fm_search, image=icon_search, command=lambda: get_users(fm_search_result, selected_choice.get(), spy_keyword.get()))
    btn_search.grid(row=0, column=2, sticky=E)

    fm_form = LabelFrame(fm_users, text="Information", bg='yellow')
    fm_form.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
    fm_form.columnconfigure((0,1), weight=1)
    fm_form.grid(row=0, column=1, sticky=NSEW)

    Label(fm_form, text='Name : ', bg='yellow').grid(row=0, column=0, sticky=E)
    Label(fm_form, text='User Name : ', bg='yellow').grid(row=1, column=0, sticky=E)
    Label(fm_form, text='Password : ', bg='yellow').grid(row=2, column=0, sticky=E)
    Label(fm_form, text='First Name : ', bg='yellow').grid(row=3, column=0, sticky=E)
    Label(fm_form, text='Last Name : ', bg='yellow').grid(row=4, column=0, sticky=E)

    global spy_update_fullname, spy_update_user, spy_update_pwd, spy_update_fname, spy_update_lname
    spy_update_fullname = StringVar()
    spy_update_user = StringVar()
    spy_update_pwd = StringVar()
    spy_update_fname = StringVar()
    spy_update_lname = StringVar()
    Label(fm_form, textvariable=spy_update_fullname, bg='yellow').grid(row=0, column=1, sticky=W)
    Label(fm_form, textvariable=spy_update_user, bg='yellow').grid(row=1,  column=1, sticky=W)
    Entry(fm_form, textvariable=spy_update_pwd).grid(row=2,  column=1, sticky=NSEW)
    Entry(fm_form, textvariable=spy_update_fname).grid(row=3,  column=1, sticky=NSEW)
    Entry(fm_form, textvariable=spy_update_lname).grid(row=4,  column=1, sticky=NSEW)
    Button(fm_form,text="Update",width=10,height=1, command=lambda: update_profile(spy_update_user.get(), spy_update_pwd.get(), spy_update_fname.get(), spy_update_lname.get())).grid(row=8,columnspan=2, sticky=EW)
    Button(fm_form,text="Delete",width=10,height=1, command=lambda: delete_profile(spy_update_user.get())).grid(row=9,columnspan=2, sticky=EW)
    Button(fm_users,text="Back",width=10,height=1,command=lambda: welcomepage(profile)).grid(row=1,column=1,pady=10,padx=15,sticky=E)

def edit_profile(profile):
    clear_page()
    Label(root,text="Edit Profile",fg='#534340',bg='#8ac4d0',font='Mali 32 bold').grid(row=0,columnspan=4)
    welcomeframe = Frame(root,bg='#085E7D')
    welcomeframe.rowconfigure((0,1,2,3),weight=1)
    welcomeframe.columnconfigure((0,1),weight=1)    

    spy_firstname = StringVar(value=profile[2])
    spy_lastname = StringVar(value=profile[3])
    username = profile[0]


    Label(welcomeframe,text="First Name : ",bg='#085E7D',fg='white').grid(row=0, column=0)
    lbl_firstname = Entry(welcomeframe,textvariable=spy_firstname,bg='white',fg='#085E7D')
    lbl_firstname.grid(row=0, column=1)
    lbl_firstname.focus_force()

    Label(welcomeframe,text="Last Name : ",bg='#085E7D',fg='white').grid(row=1, column=0)
    lbl_lastname = Entry(welcomeframe,textvariable=spy_lastname,bg='white',fg='#085E7D')
    lbl_lastname.grid(row=1, column=1)

    welcomeframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')


    Button(welcomeframe,text="Update",width=10,height=1,command=lambda: update_profile_name(spy_firstname.get(), spy_lastname.get(), username)).grid(row=4,column=0,pady=10,padx=15,sticky=E)
    Button(welcomeframe,text="Back",width=10,height=1,command=lambda: welcomepage(profile)).grid(row=4,column=1,pady=10,padx=15,sticky=E)


def retrieve_profile(username):
    conn, cursor = createconnection()
    sql_select = "SELECT * FROM login WHERE user = ?"
    cursor.execute(sql_select, [username])
    profile = cursor.fetchone()
    conn.close()
    return profile


#สร้าง function นี้ขึ้นมาเพื่อที่จะให้ admin สามารถเปลี่ยนเป็นชื่อตัวเองได้ 
def update_profile_name(firstname, lastname, username):
    print(firstname, lastname, username)

    conn, cursor = createconnection()
    sql_update = 'UPDATE login SET fname = ?, lname = ? WHERE user = ?'
    cursor.execute(sql_update, (firstname, lastname, username))
    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        messagebox.showinfo("Update Profile", "Updated profile successfully.")
        profile = retrieve_profile(username)
        welcomepage(profile)
    else:
        messagebox.showwarning("Update Profile", "No data changes.")

def clear_page():
    for child in root.winfo_children():
        child.destroy()

conn,cursor = createconnection()
root = mainwindow()


selected_result = StringVar()
search_result = []
icon_search = PhotoImage(file='images/search.png')
img1 = PhotoImage(file='images/profile.png').subsample(5,5)
loginlayout()
root.mainloop()
cursor.close()
conn.close()