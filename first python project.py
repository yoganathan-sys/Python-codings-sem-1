from tkinter import *
from tkinter import messagebox

FILE_NAME = "students.txt"

# ---------------- Functions ---------------- #

def add_student():
    sid = entry_id.get()
    name = entry_name.get()
    marks = entry_marks.get()

    if sid == "" or name == "" or marks == "":
        messagebox.showerror("Error", "All fields are required")
        return

    with open(FILE_NAME, "a") as f:
        f.write(f"{sid},{name},{marks}\n")

    messagebox.showinfo("Success", "Student Added Successfully")
    clear_fields()

def view_students():
    text_area.delete(1.0, END)
    try:
        with open(FILE_NAME, "r") as f:
            data = f.read()
            if data == "":
                text_area.insert(END, "No Records Found")
            else:
                text_area.insert(END, "ID\tName\tMarks\n")
                text_area.insert(END, "-"*30 + "\n")
                for line in data.splitlines():
                    sid, name, marks = line.split(",")
                    text_area.insert(END, f"{sid}\t{name}\t{marks}\n")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")

def search_student():
    sid = entry_id.get()
    text_area.delete(1.0, END)

    found = False
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == sid:
                    text_area.insert(END, f"ID: {data[0]}\nName: {data[1]}\nMarks: {data[2]}")
                    found = True
                    break
        if not found:
            messagebox.showinfo("Not Found", "Student ID not found")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")

def delete_student():
    sid = entry_id.get()
    lines = []
    deleted = False

    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                if not line.startswith(sid + ","):
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            messagebox.showinfo("Success", "Student Deleted")
        else:
            messagebox.showinfo("Not Found", "Student ID not found")

        clear_fields()
        view_students()

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")

def update_student():
    sid = entry_id.get()
    name = entry_name.get()
    marks = entry_marks.get()

    updated = False
    lines = []

    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(FILE_NAME, "w") as f:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == sid:
                    f.write(f"{sid},{name},{marks}\n")
                    updated = True
                else:
                    f.write(line)

        if updated:
            messagebox.showinfo("Success", "Student Updated")
        else:
            messagebox.showinfo("Not Found", "Student ID not found")

        clear_fields()
        view_students()

    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")

def clear_fields():
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    entry_marks.delete(0, END)

# ---------------- GUI Design ---------------- #

root = Tk()
root.title("Student Management System")
root.geometry("600x500")
root.resizable(False, False)

Label(root, text="Student Management System", font=("Arial", 18, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = Entry(frame)
entry_id.grid(row=0, column=1)

Label(frame, text="Student Name").grid(row=1, column=0, padx=10, pady=5)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

Label(frame, text="Marks").grid(row=2, column=0, padx=10, pady=5)
entry_marks = Entry(frame)
entry_marks.grid(row=2, column=1)

btn_frame = Frame(root)
btn_frame.pack(pady=10)

Button(btn_frame, text="Add", width=10, command=add_student).grid(row=0, column=0, padx=5)
Button(btn_frame, text="View", width=10, command=view_students).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Search", width=10, command=search_student).grid(row=0, column=2, padx=5)
Button(btn_frame, text="Update", width=10, command=update_student).grid(row=0, column=3, padx=5)
Button(btn_frame, text="Delete", width=10, command=delete_student).grid(row=0, column=4, padx=5)

text_area = Text(root, height=12, width=65)
text_area.pack(pady=10)

root.mainloop()
