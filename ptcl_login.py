from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("System")
        self.root.geometry("998x600+200+40")
        self.root.configure(background="#0b9798")
        # ---------->
        self.bg = ImageTk.PhotoImage(file="background1.jpg")
        self.bg_image = Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
        #---------->  variables
        self.user=StringVar()
        self.password=StringVar()

        # --------------->  Creat frame
        f1=Frame(self.root,bd=5,relief=RIDGE,bg="#0b9798")
        f1.place(x=380,y=150,width=500,height=300)

        # ------------------->  title Name
        title=Label(f1,text="Login the page",font=('ALGERIAN',33),bg="#0b9798",fg="white")
        title.place(x=80,y=5)


        # --------------------->  Label and entrybox for username and password
        lblusername = Label(f1, text="Username", font=('Times New Roman',23, "bold"),bg="#0b9798",fg="white")
        lblusername.place(x=28, y=80)
        txtuser = Entry(f1,textvariable=self.user ,relief=GROOVE,bd=5,width=25, font=('Times New Roman',15, "bold"))
        txtuser.place(x=174, y=83)
        txtuser.focus()

        lblpass = Label(f1, text="Password", font=('Times New Roman', 23, "bold"),bg="#0b9798",fg="white")
        lblpass.place(x=28, y=140)
        txtpass = Entry(f1, textvariable=self.password ,relief=GROOVE,show="*", bd=5, width=25, font=('Times New Roman',15, "bold"))
        txtpass.place(x=174, y=143)

        btnlog=Button(f1,text="Login",font=("Times New Roman",18),bg="#097777",fg="white",width=8,activebackground="#076d6d",activeforeground = "white",command=self.logfun)
        btnlog.place(x=40,y=215)
        btnreset = Button(f1, text="Reset", font=("Times New Roman",18),bg="#097777",fg="white", width=8,activebackground="#076d6d",activeforeground = "white",command=self.resetfun)
        btnreset.place(x=180, y=215)
        btnexit = Button(f1, text="Exit", font=("Times New Roman",18),bg="#097777",fg="white", width=8,activebackground="#076d6d",activeforeground = "white",command=self.exitfun)
        btnexit.place(x=320, y=215)

    # ---------------->  define function for button
    def logfun(self):
    
        if self.user.get()=="waqas" and self.password.get()=="12345":
            self.root.destroy()
            import ptcl_main
            ptcl_main.file_App()
        else:
            messagebox.showerror("Error" , "Invalid Username or Password")
    # ------------>  Reset function for reset  button
    def resetfun(self):
        self.user.set("")
        self.password.set("")

    # -----------> Exit function for Exti button
    def exitfun(self):
        opt = messagebox.askyesno("Exit","Do you really want to Exit")
        if opt>0:
            self.root.destroy()
        else:
            return


root=Tk()
obj=login(root)
root.mainloop()