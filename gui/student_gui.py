import tkinter as tk
from tkinter import ttk, messagebox

from dao.student_dao import (
    add_student,
    get_all_students,
    update_student,
    delete_student
)

from dao.department_dao import get_all_departments


class StudentGUI(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Student Management")
        self.geometry("950x650")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            self,
            text="Student Management",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        form = ttk.LabelFrame(self, text="Student Details")
        form.pack(fill="x", padx=20)

        ttk.Label(form, text="Name").grid(row=0, column=0, padx=10, pady=8, sticky="w")
        self.name_entry = ttk.Entry(form, width=35)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(form, text="Email").grid(row=0, column=2, padx=10)
        self.email_entry = ttk.Entry(form, width=35)
        self.email_entry.grid(row=0, column=3)

        ttk.Label(form, text="Phone").grid(row=1, column=0, padx=10, pady=8, sticky="w")
        self.phone_entry = ttk.Entry(form, width=35)
        self.phone_entry.grid(row=1, column=1)

        ttk.Label(form, text="Department").grid(row=1, column=2, padx=10)
        self.dept_combo = ttk.Combobox(form, width=32, state="readonly")
        self.dept_combo.grid(row=1, column=3)

        ttk.Label(form, text="Date of Birth").grid(row=2, column=0, padx=10, pady=8)
        self.dob_entry = ttk.Entry(form, width=35)
        self.dob_entry.grid(row=2, column=1)

        ttk.Label(form, text="Admitted Year").grid(row=2, column=2, padx=10)
        self.year_entry = ttk.Entry(form, width=35)
        self.year_entry.grid(row=2, column=3)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(button_frame, text="Add", command=self.add_student).grid(row=0, column=0, padx=6)
        ttk.Button(button_frame, text="Update", command=self.update_student).grid(row=0, column=1, padx=6)
        ttk.Button(button_frame, text="Delete", command=self.delete_student).grid(row=0, column=2, padx=6)
        ttk.Button(button_frame, text="Refresh", command=self.load_students).grid(row=0, column=3, padx=6)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).grid(row=0, column=4, padx=6)

        columns = (
            "ID",
            "Name",
            "Email",
            "Phone",
            "Department",
            "DOB",
            "Year"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Name", width=170)
        self.tree.column("Email", width=200)
        self.tree.column("Phone", width=120)
        self.tree.column("Department", width=150)
        self.tree.column("DOB", width=110)
        self.tree.column("Year", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)
        scrollbar.place(relx=0.98, rely=0.34, relheight=0.54)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.load_departments()
        self.load_students()

    def load_departments(self):
        self.departments = get_all_departments()
        self.dept_combo["values"] = [
            f"{d[0]} - {d[1]}"
            for d in self.departments
        ]

    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.students = get_all_students()

        for s in self.students:

            department = ""

            if len(s) > 5:
                department = s[5]

            self.tree.insert(
                "",
                tk.END,
                values=(
                    s[0],
                    s[1],
                    s[2],
                    s[3],
                    department,
                    s[6],
                    s[7]
                )
            )

    def add_student(self):

        try:

            dept_id = int(
                self.dept_combo.get().split(" - ")[0]
            )

            add_student(
                self.name_entry.get(),
                self.email_entry.get(),
                self.phone_entry.get(),
                dept_id,
                self.dob_entry.get(),
                int(self.year_entry.get())
            )

            messagebox.showinfo(
                "Success",
                "Student added successfully."
            )

            self.clear_form()
            self.load_students()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def update_student(self):

        selected = self.tree.selection()

        if not selected:
            return

        student_id = self.tree.item(selected[0])["values"][0]

        try:

            dept_id = int(
                self.dept_combo.get().split(" - ")[0]
            )

            update_student(
                student_id,
                self.name_entry.get(),
                self.email_entry.get(),
                self.phone_entry.get(),
                dept_id,
                self.dob_entry.get(),
                int(self.year_entry.get())
            )

            messagebox.showinfo(
                "Success",
                "Student updated successfully."
            )

            self.clear_form()
            self.load_students()

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_student(self):

        selected = self.tree.selection()

        if not selected:
            return

        if not messagebox.askyesno(
            "Confirm",
            "Delete selected student?"
        ):
            return

        student_id = self.tree.item(selected[0])["values"][0]

        delete_student(student_id)

        messagebox.showinfo(
            "Deleted",
            "Student deleted successfully."
        )

        self.clear_form()
        self.load_students()

    def clear_form(self):

        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.dept_combo.set("")

    def on_select(self, event):

        selected = self.tree.selection()

        if not selected:
            return

        index = self.tree.index(selected[0])

        s = self.students[index]

        self.clear_form()

        self.name_entry.insert(0, s[1])
        self.email_entry.insert(0, s[2])
        self.phone_entry.insert(0, s[3])
        self.dob_entry.insert(0, s[6])
        self.year_entry.insert(0, s[7])

        dept_id = s[4]

        for i, dept in enumerate(self.departments):
            if dept[0] == dept_id:
                self.dept_combo.current(i)
                break