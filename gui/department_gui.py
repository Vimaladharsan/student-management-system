import tkinter as tk
from tkinter import messagebox
from dao.department_dao import add_department, get_all_departments, update_department, delete_department

class DepartmentGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Manage Departments")
        self.geometry("400x400")

        tk.Label(self, text="Department Name").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        tk.Button(self, text="Add", command=self.add_department).pack(pady=5)
        tk.Button(self, text="Update", command=self.update_department).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete_department).pack(pady=5)
        tk.Button(self, text="Refresh", command=self.load_departments).pack(pady=5)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.load_departments()

    def load_departments(self):
        self.listbox.delete(0, tk.END)
        self.departments = get_all_departments()
        for dept in self.departments:
            self.listbox.insert(tk.END, f"{dept[0]} - {dept[1]}")

    def add_department(self):
        name = self.name_entry.get()
        if name:
            add_department(name)
            self.load_departments()
            self.name_entry.delete(0, tk.END)

    def update_department(self):
        selected = self.listbox.curselection()
        if selected:
            dept_id = self.departments[selected[0]][0]
            name = self.name_entry.get()
            if name:
                update_department(dept_id, name)
                self.load_departments()
                self.name_entry.delete(0, tk.END)

    def delete_department(self):
        selected = self.listbox.curselection()
        if selected:
            dept_id = self.departments[selected[0]][0]
            delete_department(dept_id)
            self.load_departments()
            self.name_entry.delete(0, tk.END)

    def on_select(self, event):
        selected = self.listbox.curselection()
        if selected:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.departments[selected[0]][1])
