import tkinter as tk
from tkinter import messagebox, ttk
from dao.teacher_dao import add_teacher, get_all_teachers
from dao.department_dao import get_all_departments

class TeacherGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Manage Teachers")
        self.geometry("600x400")

        tk.Label(self, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Email").grid(row=1, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1)

        tk.Label(self, text="Phone").grid(row=2, column=0)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(self, text="Department").grid(row=3, column=0)
        self.dept_combo = ttk.Combobox(self, state="readonly")
        self.dept_combo.grid(row=3, column=1)

        tk.Button(self, text="Add", command=self.add_teacher).grid(row=4, column=0)
        tk.Button(self, text="Refresh", command=self.load_teachers).grid(row=4, column=1)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.grid(row=5, column=0, columnspan=2, pady=10)

        self.load_departments()
        self.load_teachers()

    def load_departments(self):
        self.departments = get_all_departments()
        self.dept_combo['values'] = [f"{d[0]} - {d[1]}" for d in self.departments]

    def load_teachers(self):
        self.listbox.delete(0, tk.END)
        self.teachers = get_all_teachers()
        for t in self.teachers:
            self.listbox.insert(tk.END, f"{t[0]} - {t[1]} ({t[2]})")

    def add_teacher(self):
        try:
            name = self.name_entry.get()
            email = self.email_entry.get()
            phone = self.phone_entry.get()
            dept_id = int(self.dept_combo.get().split(" - ")[0])
            add_teacher(name,email,phone,dept_id)
            self.load_teachers()
        except Exception as e:
            messagebox.showerror("Error", str(e))
