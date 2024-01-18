
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import re
import tkinter


import psycopg2

####################################################    for window

root = tk.Tk()
root.title('RegForm.com - login App')
root.geometry("1020x500")





def GetValue(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

    row_id =Listbox.selection()[0]
    select = Listbox.set(row_id)

    e1.insert(0,select['id'])
    e2.insert(0,select['stname'])
    e3.insert(0,select['course'])
    e4.insert(0,select['fee'])
    e5.insert(0,select['email'])


    ##################################################          ADD

def Add():
    
    
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    studemail = e5.get()

    try:
        

                #       All fields required.

        if studid == "" or studname == "" or coursename == "" or feee == "" or studemail == "":
            msg = messagebox.showinfo("information","All Fields Requireds...!!")
            return msg

        else:
                        
                        #     use for email pattern

            pattern = re.compile(r'[\w._%+-]{1,20}\w{3}@[\w.-]{2,20}.[A-Za-z]{2,3}')
            result = pattern.match(studemail)

            if (result):   

                conn = psycopg2.connect(host="localhost", user="postgres",password="12345%", dbname="postgres")
                print("Connect to the Database.")
                cur = conn.cursor()

                        #        if i enter dublicate id it will show massage box.

                if studid == id:

                    try:
                        sql = "INSERT INTO student_record (id,stname,course,fee,email) VALUES (%s,%s,%s,%s,%s)"
                        val = (studid,studname,coursename,feee,studemail)
                        cur.execute(sql,val)
                        conn.commit()

                        lastid = cur.lastrowid
                        messagebox.showinfo("information","Record inserted successfully...")

                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)

                        e1.focus_set()
                    except Exception as e:
                        print(e)
                        conn.rollback()
                        conn.close()
                
                else:

                    try:
                        sql = "INSERT INTO student_record (id,stname,course,fee,email) VALUES (%s,%s,%s,%s,%s)"
                        val = (studid,studname,coursename,feee,studemail)
                        cur.execute(sql,val)
                        conn.commit()

                        lastid = cur.lastrowid
                        messagebox.showinfo("information","Record inserted successfully...")

                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)

                        e1.focus_set()

                    except Exception as e:
                        print(e)
                        msg = messagebox.showwarning("information","Student Id already exists..!!")
                        return msg
                        conn.rollback()
                        conn.close()

                
       
                    

            else:
                msg = messagebox.showwarning("information","Email pattern is wrong...!! Exp: Xyz123@abc.com")
                return msg
       

    except:
            msg = messagebox.showwarning("information","Invalid DataType ..!!")
            return msg    
    
    ####################################################        Update

def update():
        

    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    studemail = e5.get()


    try:
        

        if studid == "" or studname == "" or coursename == "" or feee == "" or studemail == "":
            msg = messagebox.showinfo("information","All Fields Requireds...!!")
            return msg

        else:

                #   use for email pattern
                
            pattern = re.compile(r'[\w._%+-]{1,20}\w{3}@[\w.-]{2,20}.[A-Za-z]{2,3}')
            result = pattern.match(studemail)

            if (result): 
                conn = psycopg2.connect(host="localhost", user="postgres",password="12345%", dbname="postgres")
                print("Connect to the Database.")
                cur = conn.cursor()
                cur.execute("SELECT id,stname,course,fee,email FROM student_record order by id")
                records = cur.fetchall()
                print(records)

                id_list=[]
                for x in records:
                    id_list.append(x[0])
                print (id_list)
                print(type(id_list))

                     
                

                if studid not in id_list:
                    print(studid,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    try:
                    
                        sql = "UPDATE student_record set stname = %s,course = %s,fee = %s,email = %s where id = %s"
                        val = (studname,coursename,feee,studemail,studid)
                        cur.execute(sql,val)
                        conn.commit()

                        lastid = cur.lastrowid
                        messagebox.showinfo("information","Record Updated successfully...")
                        
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e5.delete(0,END)
                    
                    except Exception as e:
                        print(e)
                        messagebox.showinfo("information","Record already exist..!!")
                        conn.rollback()
                        conn.close()

                elif studid in id_list:   
                    msg = messagebox.showinfo("information","Student Id does not exist in Database..!!")
                    return msg

            else:
                msg = messagebox.showwarning("information","Email pattern is wrong...!! Exp: Xyz123@abc.com")
                return msg 
                                
    except:
        msg = messagebox.showwarning("information","Student Id alread exist..!!")
        return msg



    

#############################################################       Delete

def delete():
    studid = e1.get()

 #       All fields required.

    if studid == "":
        msg = messagebox.showinfo("information","All Fields Requireds...!!")
        return msg

    else:
   
        if studid == "" :
            msg = messagebox.showinfo("information","Student Id Fields Requireds...!!")
            return msg

        else: 
            
            conn = psycopg2.connect(host="localhost", user="postgres" ,password="12345%", dbname="postgres")
            print("Connect to the Database.")
            cur = conn.cursor()

            try:
                sql = "delete from student_record where id = %s"
                val = (studid,)
                cur.execute(sql,val)
                conn.commit()

                lastid = cur.lastrowid
                messagebox.showinfo("information","Record Delete successfully...")
                
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)

                e1.focus_set()
            except Exception as e:
                print(e)
                conn.rollback()
                conn.close()

###################################### 2nd show function & 1st create function should ON.

def refresh():         #  show
    
    conn = psycopg2.connect(host="localhost", user="postgres",password="12345%", dbname="postgres")
    print("Connect to the Database.")
    cur = conn.cursor()
    cur.execute("SELECT id,stname,course,fee,email FROM student_record order by id")
    records = cur.fetchall()
    print(records)

    

   

#############################################            For only once run # refresh button.

    if len(records) != 0:
        Listbox.delete(*Listbox.get_children())
        for row in records:
            Listbox.insert('',END,values = row)
        conn.close()

    
##############################################################          Exit the window

def exit():
    exit = tkinter.messagebox.askyesno("Pgadmin Connection","Confirm if you want to exit..!!")
    if exit > 0:
        root.destroy()
        return





#######################################################    For field



global e1
global e2
global e3
global e4
global e5

tk.Label(root, text="Student Registation",fg="black", font=(None,30)).place(x=480,y=30)

tk.Label(root, text="Student ID").place(x=10,y=10)
Label(root, text="Student Name").place(x=10,y=40)
Label(root, text="Course").place(x=10,y=70)
Label(root, text="Fee").place(x=10,y=100)
Label(root, text="Email").place(x=10,y=130)


e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)

Button(root, text="Add", command =Add, height=3, width=13).place(x=30,y=160)
Button(root, text="update", command =update, height=3, width=13).place(x=140,y=160)
Button(root, text="Delete", command =delete, height=3, width=13).place(x=250,y=160)


Button(root, text="Refresh",command=refresh,height=3, width=13).place(x=670,y=160)

Button(root, text="Exit", command=exit,height=3, width=13).place(x=780,y=160)


cols = ('id','stname','course','fee','email')
Listbox = ttk.Treeview(root, columns =cols, show='headings')


for col in cols:
    Listbox.heading(col, text=col)
    Listbox.grid(row=1,column=0,columnspan =2)
    Listbox.place(x=10, y=230)

#show()
Listbox.bind('<Double-Button-1>', GetValue)

root.mainloop()

