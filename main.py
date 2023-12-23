import tkinter
from tkinter import *

root = Tk()
root.title("My Everyday To-Do List")
root.resizable(True,True)
root.geometry("500x500+400+100")

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)
    if task :
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
def openTaskFile():
    try:
        global task_list
        with open('tasklist.txt','r') as taskfile:
         tasks = taskfile.readlines()

        for task in tasks:
          if task !='\n':
            task_list.append(task)
            listbox.insert(END,task)
    except:
        file = open('tasklist.txt','w')
        file.close()

ImageIcon = PhotoImage(file="Untitled.png")
root.iconphoto(False,ImageIcon)

topBar = Frame(root,width=500,height=100,bg="#307065")
topBar.place(x=0,y=0)

heading = Label(root,text="EVERYDAY TO-DO TASKS",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=100,y=20)

frame = Frame(root,width=500,height=50,bg="#405060")
frame.place(x=0,y=100)

task = StringVar()
task_entry = Entry(frame,width=25,font="arial 20",bd=0)
task_entry.place(x=30,y=7)
task_entry.focus()

button = Button(frame,text="Add",font="arial 20 bold",width=4,bg="#5a95ff",fg="#aaa",bd=0,command=addTask)
button.place(x=410,y=3)

#ListBox
frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=("Arial",12),width=380,height=12,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
delete_Button = Button(root,text="Delete",width=4,height=1,bg="#306075",fg="#302033",command=deleteTask)
delete_Button.place(x=200,y=420)

root.mainloop()