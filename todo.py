import tkinter as tk
from tkinter import messagebox

#Add task function
def add_task():
    task =task_entry.get()
    if task != "":
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)
    else:
         messagebox.showwarning("Input Error","Please enter a task.")

#Delete selected task
def delete_task():
 try:
      selected_index = task_listbox.curselection()[0]
      task_listbox.delete(selected_index)
 except  IndexError:
     messagebox.showwarning("Selection Error","Please select a task to delete.")

#GUI Setup
window=tk.Tk()
window.title("To-Do List")
window.geometry("400x400")
window.config(bg="White")

#Heading
title_label = tk.Label(window,text="📝 My To-Do List",font=("Helvetica",20,"bold"),fg="white",bg="black")
title_label.pack(pady=10)

#Task entry
task_entry = tk.Entry(window,width=30,font=("Helvetica",16))
task_entry.pack(pady=10)

#Buttons
add_button = tk.Button(window,text="Add task",width=14,command = add_task)
add_button.pack(pady=5)

delete_button=tk.Button(window,text="Delete Task",width=14,command = delete_task)
delete_button.pack(pady=5)

#listbox to show task
task_listbox = tk.Listbox(window,width =40,height=10,font=("Helvetica",12))
task_listbox.pack(pady=10)


#Start the Gui loop
window.mainloop()



                    
