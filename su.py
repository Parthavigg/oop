from  tkinter import  *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter  import messagebox
import mysql.connector


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\mehull.jpeg")
        lb_bg=Label(self.root,image=self.bg)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=350,y=170,width=320,height=470)

        img1=Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\red.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=450,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Arial",20,"bold"),fg="white",bg="black")
        get_str.place(x=75,y=100)

        """labels for username"""
        username=lb1=Label(frame,text="Username",font=("Arial",15,"bold"),fg="white",bg="black")
        username.place(x=100,y=155)

        self.txtuser=ttk.Entry(frame,font=("Arial",15,"bold"))
        self.txtuser.place(x=100,y=180,width=200)

        password = lb2 = Label(frame, text="Password", font=("Arial", 15, "bold"), fg="white", bg="black")
        password.place(x=100, y=225)

        self.txtpass = ttk.Entry(frame, show="*",font=("Arial", 15, "bold"))
        self.txtpass.place(x=100, y=250, width=200)

        """Icon images"""
        img2 = Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\user3.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2,bg="black", borderwidth=0)
        lblimg2.place(x=350, y=313, width=100, height=100)

        img3 = Image.open(r"C:\Users\Omkar\PycharmProjects\pythonProject3\image\pass1.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=350, y=386, width=100, height=100)

        """login button"""
        loginbtn=Button(frame,command=self.login,text="Login", font=("Arial", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=30)

        """register button"""
        loginbtn = Button(frame, text="Create New Account?",command=self.rigister_window, font=("Arial", 10, "bold"),borderwidth=0, fg="white", bg="black",
                          activeforeground="white", activebackground="black")
        loginbtn.place(x=22, y=350, width=160)
def login(self):
 if self.txtuser.get()=="" or self.txtpass.get()=="":
        messagebox.showerror("Error"," All Field Are Required")
 elif self.txtuser.get()=="mehul" and self.txtpass.get()=="gohil":
        messagebox.showinfo("Success","Success full")
 else:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="ppmehul")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                           ))
        row=my_cursor.fetchone()
        if row==None:
           messagebox.showerror("Error","Invalid Username & password")
        else:
            open_main=messagebox.askyesno("YesNo","Access only admin")
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=student(self.new_window)
            else:
                if not open_main:
                    return
        conn.commit()
        conn.close()


