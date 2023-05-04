from tkinter import *
from tkinter import ttk
from tkinter import  messagebox
from tkinter import Toplevel,messagebox
from tkinter import filedialog
import pip
import pip as PIL
from PIL import Image , ImageTk
from tkinter import messagebox as m_box
from csv import DictWriter
from csv import DictReader
from tkinter.ttk import Treeview
import csv
from csv import writer
import os
import numpy
# import cv2
import random
import datetime
import time;
from time import strftime
class file_App:
    def __init__(self):
        self.root=Tk()
        self.root.title("System")
        self.root.geometry("998x600+200+40")
        self.root.configure(background="#0b9798")
        self.root.resizable(False,False)

        title = Label(self.root,text="PTCL Management System",width=37,relief=RIDGE,bd=2,pady=5,font=("ALGERIAN",32),bg="#0d8888",fg="white")
        title.pack(fill=X)
        # --------->All frames
        detail_farme = Frame(self.root,bd=2,relief=RIDGE,height=400,width=650,bg="#0b9798")
        detail_farme.place(x=20,y=90)

        search_file_frame=Frame(self.root,bd=2,relief=RIDGE,bg="#0b9798")
        search_file_frame.place(x=690,y=90,height=400,width=290)
        
        button_farme = Frame(self.root,bd=2,relief=RIDGE,height=70,width=996,bg="#0b9798")
        button_farme.place(x=1,y=520)

        # -------------------------------   Label   ---------------------------------
        stitle = Label(detail_farme,text="Customer Deatail",font=("Times New Roman",25,"bold"),bg="#0b9798",fg="white")
        stitle.place(x=200,y=15)


        #   -------------------->  All variable
        self.phone_no = StringVar()
        self.name= StringVar()
        self.Port_no = StringVar()
        self.T_cab_pair = StringVar()
        self.DC_NO = StringVar()
        self.M_P = StringVar()
        self.DP_no = StringVar()
        self.DP_pair = StringVar()
        self.Address = StringVar()
        self.contect = StringVar()
        #   -------------------->  All Search variable
        self.search_phone_no_var = StringVar()
        

        phone_no = Label(detail_farme,text="Phone No",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        phone_no.place(x=5,y=80)
        txt_phone=Entry(detail_farme,textvariable =self.phone_no,bd=4,width=12,relief=GROOVE,font=("Bookman Old Style",16))
        txt_phone.place(x=125,y=80)
        name = Label(detail_farme,text="Name",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        name.place(x=315,y=80)
        txt_name=Entry(detail_farme,textvariable =self.name,bd=4,width=12,relief=GROOVE,font=("Bookman Old Style",16))
        txt_name.place(x=465,y=80)

        port_no = Label(detail_farme,text="PORT No",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        port_no.place(x=5,y=130)
        txt_port_no=Entry(detail_farme,textvariable =self.Port_no,bd=5,width=12,relief=GROOVE,font=("Bookman Old Style",16))
        txt_port_no.place(x=125,y=130)
        T_cab_pair = Label(detail_farme,text="T-CAB Pair",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        T_cab_pair.place(x=315,y=130)
        txt_T_cab_pair=Entry(detail_farme,textvariable=self.T_cab_pair,bd=4,width=12,relief=GROOVE,font=("Bookman Old Style",16))
        txt_T_cab_pair.place(x=465,y=130)

        DC_no = Label(detail_farme,text="Cabinet",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        DC_no.place(x=5,y=180)
        DC_no_combo=ttk.Combobox(detail_farme,textvariable =self.DC_NO,width=11,font=("Bookman Old Style",16))
        DC_no_combo["value"]=("C8","C8A","C8B","C9","C9A")
        DC_no_combo.place(x=125,y=180)
        M_P = Label(detail_farme,text="M.P",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        M_P.place(x=315,y=180)
        txt_M_P=Entry(detail_farme,textvariable =self.M_P,width=12,relief=GROOVE,bd=5,font=("Bookman Old Style",16))
        txt_M_P.place(x=465,y=180)
        
        DP_no = Label(detail_farme,text="DP NO",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        DP_no.place(x=5,y=230)
        DP_no_combo=Entry(detail_farme,textvariable =self.DP_no,width=12,relief=GROOVE,bd=5,font=("Bookman Old Style",16))
        DP_no_combo.place(x=125,y=230)
        DP_Pair = Label(detail_farme,text="DP Pair",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        DP_Pair.place(x=315,y=230)
        txt_DP_Pair=Entry(detail_farme,textvariable =self.DP_pair,width=12,relief=GROOVE,bd=5,font=("Bookman Old Style",16))
        txt_DP_Pair.place(x=465,y=230)

        contect = Label(detail_farme,text="Contect No",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        contect.place(x=5,y=280)
        txt_contect=Entry(detail_farme,textvariable =self.contect,bd=5,width=12,relief=GROOVE,font=("Bookman Old Style",16))
        txt_contect.place(x=125,y=280)

        address = Label(detail_farme,text="Address",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        address.place(x=315,y=280)
        txt_address=Entry(detail_farme,textvariable =self.Address,bd=5,width=12,relief=GROOVE,font=("Bookman Old Style",16))
        txt_address.place(x=465,y=280)


        # ================================  Buttons  ==========================================

        btn1 = Button(button_farme,text="Save",pady=5, font=("Times New Roman",18),bg="#097777",fg="white", width=13,activebackground="#076d6d",activeforeground = "white",command = self.Save_data)
        btn1.grid(row=0,column=0,padx=10,pady=10)
        btn2 = Button(button_farme,text="Update" ,pady=5,font=("Times New Roman",18),bg="#097777",fg="white", width=13,activebackground="#076d6d",activeforeground = "white",command=self.update)
        btn2.grid(row=0,column=1,padx=9,pady=10)
        btn3 = Button(button_farme,text="Clear",pady=5, font=("Times New Roman",18),bg="#097777",fg="white", width=13,activebackground="#076d6d",activeforeground = "white",command = self.clear)
        btn3.grid(row=0,column=2,padx=9,pady=10)
        btn4 = Button(button_farme,text="Logout",pady=5, font=("Times New Roman",18),bg="#097777",fg="white", width=13,activebackground="#076d6d",activeforeground = "white",command = self.log_out)
        btn4.grid(row=0,column=3,padx=9,pady=10)
        btn5 = Button(button_farme,text="Exit",pady=5, font=("Times New Roman",18),bg="#097777",fg="white", width=13,activebackground="#076d6d",activeforeground = "white",command = self.exit_fun)
        btn5.grid(row=0,column=4,padx=10,pady=10)
        btn6 = Button(search_file_frame,text="Search",font=("Times New Roman",18,"bold") ,bd=2,width=10,bg="#0b9798",fg="white",command = self.Search_data)
        btn6.place(x=70,y=130)


        # ===============================   Serch frame  ==================================

        ftitle=Label(search_file_frame,text="Search Record",font=("Algerian",25),bg="#0b9798",fg="white")
        ftitle.place(x=10,y=15)
        
        search_phone_no = Label(search_file_frame,text="Phone No",font=("Times New Roman",18,"bold"),bg="#0b9798",fg="white")
        search_phone_no.place(x=15,y=90)
        txt_search_phone_no=Entry(search_file_frame,textvariable =self.search_phone_no_var,bd=5,width=9,relief=GROOVE,font=("Bookman Old Style",14))
        txt_search_phone_no.place(x=135,y=90)

        
        self.root.mainloop()
    


    def Save_data(self):
        if self.phone_no.get()=="" or self.name.get()=="" or self.Port_no.get()=="" or self.T_cab_pair.get()=="" or self.DC_NO.get()=="" or self.M_P.get()=="" or self.DP_no.get()=="" or self.DP_pair.get()=="" or self.Address.get()=="" or self.contect.get()=="":
            messagebox.showerror("Error","please fill all the boxes....")
        else: 
            ph = self.phone_no.get()
            if os.path.exists('My File.csv'):
                with open('My File.csv' , 'r') as f:
                    counter=0
                    rows = csv.reader(f)
                    for row in rows:
                        if ph in row:
                            ask = messagebox.askyesno("information","this number is already saved\n Do you want to Update the data?")
                            if ask>0:
                                counter+=1
                                self.update()
                            else:
                                return 0
                if counter==0:
                    with open("My File.csv","a",newline="") as f:
                        dict_writter = DictWriter(f,fieldnames=['Phone no','Name','Port no','T Cab Pair','DC No','M P','DP no','DP Pair','contect','Address'])
                        if os.stat('My File.csv').st_size==0:
                            dict_writter.writeheader()
                        dict_writter.writerow({
                            'Phone no':self.phone_no.get(),
                            'Name':self.name.get(),
                            'Port no':self.Port_no.get(),
                            'T Cab Pair':self.T_cab_pair.get(),
                            'DC No':self.DC_NO.get(),
                            'M P':self.M_P.get(),
                            'DP no':self.DP_no.get(),
                            'DP Pair':self.DP_pair.get(),
                            'contect':self.contect.get(),
                            'Address':self.Address.get()
                        })
                        messagebox.showinfo("information","Your Data is saved Successfully!!!")
                else:
                    return 0
            else:
                with open("My File.csv","a",newline="") as f:
                    dict_writter = DictWriter(f,fieldnames=['Phone no','Name','Port no','T Cab Pair','DC No','M P','DP no','DP Pair','contect','Address'])
                    if os.stat('My File.csv').st_size==0:
                        dict_writter.writeheader()
                    dict_writter.writerow({
                        'Phone no':self.phone_no.get(),
                        'Name':self.name.get(),
                        'Port no':self.Port_no.get(),
                        'T Cab Pair':self.T_cab_pair.get(),
                        'DC No':self.DC_NO.get(),
                        'M P':self.M_P.get(),
                        'DP no':self.DP_no.get(),
                        'DP Pair':self.DP_pair.get(),
                        'contect':self.contect.get(),
                        'Address':self.Address.get()
                    })
                    messagebox.showinfo("information","Your Data is saved Successfully!!!")
    def Search_data(self):
        ph = self.search_phone_no_var.get()
        with open('My File.csv' , 'r') as f:
            counter=0
            rows = csv.reader(f)
            rough_list=[]
            for row in rows:
                rough_list.append(row)
            my_no = []
            for first in rough_list:
                if ph in first:
                    self.phone_no.set(first[0])
                    self.name.set(first[1])
                    self.Port_no.set(first[2])
                    self.T_cab_pair.set(first[3])
                    self.DC_NO.set(first[4])
                    self.M_P.set(first[5])
                    self.DP_no.set(first[6])
                    self.DP_pair.set(first[7])
                    self.contect.set(first[8])
                    self.Address.set(first[9])
                    
                    counter+=1
            if counter==0:
                messagebox.showerror("Error","Your Phone no is Incorrect\nPlease enter correct no\nTry again....")
            else:
                return 0

    def update(self):
        ph = self.search_phone_no_var.get()
        with open('My File.csv' , 'r') as f:
            rows = csv.reader(f)
            rough_list=[]
            for row in rows:
                rough_list.append(row)
            for first in rough_list:
                if ph in first:
                    first[0] = self.phone_no.get()
                    first[1] = self.name.get()
                    first[2] = self.Port_no.get()
                    first[3] = self.T_cab_pair.get()
                    first[4] = self.DC_NO.get()
                    first[5] = self.M_P.get()
                    first[6] = self.DP_no.get()        
                    first[7] = self.DP_pair.get()
                    first[8] = self.contect.get()
                    first[9] = self.Address.get()
                    
                    with open('My File.csv' , 'w') as f:
                        rows = csv.writer(f,lineterminator="\n")
                        rows.writerows(rough_list)
                        messagebox.showinfo("information","Your Data is Update Successfully!!!")

    def clear(self):
        self.phone_no.set("")
        self.name.set("")
        self.Port_no.set("")
        self.T_cab_pair.set("")
        self.DC_NO.set("")
        self.M_P.set("")
        self.DP_no.set("")
        self.DP_pair.set("")
        self.Address.set("")
        self.contect.set("")

      
    def exit_fun(self):
        ask = messagebox.askyesno("Delete","Do you really want to delete")
        if ask>0:
            self.root.destroy()
            

    def log_out(self):
        self.root.destroy()
        import ptcl_login

