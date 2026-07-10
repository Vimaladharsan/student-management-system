import tkinter as tk
from tkinter import messagebox, ttk
from dao.student_dao import add_student, get_all_students, update_student, delete_student
from dao.department_dao import get_all_departments

class StudentGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Manage Students")
        self.geometry("600x500")

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

        tk.Label(self, text="DOB (YYYY-MM-DD)").grid(row=4, column=0)
        self.dob_entry = tk.Entry(self)
        self.dob_entry.grid(row=4, column=1)

        tk.Label(self, text="Admitted Year").grid(row=5, column=0)
        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=5, column=1)

        tk.Button(self, text="Add", command=self.add_student).grid(row=6, column=0)
        tk.Button(self, text="Update", command=self.update_student).grid(row=6, column=1)
        tk.Button(self, text="Delete", command=self.delete_student).grid(row=6, column=2)
        tk.Button(self, text="Refresh", command=self.load_students).grid(row=6, column=3)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.grid(row=7, column=0, columnspan=4, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.load_departments()
        self.load_students()

    def load_departments(self):
        self.departments = get_all_departments()
        self.dept_combo['values'] = [f"{d[0]} - {d[1]}" for d in self.departments]

    def load_students(self):
        self.listbox.delete(0, tk.END)
        self.students = get_all_students()
        for s in self.students:
            self.listbox.insert(tk.END, f"{s[0]} - {s[1]} ({s[2]})")

    def add_student(self):
        try:
            name = self.name_entry.get()
            email = self.email_entry.get()
            phone = self.phone_entry.get()
            dept_id = int(self.dept_combo.get().split(" - ")[0])
            dob = self.dob_entry.get()
            year = int(self.year_entry.get())
            add_student(name,email,phone,dept_id,dob,year)
            self.load_students()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        selected = self.listbox.curselection()
        if selected:
            student_id = self.students[selected[0]][0]
            try:
                name = self.name_entry.get()
                email = self.email_entry.get()
                phone = self.phone_entry.get()
                dept_id = int(self.dept_combo.get().split(" - ")[0])
                dob = self.dob_entry.get()
                year = int(self.year_entry.get())
                update_student(student_id,name,email,phone,dept_id,dob,year)
                self.load_students()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def delete_student(self):
        selected = self.listbox.curselection()
        if selected:
            student_id = self.students[selected[0]][0]
            delete_student(student_id)
            self.load_students()

    def on_select(self, event):
        selected = self.listbox.curselection()
        if selected:
            s = self.students[selected[0]]

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, s[1])

            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, s[2])

            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, s[3])

            dept_id = s[4]
            for i, dept in enumerate(self.departments):
                if dept[0] == dept_id:
                    self.dept_combo.current(i)
                    break

            self.dob_entry.delete(0, tk.END)
            self.dob_entry.insert(0, s[6])

            self.year_entry.delete(0, tk.END)
            self.year_entry.insert(0, s[7])
