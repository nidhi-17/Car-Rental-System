from tkinter import *
from PIL import Image, ImageTk
from email.mime.text import MIMEText
from tkcalendar import *
import mysql.connector
from io import BytesIO
from tkinter import messagebox
import smtplib, ssl
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from werkzeug.security import check_password_hash, generate_password_hash


datas = []

class LoginPage:
    #global Edata
    def __init__(self):
        self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="#Mahakali1972",
                autocommit = True
            )
        print("Database connected")
        self.mycursor2 = self.mydb.cursor()
        global screen
        global username
        global password
        global username_entry
        global password_entry
        global name1
        global name2
        screen = Tk()
        # centre opening
        window_height = 590
        window_width = 630
        screen_width = screen.winfo_screenwidth()
        screen_height = screen.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        screen.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        frame1 = Frame(screen, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
        frame1.place(x=0, y=1, height=590, width=630)

        frame2 = Frame(screen, bg="#FFFFFF", highlightthickness=0, highlightbackground="#FFFFFF")
        frame2.place(x=4, y=6, height=577, width=622)

        # colour
        L2 = Label(frame2, height=4, width=91, bg="#1569C7")
        L2.grid(row=0, column=0, sticky=W)
        username = StringVar(frame2)
        password = StringVar(frame2)
        list1 = ['User', 'Admin']
        c = StringVar(frame2)
        c.set(' User : ')
        droplist = OptionMenu(frame2, c, *list1)
        droplist.config(font=("Comic Sans MS", 12), bg="#FFFFFF", width=15)
        droplist.grid(row=1, column=0, padx=220, pady=50, sticky=W)

        usernameLabel = Label(frame2, font=("Comic Sans MS", 12), text="Username :", bg="#FFFFFF")
        usernameLabel.grid(row=2, column=0, padx=180, pady=5, sticky=W)
        name1 = StringVar()
        self.username_entry = Entry(frame2, font=("Comic Sans MS", 12), textvariable=name1)
        self.username_entry.grid(row=2, column=0, padx=280, pady=10, sticky=W)
        passwdlabel = Label(frame2, font=("Comic Sans MS", 12), text="Password :", bg="#FFFFFF")
        passwdlabel.grid(row=3, column=0, padx=180, pady=5, sticky=W)
        name2 = StringVar()
        self.password_entry = Entry(frame2, textvariable=name2, font=12, show="*", width=18)
        self.password_entry.grid(row=3, column=0, padx=280, pady=10, sticky=W)
        button1 = Button(frame2, font=("Comic Sans MS", 12), text="login", bg="#FFFFFF",command=self.button_login).grid(row=4, column=0, padx=280, pady=10, sticky=W)
        new_userLabel = Label(frame2, font=("Comic Sans MS", 12), bg="#FFFFFF", text="New User?").grid(row=5, column=0, padx=260, pady=10, sticky=W)
        button2 = Button(frame2, font=("Comic Sans MS", 12), text="Click here to Register", command=self.register,bg="#FFFFFF").grid(row=6, column=0, padx=220, pady=10, sticky=W)
        screen.mainloop()

    def button_login(self):
        us = self.username_entry.get()
        pw = self.password_entry.get()
        datas.append(us)
        #Edata = us
        if (us == 'Admin' and pw == '123'):
            screen.withdraw()
            AdminPage()

        elif (us == '' and pw == ''):
            messagebox.showerror("Oops !", "Blank Not allowed")

        else:
            print("End")

        queryy = """SELECT pass FROM mp.customer WHERE Email_ID = %s"""
        self.mycursor2.execute(queryy, (us,))
        Vpass = self.mycursor2.fetchone()
        for i in Vpass:
            mm = check_password_hash(i, pw)
            print(Vpass)
            if mm:
                screen.withdraw()
                Upage = UserPage()
                Upage.Layout1()
        # if (us == '' and pw == ''):
        #     messagebox.showinfo("", "Blank Not allowed")
        # elif (us == 'Admin' and pw == '123'):
        #     screen.withdraw()
        #     AdminPage()
        # elif (us == check_password_hash(*Vpass)):
        #     screen.withdraw()
        #     Upage = UserPage()
        #     Upage.Layout1()
        # else:
        #     messagebox.showerror("Oops !", "Incorrent Username and Password")

    def register_user(self):
        # screen.destroy()
        f = First_Name.get()
        l = Last_Name.get()
        A = Age.get()
        M = Mobile_No.get()
        E = Email_ID.get()
        Ad = Address.get()
        com1 = self.pass1En.get()
        com2 = self.pass2En.get()
        if com1 == com2 :
            try:
                pass_hash = generate_password_hash(com1)
                self.connection = mysql.connector.connect(host='localhost',
                                                          database='mp',
                                                          user='root',
                                                          password='#Mahakali1972')
                mySql_insert_query = """INSERT INTO Customer( f_name,l_name,Mobile_No,Email_ID,Address,Age,pass)VALUES (%s, %s, %s,%s, %s, %s,%s)"""

                self.cursor = self.connection.cursor()
                self.cursor.execute(mySql_insert_query, (f, l, M, E, Ad, A, pass_hash))
                self.connection.commit()
                print(self.cursor.rowcount, "Record inserted successfully into Customer table")
                self.cursor.close()
                #screen.withdraw()
                LoginPage()
            except mysql.connector.Error as error:
                print("Failed to insert record into Customer table {}".format(error))

            Last_Name_entry.delete(0, END)
            Age_entry.delete(0, END)
            Mobile_no_entry.delete(0, END)
            Email_Id_entry.delete(0, END)
            Address_entry.delete(0, END)
        else:
            messagebox.showerror("Oops !","Passwards don't match. Please try again !")

    def register(self):

        global screen1
        screen1 = Toplevel(screen)
        screen1.title("Registration Page")
        window_height = 590
        window_width = 630
        screen_width = screen.winfo_screenwidth()
        screen_height = screen.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        screen1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        frame3 = Frame(screen1, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
        frame3.place(x=0, y=1, height=590, width=630)

        frame4 = Frame(screen1, bg="#FFFFFF", highlightthickness=0, highlightbackground="#FFFFFF")
        frame4.place(x=4, y=6, height=577, width=622)

        # colour
        L3 = Label(frame4, height=4, width=91, bg="#1569C7")
        L3.grid(row=0, column=0, sticky=W)

        global First_Name
        global Last_Name
        global Age
        global Mobile_No
        global Email_ID
        global Address
        global otp
        global First_Name_entry
        global Last_Name_entry
        global Age_entry
        global Mobile_no_entry
        global Email_Id_entry
        global Address_entry
        global otp_entry
        First_Name = StringVar()
        Last_Name = StringVar()
        Age = IntVar()
        Mobile_No = IntVar()
        Email_ID = StringVar()
        Address = StringVar()
        Details=Label(frame4, text="Please Fill The Details Below", font=("Comic Sans MS", 15), bg="#FFFFFF")
        Details.grid(row=1,column=0,padx=190,pady=10,sticky=W)
        Fname = Label(frame4, text="First Name *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        Fname.grid(row=2, column=0, padx=170,pady=10,sticky=W)
        First_Name_entry = Entry(frame4, font=("Comic Sans MS", 12), textvariable=First_Name)
        First_Name_entry.grid(row=2, column=0, padx=290, pady=10, sticky=W)
        Lname=Label(frame4, text="Last Name *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        Lname.grid(row=3, column=0, pady=10, padx=170, sticky=W)
        Last_Name_entry = Entry(frame4, font=("Comic Sans MS", 12), textvariable=Last_Name)
        Last_Name_entry.grid(row=3, column=0, pady=10, padx=290, sticky=W)
        UserAge=Label(frame4, text="Age *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        UserAge.grid(row=4, column=0, pady=10, padx=215, sticky=W)
        Age_entry = Entry(frame4, font=("Comic Sans MS", 12), textvariable=Age)
        Age_entry.grid(row=4, column=0, pady=10, padx=290, sticky=W)
        Mobile=Label(frame4, text="Mobile No. *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        Mobile.grid(row=5, column=0, pady=10, padx=160, sticky=W)
        Mobile_no_entry = Entry(frame4, font=("Comic Sans MS", 12), textvariable=Mobile_No)
        Mobile_no_entry.grid(row=5, column=0, pady=10, padx=290, sticky=W)
        Email=Label(frame4, text="Email ID *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        Email.grid(row=6, column=0, pady=10, padx=175, sticky=W)
        Email_Id_entry = Entry(frame4, font=("Comic Sans MS", 12), textvariable=Email_ID)
        Email_Id_entry.grid(row=6, column=0, pady=10, padx=290, sticky=W)
        Addr=Label(frame4, text="Address *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        Addr.grid(row=7, column=0, pady=10, padx=180, sticky=W)
        Address_entry = Entry(frame4, font=("Comic Sans MS", 12), textvariable=Address)
        Address_entry.grid(row=7, column=0, pady=10, padx=290)
        # passward
        self.str1 = StringVar()
        pass1 = Label(frame4, text="Passward *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        pass1.grid(row=8, column=0, pady=10, padx=180, sticky=W)
        self.pass1En = Entry(frame4, font=("Comic Sans MS", 12), textvariable=self.str1, show="*")
        self.pass1En.grid(row=8, column=0, pady=10, padx=290)
        # confirm passward
        self.str2 = StringVar()
        pass2 = Label(frame4, text="Confirm Passward *", font=("Comic Sans MS", 12), bg="#FFFFFF")
        pass2.grid(row=9, column=0, pady=10, padx=120, sticky=W)
        self.pass2En = Entry(frame4, font=("Comic Sans MS", 12), textvariable=self.str2, show="*")
        self.pass2En.grid(row=9, column=0, pady=10, padx=290)

        Butt=Button(frame4, text="Register", width=10, height=1, font=("Comic Sans MS", 12), bg="#FFFFFF", command=self.register_user)
        Butt.grid(row=10, column=0, pady=20, padx=280, sticky=W)
        screen.mainloop()

class UserPage(LoginPage):
    def __init__(self):
        try:
            # objL = LoginPage
            # print(objL.username_entry.get())
            # print(objL.button_login(self).username_entry.get())
            self.mydb = mysql.connector.connect (
                    host="localhost",
                    user="root",
                    password="#Mahakali1972"
                )
            print("Database connected")
            self.mycursor = self.mydb.cursor()
            print("Hi")
        except Exception as e:
            print(e)

    def Layout1(self):
        self.root = Toplevel()
        # root.eval('tk::PlaceWindow . Center')
        self.root.title("Welcome !")

        # centre opening
        window_height = 690
        window_width = 630

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        frame1 = Frame(self.root, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
        frame1.place(x=0, y=1, height=690, width=630)

        frame2 = Frame(self.root, bg="#FFFFFF", highlightthickness=0, highlightbackground="#FFFFFF")
        frame2.place(x=4, y=6, height=677, width=622)

        # colour
        self.L2 = Label(frame2, height=4, width=91, bg="#1569C7")
        self.L2.grid(row=0, column=0, sticky=W)

        Pimage = Image.open("profilePic.PNG")
        Pimage = Pimage.resize((40, 40), Image.ANTIALIAS)
        PFimg = ImageTk.PhotoImage(Pimage)
        # profile
        profile = Menubutton(frame2, image = PFimg, relief="flat")
        profile.grid(row=0, column=0, padx=545, pady=1, sticky=W)

        # submenu
        submenu1 = Menu(profile, fg='black', font=("Comic Sans MS", 15), relief="flat", tearoff=0, bd=4)
        profile.config(menu=submenu1)

        def log():
            self.root.withdraw()
            LoginPage()
        def detail():
            newWindow_aa = Toplevel(self.root)
            newWindow_aa.title("Details")
            window_height = 451
            window_width = 450

            screen_width = newWindow_aa.winfo_screenwidth()
            screen_height = newWindow_aa.winfo_screenheight()

            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))

            newWindow_aa.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            frame1 = Frame(newWindow_aa, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
            frame1.place(x=0, y=1, height=450, width=450)

            frame2 = Frame(newWindow_aa, bg="white", highlightthickness=0, highlightbackground="#FFFFFF")
            frame2.place(x=4, y=6, height=440, width=440)

            # colour
            L2 = Label(frame2, height=4, width=91, bg="#1569C7")
            L2.grid(row=0, column=0, sticky=W)

            #labels containing info
            DetailData = "SELECT * FROM mp.customer WHERE Email_ID = %s"
            self.mycursor.execute(DetailData,(datas[0],))
            DD = self.mycursor.fetchall()
            for De in DD:
                L3 = Label(frame2, text="First Name : {}".format(De[1]), bg="white", font=("Comic Sans MS", 15))
                L3.grid(row=1, column=0, sticky=W, padx=20, pady=10)
                L4 = Label(frame2, text="Last Name : {}".format(De[2]), bg="white", font=("Comic Sans MS", 15))
                L4.grid(row=2, column=0, sticky=W, padx=20, pady=10)
                L5 = Label(frame2, text="Mobile Number : {}".format(De[3]), bg="white", font=("Comic Sans MS", 15))
                L5.grid(row=3, column=0, sticky=W, padx=20, pady=10)
                L6 = Label(frame2, text="Email ID : {}".format(De[4]), bg="white", font=("Comic Sans MS", 15))
                L6.grid(row=4, column=0, sticky=W, padx=20, pady=10)
                L7 = Label(frame2, text="Address : {}".format(De[5]), bg="white", font=("Comic Sans MS", 15))
                L7.grid(row=5, column=0, sticky=W, padx=20, pady=10)
                L8 = Label(frame2, text="Age : {}".format(De[6]), bg="white", font=("Comic Sans MS", 15))
                L8.grid(row=6, column=0, sticky=W, padx=20, pady=10)

        def Orders():
            root1 = Tk()
            # root.eval('tk::PlaceWindow . Center')
            root1.title("Bookings")

            # centre opening
            window_height = 690
            window_width = 630

            screen_width = root1.winfo_screenwidth()
            screen_height = root1.winfo_screenheight()

            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))

            root1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            frame1 = Frame(root1, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
            frame1.place(x=0, y=1, height=690, width=630)

            frame2 = Frame(root1, bg="#FFFFFF", highlightthickness=0, highlightbackground="#FFFFFF")
            frame2.place(x=4, y=6, height=677, width=622)

            # colour
            L2 = Label(frame2, height=4, width=91, bg="#1569C7")
            L2.grid(row=0, column=0, sticky=W)

            LF1 = LabelFrame(frame2, bg="white", highlightthickness=0, highlightbackground="#5C5858", bd=5,
                             relief="ridge")
            LF1.place(x=40, y=90, height=560, width=543)

            C1 = Canvas(LF1, height=530, width=515, highlightthickness=3, highlightbackground="white", bg="#FFFFFF")
            C1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

            self.frame3 = Frame(C1, bg="white", highlightthickness=0, highlightbackground="#FFFFFF")
            self.frame3.place(x=6, y=6, height=525, width=510)

            sb1 = Scrollbar(LF1, orient="vertical", command=C1.yview)
            sb1.grid(row=1, column=0, sticky=N + S, padx=490, pady=140)

            '''self.mycursor.execute("SELECT car_no, car_name, Rate FROM mp.car")

            myresult2 = self.mycursor.fetchall()
            for i in myresult2:
                print(i)'''

            self.frame3.bind("<Configure>", lambda p: C1.configure(scrollregion=C1.bbox("all")))
            C1.create_window((0, 0), window=self.frame3, anchor="nw")
            C1.config(yscrollcommand=sb1.set)

            stat = "SELECT booking.Book_id , booking.P_Time , booking.P_Loc ,booking.from_d1,booking.To_d2 FROM mp.booking, mp.customer WHERE booking.Customer_cust_id = customer.cust_id"
            self.mycursor.execute(stat)
            dats = self.mycursor.fetchall()
            a = 1
            j = 1
            k = j + 1
            l = k + 1
            m = l + 1
            n = m + 1
            label = list(range(len(dats)))
            print(len(dats))
            for th in dats:
                Label(self.frame3, text=str(a) + ".", font=("Comic Sans MS", 15), bg="#FFFFFF", height=5, width=5).grid(
                    row=j,
                    column=0,
                    padx=5,
                    pady=5)
                Label(self.frame3, text="Book ID : {}".format(th[0]), font=("Comic Sans MS", 15), bg="#FFFFFF").grid(row=j, column=2,
                                                                                                        padx=5,
                                                                                                        pady=5)
                Label(self.frame3, text="Pick up Time : {}".format(th[1]), font=("Comic Sans MS", 15), bg="#FFFFFF").grid(
                    row=k, column=2,
                    padx=5,
                    pady=5)
                Label(self.frame3, text="Location : {}".format(th[2]), font=("Comic Sans MS", 15),
                      bg="#FFFFFF").grid(row=l, column=2,
                                         padx=5,
                                         pady=5)

                Label(self.frame3, text="From Date : {}".format(th[3]), font=("Comic Sans MS", 15),
                      bg="#FFFFFF").grid(row=m, column=2,
                                         padx=5,
                                         pady=5)
                Label(self.frame3, text="To Date : {}".format(th[4]), font=("Comic Sans MS", 15),
                      bg="#FFFFFF").grid(row=n, column=2,
                                         padx=5,
                                         pady=5)


                j = j + 6
                k = k + 6
                l = l + 6
                m = m + 6
                n = n + 6
                a = a + 1

        def reset():
            newWindow_bb = Toplevel(self.root)
            newWindow_bb.title("Passward Reset")
            window_height = 351
            window_width = 350

            screen_width = newWindow_bb.winfo_screenwidth()
            screen_height = newWindow_bb.winfo_screenheight()

            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))

            newWindow_bb.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            frame1 = Frame(newWindow_bb, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
            frame1.place(x=0, y=1, height=350, width=350)

            frame2 = Frame(newWindow_bb, bg="white", highlightthickness=0, highlightbackground="#FFFFFF")
            frame2.place(x=4, y=6, height=340, width=340)

            # colour
            L2 = Label(frame2, height=4, width=91, bg="#1569C7")
            L2.grid(row=0, column=0, sticky=W)

            L3 = Label(frame2, text="Passward : ", bg="white", font=("Comic Sans MS", 15))
            L3.grid(row=1, column=0, sticky=W, padx=20, pady=10)
            txt11 = StringVar()
            TL3 = Entry(frame2, bg="white", font=("Comic Sans MS", 15), textvariable=txt11, width=15, show="*")
            TL3.grid(row=1, column=0, sticky=W, padx=150, pady=10)

            L4 = Label(frame2, text="Re-Enter : ", bg="white", font=("Comic Sans MS", 15))
            L4.grid(row=2, column=0, sticky=W, padx=20, pady=10)
            txt12 = StringVar()
            TL4 = Entry(frame2, bg="white", font=("Comic Sans MS", 15), textvariable=txt12, width=15, show="*")
            TL4.grid(row=2, column=0, sticky=W, padx=150, pady=10)

            def RB1(txt1,txt2):
                if txt1 == txt2 :
                    hashp = generate_password_hash(txt1)
                    print(hashp)
                    query = "UPDATE mp.customer SET pass = %s WHERE Email_ID = %s"
                    self.mycursor.execute(query, (hashp, datas[0],))
                    self.mydb.commit()
                    print("done")
                    messagebox.showinfo("Success", "Passward changed")
                else:
                    messagebox.showerror("Oops !", "Passwards don't match please try again")


            RButton = Button(frame2, text="Change Passward", bg="white", font=("Comic Sans MS", 15), command=lambda:RB1(txt11.get(),txt12.get()))
            RButton.grid(row=3, column=0, sticky=W, padx=80, pady=10)

        #cotents
        Rdata="SELECT f_name FROM mp.customer WHERE Email_ID = %s"
        self.mycursor.execute(Rdata,(datas[0],))
        RK = self.mycursor.fetchone()
        for kk in RK:
            submenu1.add_command(label="      {}      ".format(kk.capitalize()), compound="center")
            submenu1.add_separator()
            submenu1.add_command(label="Details", compound="center", command=detail)
            # submenu1.add_separator()
            submenu1.add_command(label="Bookings", compound="center", command=Orders)
            # submenu1.add_separator()
            submenu1.add_command(label="Reset passward", compound="center", command=reset)
            submenu1.add_separator()
            submenu1.add_command(label="Log out", compound="center", command=log)


        # title
        self.L3 = Label(frame2, text="Fill In The Information", font=("Comic Sans MS", 20, "bold"), bg="#FFFFFF")
        self.L3.grid(row=1, column=0, sticky=W, pady=10, padx=165)

        # seats
        self.L4 = Label(frame2, text="No of seats :", font=("Comic Sans MS", 15), bg="#FFFFFF")
        self.L4.grid(row=2, column=0, sticky=W, padx=140, pady=3)
        # txtbox

        self.seats = StringVar()

        self.txt1 = Entry(frame2, textvariable=self.seats, font=('Comic Sans MS', 15, 'normal'), borderwidth=3, relief="sunken")
        self.txt1.grid(row=2, column=0, sticky=W, padx=280, pady=3)

        # Date
        self.L5 = Label(frame2, text="Date", font=("Comic Sans MS", 15, "bold"), bg="#FFFFFF")
        self.L5.grid(row=3, column=0, sticky=W, padx=120, pady=3)

        # from
        self.L6 = Label(frame2, text="From :", font=("Comic Sans MS", 15), bg="#FFFFFF")
        self.L6.grid(row=4, column=0, sticky=W, padx=185, pady=3)
        self.cal1 = DateEntry(frame2, selectmode="day", year=2021, month=5, day=6, width=18, locale='en_US',
                         date_pattern='dd/mm/yyyy', font=("Comic Sans MS", 15))
        self.cal1.grid(row=4, column=0, sticky=W, padx=283, pady=3)

        # to
        self.L7 = Label(frame2, text="To :", font=("Comic Sans MS", 15), bg="#FFFFFF")
        self.L7.grid(row=5, column=0, sticky=W, padx=210, pady=3)
        self.cal2 = DateEntry(frame2, selectmode="day", year=2021, month=5, day=6, width=18, locale='en_US',
                         date_pattern='dd/mm/yyyy', font=("Comic Sans MS", 15))
        self.cal2.grid(row=5, column=0, sticky=W, padx=283, pady=5)

        # time
        self.L8 = Label(frame2, text="Time", font=("Comic Sans MS", 15, "bold"), bg="#FFFFFF")
        self.L8.grid(row=6, column=0, sticky=W, padx=120, pady=3)

        # pick-up
        self.L9 = Label(frame2, text="Pickup Time :", font=("Comic Sans MS", 15), bg="#FFFFFF")
        self.L9.grid(row=7, column=0, sticky=W, padx=120, pady=3)
        self.time = StringVar()
        self.txt3 = Entry(frame2, textvariable=self.time, font=('Comic Sans MS', 15, 'normal'), borderwidth=3, relief="sunken")
        self.txt3.grid(row=7, column=0, sticky=W, padx=280, pady=3)

        # location
        self.L10 = Label(frame2, text="Location", font=("Comic Sans MS", 15, "bold"), bg="#FFFFFF")
        self.L10.grid(row=8, column=0, sticky=W, padx=120, pady=3)

        # Area
        self.L11 = Label(frame2, text="Area :", font=("Comic Sans MS", 15), bg="#FFFFFF")
        self.L11.grid(row=9, column=0, sticky=W, padx=190, pady=3)
        self.time1 = StringVar()
        self.txt3 = Entry(frame2, textvariable=self.time1, font=('Comic Sans MS', 15, 'normal'), borderwidth=3, relief="sunken")
        self.txt3.grid(row=9, column=0, sticky=W, padx=280, pady=3)

        # choice
        self.L12 = Label(frame2, text="Any preferred car ?", font=("Comic Sans MS", 15), bg="#FFFFFF")
        self.L12.grid(row=10, column=0, sticky=W, padx=110, pady=5)
        # radio buttons
        self.L13 = Label(frame2, text="Enter name :", font=("Comic Sans MS", 15), bg="#FFFFFF")
        self.name = StringVar()
        self.txt4 = Entry(frame2, textvariable=self.name, font=('Comic Sans MS', 15, 'normal'), borderwidth=3, relief="sunken")

        self.i = IntVar()
        self.R1 = Radiobutton(frame2, text="Yes", value=1, variable=self.i, command=self.Radio1, bg="#FFFFFF",
                              font=("Comic Sans MS", 15),
                              borderwidth=3)
        self.R1.grid(row=10, column=0, sticky=W, padx=300, pady=8)

        self.R2 = Radiobutton(frame2, text="No", value=2, variable=self.i, bg="#FFFFFF", font=("Comic Sans MS", 15), borderwidth=3,
                              command=self.Radio1)
        self.R2.grid(row=10, column=0, sticky=W, padx=380, pady=8)

        def Button1():
            self.root.withdraw()
            K = UserPage()
            K.Layout2(self.i.get(), self.seats.get(), self.time1.get(), self.name.get(), self.time.get(), self.cal1.get(), self.cal2.get())

        # search button
        self.B1 = Button(frame2, text="Search", font=('Comic Sans MS', 15, 'normal'), borderwidth=10, relief="raised",
                    command=Button1)
        self.B1.grid(row=12, column=0, sticky=W, padx=265, pady=30)

        self.root.mainloop()
        self.mydb.close()
        print("Database disconnected")

    def Layout2(self,Rnum,S1,CL,CN,pickup, date1, date2):
        root1 = Tk()
        # root.eval('tk::PlaceWindow . Center')
        root1.title("Welcome !")

        # centre opening
        window_height = 690
        window_width = 630

        screen_width = root1.winfo_screenwidth()
        screen_height = root1.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        root1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        frame1 = Frame(root1, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
        frame1.place(x=0, y=1, height=690, width=630)

        frame2 = Frame(root1, bg="#FFFFFF", highlightthickness=0, highlightbackground="#FFFFFF")
        frame2.place(x=4, y=6, height=677, width=622)

        # colour
        L2 = Label(frame2, height=4, width=91, bg="#1569C7")
        L2.grid(row=0, column=0, sticky=W)


        LF1 = LabelFrame(frame2, bg="white", highlightthickness=0, highlightbackground="#5C5858", bd=5, relief="ridge")
        LF1.place(x=40, y=90, height=560, width=543)

        C1 = Canvas(LF1, height=530, width=515, highlightthickness=3, highlightbackground="white", bg="#FFFFFF")
        C1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.frame3 = Frame(C1, bg="white", highlightthickness=0, highlightbackground="#FFFFFF")
        self.frame3.place(x=6, y=6, height=525, width=510)

        sb1 = Scrollbar(LF1, orient="vertical", command=C1.yview)
        sb1.grid(row=1, column=0, sticky=N + S, padx=490, pady=140)

        '''self.mycursor.execute("SELECT car_no, car_name, Rate FROM mp.car")

        myresult2 = self.mycursor.fetchall()
        for i in myresult2:
            print(i)'''

        self.frame3.bind("<Configure>", lambda p: C1.configure(scrollregion=C1.bbox("all")))
        C1.create_window((0, 0), window=self.frame3, anchor="nw")
        C1.config(yscrollcommand=sb1.set)

        if Rnum == 1:
            sql1 = "SELECT * FROM mp.car WHERE no_of_seats = %s and car_location = %s and car_name=%s"
            val = (S1, CL, CN,)
            self.mycursor.execute(sql1, val)
            data1 = self.mycursor.fetchall()
            a=1
            j = 1
            k = j + 1
            l = k + 1
            m = l + 1
            n = m + 1
            label = list(range(len(data1)))
            print(len(data1))
            pic = 0
            for i in data1:
                image = Image.open(BytesIO(i[5]))
                img = ImageTk.PhotoImage(image, width = 100, height = 100, master = self.frame3)



                Label(self.frame3, text=str(a) + ".", font=("Comic Sans MS", 15), bg="#FFFFFF", height=5, width=5).grid(row=j,
                                                                                                             column=0,
                                                                                                             padx=5,
                                                                                                             pady=5)
                label[pic] = Label(self.frame3, image=img, bg="#FFFFFF")
                label[pic].image = img
                label[pic].grid(row=j, column=2, padx=20, pady=10)
                Label(self.frame3, text="Description :", font=("Comic Sans MS", 15), bg="#FFFFFF").grid(row=k, column=2,
                                                                                                       padx=5,
                                                                                                       pady=5)
                Label(self.frame3, text=str(i[1]), font=("Comic Sans MS", 15), bg="#FFFFFF").grid(
                    row=l, column=2,
                    padx=5,
                    pady=5)
                Label(self.frame3, text="Rate : " + str(i[3]) +"/- per day", font=("Comic Sans MS", 15), bg="#FFFFFF").grid(row=m, column=2,
                                                                                                   padx=5,
                                                                                                   pady=5)
                def Info(name, loc, d1, d2, time, rate):
                    queryyB2 = """SELECT cust_id FROM mp.customer WHERE Email_ID = %s"""
                    self.mycursor.execute(queryyB2, (datas[0],))
                    VpassB2 = self.mycursor.fetchone()
                    for rr in VpassB2:
                        query11 = "INSERT INTO mp.booking (P_Time,P_Loc,from_d1,To_d2, Customer_cust_id) VALUES (%s,%s,%s,%s,%s)"
                        val11 = (time, loc, d1, d2, rr)
                        self.mycursor.execute(query11, val11)
                        self.mydb.commit()
                        print("Done")
                        print("executed")
                    print("executed")
                    port = 587  # For starttls
                    smtp_server = "smtp.gmail.com"
                    sender_email = "pythonmp2@gmail.com"
                    receiver_email = datas[0]
                    password = "python12@"
                    print(password)
                    msg = MIMEText('We are pleased to inform you that your booking is confirmed.'
                                   '\nPlease check the following information.'
                                   '\nYou booked {} available in {}.'
                                   '\nCar needed from {} to {}.'
                                   '\nPickup Time : {}.'
                                   '\nRate per day : {}'.format(name, loc, d1, d2, time, rate))

                    msg['Subject'] = 'Booking Confirmation'
                    msg['From'] = 'Car Rental System'
                    msg['To'] = 'sanjana2001b18@gmail.com'

                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.starttls(context=context)
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, msg.as_string())
                        print("Mail sent")
                        messagebox.showinfo("Confirmation", "A booking confirmation mail has been sent to your Email Id.")
                        root1.withdraw()
                        obj = UserPage()
                        obj.Layout1()
                Button(self.frame3, text="Book now", font=("Comic Sans MS", 15), bg="#FFFFFF", command=lambda: Info(i[1], CL, date1, date2, pickup, i[3])).grid(row=n, column=2, padx=5,
                                                                                                                  pady=5)
                j = j + 6
                k = k + 6
                l = l + 6
                m = m + 6
                n = n + 6
                a = a + 1
                pic = pic +1
        elif Rnum == 2:
            sql1 = "SELECT * FROM mp.car WHERE no_of_seats = %s and car_location = %s"
            val = (S1, CL,)
            self.mycursor.execute(sql1, val)
            data1 = self.mycursor.fetchall()
            a = 1
            j = 1
            k = j + 1
            l = k + 1
            m = l + 1
            n = m + 1
            label = list(range(len(data1)))
            print(len(data1))
            pic = 0
            for i in data1:

                Label(self.frame3, text=str(a) + ".", font=("Comic Sans MS", 15), bg="#FFFFFF", height=5, width=5).grid(row=j,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
                image = Image.open(BytesIO(i[5]))
                img = ImageTk.PhotoImage(image, width=100, height=100, master=self.frame3)

                label[pic] = Label(self.frame3, image=img, bg="#FFFFFF")
                label[pic].image = img
                label[pic].grid(row=j, column=2, padx=20, pady=10)
                Label(self.frame3, text="Description :", font=("Comic Sans MS", 15), bg="#FFFFFF").grid(row=k, column=2, padx=5, pady=2)
                Label.image = img
                Label(self.frame3, text=str(i[1]), font=("Comic Sans MS", 15), bg="#FFFFFF").grid(
                    row=l, column=2,
                    padx=5,
                    pady=5)

                Label(self.frame3, text="Rate : " + str(i[3]) + "/- per day", font=("Georgia", 15), bg="#FFFFFF").grid(
                    row=m, column=2,
                    padx=5,
                    pady=5)

                def Info(name, loc, d1, d2, time, rate):
                    print(loc,d1,d2,time)
                    queryyB = """SELECT cust_id FROM mp.customer WHERE Email_ID = %s"""
                    self.mycursor.execute(queryyB, (datas[0],))
                    VpassB = self.mycursor.fetchone()
                    for rr in VpassB:
                        query11 = "INSERT INTO mp.booking (P_Time,P_Loc,from_d1,To_d2, Customer_cust_id) VALUES (%s,%s,%s,%s,%s)"
                        val11 = (time, loc, d1, d2,rr)
                        self.mycursor.execute(query11, val11)
                        self.mydb.commit()
                        print("Done")
                        print("executed")
                    port = 587  # For starttls
                    smtp_server = "smtp.gmail.com"
                    sender_email = "pythonmp2@gmail.com"
                    receiver_email = datas[0]
                    password = "python12@"
                    print(password)
                    msg = MIMEText('We are pleased to inform you that your booking is confirmed.'
                                   '\nPlease check the following information.'
                                   '\nYou booked {} available in {}.'
                                   '\nCar needed from {} to {}.'
                                   '\nPickup Time : {}.'
                                   '\nRate per day : {}'.format(name, loc, d1, d2, time, rate))

                    msg['Subject'] = 'Booking Confirmation'
                    msg['From'] = 'Car Rental System'
                    msg['To'] = 'sanjana2001b18@gmail.com'

                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.starttls(context=context)
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, msg.as_string())
                        print("Mail sent")
                        messagebox.showinfo("Confirmation", "A booking confirmation mail has been sent to your Email Id.")
                        root1.withdraw()
                        obj = UserPage()
                        obj.Layout1()
                Button(self.frame3, text="Book now", font=("Comic Sans MS", 15), bg="#FFFFFF", command=lambda: Info(i[1], CL, date1, date2, pickup, i[3])).grid(row=n, column=2, padx=5,
                                                                                              pady=5)
                j = j + 6
                k = k + 6
                l = l + 6
                m = m + 6
                n = n + 6
                a = a + 1
                pic = pic + 1
        else:
            messagebox.showerror("Oops !", "Please enter valid details.")

        root1.mainloop()
        self.mydb.close()
        print("Database disconnected")

    def Radio1(self):
        print(self.i.get())
        if self.i.get() == 1:
            self.L13.grid(row=11, column=0, sticky=W, padx=125, pady=3)
            self.txt4.grid(row=11, column=0, sticky=W, padx=280, pady=3)
        else:
            self.L13.grid_remove()
            self.txt4.grid_remove()

    '''def talk(self, text):
        engine.say(text)
        engine.runAndWait(0)
        return'''

class AdminPage:
    def __init__(self):
        self.mydb = mysql.connector.connect (
                host="localhost",
                user="root",
                password="#Mahakali1972",
                autocommit=True
            )
        print("Database connected")
        self.mycursor = self.mydb.cursor()
        # root.eval('tk::PlaceWindow . Center')
        self.root1 = Tk()
        self.root1.title("Car Booking and Details")

        # centre opening
        window_height = 560
        window_width = 540

        screen_width = self.root1.winfo_screenwidth()
        screen_height = self.root1.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.root1.geometry("{}x{}+{}+{}".format(window_width,
                                            window_height, x_cordinate, y_cordinate))
        frame1 = Frame(self.root1, bg="#5C5858", highlightthickness=0,
                       highlightbackground="#5C5858")
        frame1.place(x=0, y=1, height=560, width=540)

        frame2 = Frame(self.root1, bg="#FFFFFF", highlightthickness=0,
                       highlightbackground="#FFFFFF")
        frame2.place(x=4, y=6, height=550, width=530)

        # colour
        L2 = Label(frame2, height=4, width=91, bg="#1569C7")
        L2.grid(row=0, column=0, sticky=W)

        LF1 = LabelFrame(frame2, bg="white", highlightthickness=0,
                         highlightbackground="#5C5858", bd=5, relief="ridge")
        LF1.place(x=30, y=90, height=380, width=470)

        C1 = Canvas(LF1, height=352, width=443, highlightthickness=3,
                    highlightbackground="white", bg="#FFFFFF")
        C1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # lbl=Label(C1,text="hello",bg="red")
        # lbl.place(x=0,y=10,height=40,width=150)

        # lbl1=Label(C1,text="hello",bg="pink")
        # lbl1.place(x=0,y=45,height=40,width=150)

        frame3 = Frame(C1, bg="white", highlightthickness=0,
                       highlightbackground="#FFFFFF")
        frame3.place(x=6, y=6, height=525, width=550)

        Pimage = Image.open("profilePic.PNG")
        Pimage = Pimage.resize((40, 40), Image.ANTIALIAS)
        PFimg = ImageTk.PhotoImage(Pimage, master=frame2)
        # profile
        profile = Menubutton(frame2, image=PFimg, relief="flat")
        profile.grid(row=0, column=0, padx=480, pady=1, sticky=W)

        # submenu
        submenu1 = Menu(profile, fg='black', font=("Comic Sans MS", 15), relief="flat", tearoff=0, bd=4)
        profile.config(menu=submenu1)

        def log():
            self.root1.withdraw()
            LoginPage()

        def detail():
            newWindow_aa = Toplevel(self.root1)
            newWindow_aa.title("Details")
            window_height = 451
            window_width = 450

            screen_width = newWindow_aa.winfo_screenwidth()
            screen_height = newWindow_aa.winfo_screenheight()

            x_cordinate = int((screen_width / 2) - (window_width / 2))
            y_cordinate = int((screen_height / 2) - (window_height / 2))

            newWindow_aa.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
            frame1 = Frame(newWindow_aa, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
            frame1.place(x=0, y=1, height=450, width=450)

            frame2 = Frame(newWindow_aa, bg="white", highlightthickness=0, highlightbackground="#FFFFFF")
            frame2.place(x=4, y=6, height=440, width=440)

            # colour
            L2 = Label(frame2, height=4, width=91, bg="#1569C7")
            L2.grid(row=0, column=0, sticky=W)

            #labels containing info
            DetailData = "SELECT * FROM mp.admin WHERE admin_id = 1 "
            self.mycursor.execute(DetailData)
            DD = self.mycursor.fetchall()
            for De in DD:
                L3 = Label(frame2, text="First Name : {}".format(De[1]), bg="white", font=("Comic Sans MS", 15))
                L3.grid(row=1, column=0, sticky=W, padx=20, pady=10)
                L4 = Label(frame2, text="Last Name : {}".format(De[2]), bg="white", font=("Comic Sans MS", 15))
                L4.grid(row=2, column=0, sticky=W, padx=20, pady=10)
                L5 = Label(frame2, text="Email ID : {}".format(De[3]), bg="white", font=("Comic Sans MS", 15))
                L5.grid(row=3, column=0, sticky=W, padx=20, pady=10)
                L6 = Label(frame2, text="Mobile Number : {}".format(De[4]), bg="white", font=("Comic Sans MS", 15))
                L6.grid(row=4, column=0, sticky=W, padx=20, pady=10)

        Rdata = "SELECT a_fname FROM mp.admin WHERE admin_id = 1"
        self.mycursor.execute(Rdata)
        RK = self.mycursor.fetchone()
        for kk in RK:
            submenu1.add_command(label="      {}      ".format(kk.capitalize()), compound="center")
            submenu1.add_separator()
            submenu1.add_command(label="Details", compound="center", command=detail)
            submenu1.add_command(label="Log out", compound="center", command=log)

        sb1 = Scrollbar(LF1, orient="vertical", command=C1.yview)
        sb1.grid(row=1, column=0, sticky=N + S, padx=440, pady=50)

        frame3.bind("<Configure>", lambda p: C1.configure(scrollregion=C1.bbox("all")))
        C1.create_window((0, 0), window=frame3, anchor="nw")
        C1.config(yscrollcommand=sb1.set)

        Add_b = Button(self.root1)
        Add_b["bg"] = "#efefef"
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        Add_b["font"] = ("Comic Sans MS",15)
        Add_b["fg"] = "#000000"
        Add_b["justify"] = "center"
        Add_b["text"] = "ADD CAR"
        Add_b.place(x=40, y=500, width=112, height=34)
        Add_b["command"] = self.Button_add

        Del_b = Button(self.root1)
        Del_b["bg"] = "#efefef"
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        Del_b["font"] = ("Comic Sans MS",15)
        Del_b["fg"] = "#000000"
        Del_b["justify"] = "center"
        Del_b["text"] = "DELETE CAR"
        Del_b.place(x=190, y=500, width=130, height=34)
        Del_b["command"] = self.Button_del

        Book_b = Button(self.root1)
        Book_b["bg"] = "#efefef"
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        Book_b["font"] = ("Comic Sans MS",15)
        Book_b["fg"] = "#000000"
        Book_b["justify"] = "center"
        Book_b["text"] = "BOOKINGS"
        Book_b.place(x=350, y=500, width=112, height=34)
        Book_b["command"] = self.Button_book

        mydb = mysql.connector.connect(host="localhost", user="root", password="#Mahakali1972")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM mp.car")
        myresult = mycursor.fetchall()
        label = list(range(len(myresult)))
        pic = 0
        i = 1
        try:
            for rows in myresult:
                Label(frame3, text='Sr', bg="#FFFFFF").grid(row=0, column=0, padx=1, pady=5)
                Label(frame3, text='car no', bg="#FFFFFF").grid(row=0, column=1, padx=1, pady=5)
                Label(frame3, text='Name', bg="#FFFFFF").grid(row=0, column=2, padx=1, pady=5)
                Label(frame3, text='Area', bg="#FFFFFF").grid(row=0, column=3, padx=1, pady=5)
                Label(frame3, text='Rate', bg="#FFFFFF").grid(row=0, column=4, padx=1, pady=5)
                Label(frame3, text='Seats', bg="#FFFFFF").grid(row=0, column=5, padx=1, pady=5)
                Label(frame3, text='Image', bg="#FFFFFF").grid(row=0, column=6, padx=1, pady=5)

                Label(frame3, text=str(i) + '.', bg="#FFFFFF").grid(row=i, column=0, padx=1, pady=5)
                Label(frame3, text=rows[0], bg="#FFFFFF").grid(row=i, column=1, padx=1, pady=5)
                Label(frame3, text=rows[1], bg="#FFFFFF").grid(row=i, column=2, padx=1, pady=5)
                Label(frame3, text=rows[2], bg="#FFFFFF").grid(row=i, column=3, padx=1, pady=5)
                Label(frame3, text=rows[3], bg="#FFFFFF").grid(row=i, column=4, padx=1, pady=5)
                Label(frame3, text=rows[4], bg="#FFFFFF").grid(row=i, column=5, padx=1, pady=5)
                try:
                    img = Image.open((BytesIO(rows[5])))
                    img = img.resize((60, 60), Image.ANTIALIAS)
                    phimg = ImageTk.PhotoImage(img, master=frame3)
                    # Label(frame3, image = phimg).grid(row=5,column=0,padx=5,pady=5)
                    label[pic] = Label(frame3, image=phimg, bg="#FFFFFF")
                    label[pic].image = phimg
                    label[pic].grid(row=i, column=6, padx=1, pady=5)
                    Label.image = phimg
                except Exception as e:
                    print(e)
                pic = pic + 1
                i = i + 1

        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if mydb.is_connected():
                mydb.close()
                mycursor.close()
        self.root1.mainloop()

    def Button_add(self):
        self.root1.withdraw()
        global newWindow_a
        newWindow_a = Toplevel(self.root1)
        newWindow_a.title("Add Car")
        window_height = 451
        window_width = 450

        screen_width = newWindow_a.winfo_screenwidth()
        screen_height = newWindow_a.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        newWindow_a.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        frame1 = Frame(newWindow_a, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
        frame1.place(x=0, y=1, height=450, width=450)

        frame2 = Frame(newWindow_a, bg="white", highlightthickness=0, highlightbackground="#FFFFFF")
        frame2.place(x=4, y=6, height=440, width=440)

        # colour
        L2 = Label(frame2, height=4, width=91, bg="#1569C7")
        L2.grid(row=0, column=0, sticky=W)

        # sets the geometry of toplevel
        #newWindow_a.geometry("500x400")
        global Car_no
        global Car_name
        global Car_img
        global Car_loc
        global Car_rate
        global Car_seats
        global Car_img
        Car_no = tk.StringVar()
        Car_name = tk.StringVar()
        Car_loc = tk.StringVar()
        Car_rate = tk.IntVar()
        Car_seats = tk.IntVar()
        Car_img = tk.StringVar()

        l1 = Label(frame2, text="Car number", width=12, bg="white")
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        l1["font"] = ft
        self.e1 = tk.Entry(frame2, textvariable=Car_no, width=25)
        l1.place(x=50, y=80)
        self.e1.place(x=200, y=85)

        l2 = Label(frame2, text="Car name", width=8, bg="white")
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        l2["font"] = ft
        self.e2 = tk.Entry(frame2, textvariable=Car_name, width=25)
        l2.place(x=60, y=120)
        self.e2.place(x=200, y=125)

        l3 = Label(frame2, text="Car Location", width=12, bg="white")
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        l3["font"] = ft
        self.e3 = tk.Entry(frame2, textvariable=Car_loc, width=25)
        l3.place(x=54, y=160)
        self.e3.place(x=200, y=165)

        l4 = Label(frame2, text="Rate", width=8, bg="white")
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        l4["font"] = ft
        self.e4 = tk.Entry(frame2, textvariable=Car_rate, width=25)
        l4.place(x=46, y=200)
        self.e4.place(x=200, y=205)

        l5 = Label(frame2, text="no of seats", width=10, bg="white")
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        l5["font"] = ft
        self.e5 = tk.Entry(frame2, textvariable=Car_seats, width=25)
        l5.place(x=55, y=240)
        self.e5.place(x=200, y=245)

        l6 = Label(frame2, text="Image", width=8, bg="white")
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        l6["font"] = ft
        self.e6 = tk.Entry(frame2, textvariable=Car_img, width=25)
        l6.place(x=52, y=280)
        self.e6.place(x=200, y=285)

        b7 = Button(frame2, text="Add")
        ft = tkFont.Font(family='Comic Sans MS', size=13)
        b7["font"] = ft
        b7["command"] = self.back_page1
        b7.place(x=200, y=325)

        b8 = Button(frame2, text="Back")
        ft = tkFont.Font(family='Comic Sans MS', size=13)
        b8["font"] = ft
        b8["command"] = self.back_page1
        b8.place(x=195, y=380)

        newWindow_a.mainloop()

    def back_page1(self):
        self.root1.destroy()
        AdminPage()


    def add_car(self):
        global Car_noa
        global Car_namea
        global Car_imga
        global Car_loca
        global Car_ratea
        global Car_seatsa
        global Car_imga
        Car_noa = self.e1.get()
        Car_namea = self.e2.get()
        Car_loca = self.e3.get()
        Car_ratea = self.e4.get()
        Car_seatsa = self.e5.get()
        Car_imga = self.e6.get()

        myconn = mysql.connector.connect(host="localhost", user="root", password="sanjana")
        mycursor = myconn.cursor()

        insert_query = """INSERT INTO mp.car (car_no,car_name,car_location,Rate,no_of_seats,car_pic,Admin_admin_id) 
                                        VALUES (%s,%s, %s,%s,%s,%s,%s) """
        # Convert digital data to binary format
        # with open(Car_imga, 'rb') as file:
        #     car_img_bin = file.read()

        record = (Car_noa, Car_namea, Car_loca, Car_ratea, Car_seatsa, Car_imga, 1)
        try:
            # executing the sql command
            mycursor.execute(insert_query, record)
            # commit changes in database
            myconn.commit()
            #    Car_name.delete('','end')
            #    Car_no.delete(0,'end')
            #    Car_loc.delete('','end')
            #    Car_rate.delete(0,'end')
            #    Car_seats.delete(0,'end')
            #    Car_img.delete('','end')
            newWindow_a.withdraw()
            messagebox.showinfo("success", "Stored successfully")
            AdminPage()
        except Exception as e:
            print(e)

    #    myconn.rollback()
    #    myconn.close()

    def Button_del(self):
        self.root1.withdraw()
        global Car_nob
        Car_nob = tk.StringVar()
        # Car_name=tk.StringVar()
        # Car_loc=tk.StringVar()
        # Car_rate=tk.IntVar()
        # Car_seats=tk.IntVar()
        # Car_img=tk.StringVar()

        global newWindow_b
        newWindow_b = Toplevel(self.root1)
        newWindow_b.title("Delete Car")
        window_height = 351
        window_width = 350

        screen_width = newWindow_b.winfo_screenwidth()
        screen_height = newWindow_b.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        newWindow_b.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        frame1 = Frame(newWindow_b, bg="#5C5858", highlightthickness=0, highlightbackground="#5C5858")
        frame1.place(x=0, y=1, height=350, width=350)

        frame2 = Frame(newWindow_b, bg="white", highlightthickness=0, highlightbackground="#FFFFFF")
        frame2.place(x=4, y=6, height=340, width=340)

        # colour
        L2 = Label(frame2, height=4, width=91, bg="#1569C7")
        L2.grid(row=0, column=0, sticky=W)


        # sets the geometry of toplevel
        #newWindow_b.geometry("500x500")

        l1 = Label(newWindow_b, text="Car number", width=12, bg="white")
        ft = tkFont.Font(family='Comic Sans MS', size=10)
        l1["font"] = ft
        self.e11 = Entry(newWindow_b, textvariable=Car_nob, width=25)
        l1.place(x=45, y=120)
        self.e11.place(x=180, y=120)

        # l2=Label(newWindow_b,text="Car name",width=8,bg="white")
        # ft = tkFont.Font(family='Comic Sans MS',size=10)
        # l2["font"] = ft
        # e2=tk.Entry(newWindow_b,textvariable=Car_name,width=25)
        # l2.place(x=50,y=70)
        # e2.place(x=170,y=70)

        # l3=Label(newWindow_b,text="Car Location",width=12,bg="white")
        # ft = tkFont.Font(family='Comic Sans MS',size=10)
        # l3["font"] = ft
        # e3=tk.Entry(newWindow_b,textvariable=Car_loc,width=25)
        # l3.place(x=50,y=110)
        # e3.place(x=170,y=110)

        # l4=Label(newWindow_b,text="Rate",width=8,bg="white")
        # ft = tkFont.Font(family='Comic Sans MS',size=10)
        # l4["font"] = ft
        # e4=tk.Entry(newWindow_b,textvariable=Car_rate,width=25)
        # l4.place(x=50,y=150)
        # e4.place(x=170,y=150)

        # l5=Label(newWindow_b,text="no of seats",width=10,bg="white")
        # ft = tkFont.Font(family='Comic Sans MS',size=10)
        # l5["font"] = ft
        # e5=tk.Entry(newWindow_b,textvariable=Car_seats,width=25)
        # l5.place(x=50,y=190)
        # e5.place(x=170,y=190)

        # l6=Label(newWindow_b,text="Image",width=8,bg="white")
        # ft = tkFont.Font(family='Comic Sans MS',size=10)
        # l6["font"] = ft
        # e6=tk.Entry(newWindow_b,textvariable=Car_img,width=25)
        # l6.place(x=50,y=230)
        # e6.place(x=170,y=230)

        b7 = Button(frame2, text="Delete")
        ft = tkFont.Font(family='Comic Sans MS', size=15)
        b7["font"] = ft
        b7["command"] = self.del_car
        b7.place(x=120, y=210)

        b8 = Button(newWindow_b, text="Back")
        ft = tkFont.Font(family='Comic Sans MS', size=13)
        b8["font"] = ft
        b8["command"] = self.back_page2
        b8.place(x=128, y=280)

        newWindow_b.mainloop()

    def back_page2(self):
        self.root1.destroy()
        AdminPage()

    def del_car(self):
        Car_nob1 = self.e11.get()
        # Car_namea=Car_name.get()
        # Car_loca=Car_loc.get()
        # Car_ratea=Car_rate.get()
        # Car_seatsa=Car_seats.get()
        # Car_imga=Car_img.get()

        myconn = mysql.connector.connect(host="localhost", user="root", password="sanjana")
        mycursor = myconn.cursor()
        statmt = "DELETE FROM mp.car WHERE car_no = %s"

        try:
            # executing the sql command
            mycursor.execute(statmt, (Car_nob1,))
            # commit changes in database
            myconn.commit()
            #    Car_name.delete(0,'end')
            #    Car_no.delete(0,'end')
            #    Car_loc.delete(0,'end')
            #    Car_rate.delete(0,'end')
            #    Car_seats.delete(0,'end')
            #    Car_img.delete(0,'end')
            messagebox.showinfo("success", "Deleted successfully")
            newWindow_b.withdraw()
            AdminPage()
        except:
            myconn.rollback()

        myconn.close()

    def Button_book(self):
        global newWindow_c
        newWindow_c = Toplevel(self.root1)
        #newWindow_c.geometry("700x400")
        newWindow_c.title("Bookings")
        window_height = 400
        window_width = 700

        screen_width = newWindow_c.winfo_screenwidth()
        screen_height = newWindow_c.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        newWindow_c.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        treev = ttk.Treeview(newWindow_c, selectmode='browse')

        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(newWindow_c, orient="vertical", command=treev.yview)

        # Calling pack method w.r.to verical
        verscrlbar.pack(side='right', fill='x')

        # Constructing horizontal scrollbar
        # with treeview
        horzscrlbar = ttk.Scrollbar(newWindow_c, orient="horizontal", command=treev.xview)

        # Calling pack method w.r.to horizontal
        horzscrlbar.pack(side='bottom', fill='x')

        # Configuring treeview
        treev.configure(yscrollcommand=verscrlbar.set)
        treev.configure(xscrollcommand=horzscrlbar.set)

        # Defining number of columns
        treev["columns"] = ("1", "2", "3", "4", "5", "6")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=100, anchor='c')
        treev.column("2", width=134, anchor='se')
        treev.column("3", width=120, anchor='se')
        treev.column("4", width=100, anchor='c')
        treev.column("5", width=100, anchor='se')
        treev.column("6", width=200, anchor='se')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="Booking ID")
        treev.heading("2", text="Pickup time")
        treev.heading("3", text="Pickup Location")
        treev.heading("4", text="start date")
        treev.heading("5", text="end date")
        treev.heading("6", text="customer ID")

        mydb = mysql.connector.connect(host="localhost", user="root", password="#Mahakali1972")

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM mp.booking")

        myresult = mycursor.fetchall()

        i = 0
        for ro in myresult:
            treev.insert("", END, text='', values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
            i = i + 1
        # Calling pack method w.r.to treeview
        s = ttk.Style()
        s.configure(treev, rowheight=500)
        treev.pack(side='right')
        mydb.close()

LoginPage()