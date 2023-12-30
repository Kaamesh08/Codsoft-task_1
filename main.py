import tkinter as tk

tasks = []

def create_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def update_task():
    selected_task = listbox.curselection()
    if selected_task:
        new_task = entry.get()
        listbox.delete(selected_task)
        listbox.insert(selected_task, new_task)
        entry.delete(0, tk.END)

def display_tasks():
    tasks = listbox.get(0, tk.END)
    if not tasks:
        result_label.config(text="No tasks found.")
    else:
        result_label.config(text="Tasks:\n" + "\n".join(tasks))

# GUI setup
root = tk.Tk()
root.title("To-Do List Manager")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

create_button = tk.Button(root, text="Create Task", command=create_task)
create_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack()

display_button = tk.Button(root, text="Display Tasks", command=display_tasks)
display_button.pack()

listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
