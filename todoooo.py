import sqlite3
from tkinter import *
from tkinter import messagebox
def databse():
    con=sqlite3.connect('tasks.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks(title TEXT ,completed  INTEGER NOT NULL DEFAULT 0 , time INTEGER) ")
    con.commit()
    con.close()

def addtask(title,time):
    con=sqlite3.connect('tasks.db')
    cur=con.cursor()
    cur.execute("INSERT INTO tasks(title,time)VALUES(?,?)",(title,time))
    con.commit()
    con.close()
def deletall():
   con=sqlite3.connect('tasks.db')
   cur=con.cursor()
   cur.execute('''DELETE FROM tasks''')
   con.commit()
   cur.close()
   con.close()
   
def remove(title):
    con=sqlite3.connect('tasks.db')
    cur=con.cursor()
    cur.execute("DELETE  FROM tasks WHERE title = ?",(title,))
    con.commit()
    con.close()
    

def fetch_tasks():
 con=sqlite3.connect('tasks.db')
 cur=con.cursor()
 cur.execute("SELECT title, time FROM tasks")
 results=cur.fetchall()
 con.close()
 return results
 
databse() 

window = Tk()
window.title("to-list")
window.geometry("460x500")
window.resizable(0,0)
icon = PhotoImage(file=r"C:\Users\mehran\Documents\proje_nahayi\todolisttm.py\6194029.png")
window.iconphoto(True,icon)
window.config(background="#3D3533")
labell=Label(window,text="You can do it",font=('arial',24,'bold'),bg='#5F4C48',fg='black')
frame=Frame(window,bg="#5F4C48",width=700,height=200)
selectbox=Listbox(window,selectmode='single',selectbackground='white',selectforeground='black',font=('arial',14),bg="#202C77")
labell.grid()
def get_task():
    selectbox.delete(0,END)
    rows=fetch_tasks()
    for title, time in rows:
        selectbox.insert(END,f"{title}-{time}min")
    selectbox.grid(row=3,column=0,padx=6,pady=6,sticky='we')

frame.grid()
task=[]
def add_button():
   title = title_entry.get().strip()
   if not title:
       messagebox.showinfo('eror','title of task is empty')
       return
   time=time_entry.get().strip()
   if not time:
        messagebox.showinfo('eror','time of task is empty')
        return
   try:
    time=int(time)
   except ValueError:
        messagebox.showinfo('eror','time must  integer')
        return
   addtask(title,time)
   title_entry.delete(0,END)
   time_entry.delete(0, END)
   get_task()

def delete_button():
      if messagebox.askyesno('Delete all?','Are you sure?'):
          task.clear()
          deletall()
          get_task()

def remove_button():
    selected = selectbox.curselection()
    if not selected:
        messagebox.showinfo('eror', 'select task first')
        return

    idx = selected[0]
    text = selectbox.get(idx)  
    title=text.split("-")[0]     
    remove(title)
    selectbox.delete(idx)
          
label1=Label(frame,text='title of task',bg='#5F4C48',font=('arial', 18 ,'bold'))  
label1.grid(row=0,column=0 , padx=(12,50),pady=6,sticky='') 
title_entry=Entry(frame,bg='white',font=('arial','14'))
title_entry.grid(row=0,column=1,padx=(6,20),pady=6,sticky='nsew')
label2=Label(frame,text='time of task',bg='#5F4C48',font=('arial',18 ,'bold'))
label2.grid(row=1,column=0,padx=12,pady=6,sticky='w')
time_entry=Entry(frame,bg='white',font=('arial','14'))
time_entry.grid(row=1,column=1,padx=(6,20),pady=6,sticky='nsew')
button=Button(frame,text="add",font=('arial',10,'bold'),command=add_button,width=12,height=2,bd=3)
button.grid(padx=4,pady=4,row= 2 , sticky='w'  , column=0   )
button=Button(frame,text='delete all',font=('arial',10,'bold'),command=delete_button,width=12,height=2,bd=3)
button.grid(padx=4,pady=4 ,row= 2 , column= 1,sticky='e' )
button=Button(frame,text="remove task",font=('arial',10,'bold'),command=remove_button,width=12,height=2,bd=3)
button.grid(padx=4 ,pady=4,row=2, column= 1,sticky='w')

get_task()
window.mainloop()





