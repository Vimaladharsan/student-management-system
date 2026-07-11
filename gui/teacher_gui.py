import tkinter as tk
from tkinter import ttk, messagebox

from dao.teacher_dao import add_teacher, get_all_teachers
from dao.department_dao import get_all_departments


class TeacherGUI(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Teacher Management")
        self.geometry("900x600")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            self,
            text="Teacher Management",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        form = ttk.LabelFrame(self, text="Teacher Details")
        form.pack(fill="x", padx=20)

        ttk.Label(form, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = ttk.Entry(form, width=35)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(form, text="Email").grid(row=0, column=2, padx=10)
        self.email_entry = ttk.Entry(form, width=35)
        self.email_entry.grid(row=0, column=3)

        ttk.Label(form, text="Phone").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.phone_entry = ttk.Entry(form, width=35)
        self.phone_entry.grid(row=1, column=1)

        ttk.Label(form, text="Department").grid(row=1, column=2, padx=10)
        self.dept_combo = ttk.Combobox(
            form,
            width=32,
            state="readonly"
        )
        self.dept_combo.grid(row=1, column=3)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(button_frame, text="Add", command=self.add_teacher).grid(row=0, column=0, padx=6)
        ttk.Button(button_frame, text="Refresh", command=self.load_teachers).grid(row=0, column=1, padx=6)
        ttk.Button(button_frame, text="Clear", command=self.clear_form).grid(row=0, column=2, padx=6)

        columns = (
            "ID",
            "Name",
            "Email",
            "Phone",
            "Department"
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
        self.tree.column("Name", width=180)
        self.tree.column("Email", width=220)
        self.tree.column("Phone", width=150)
        self.tree.column("Department", width=180)

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)
        scrollbar.place(relx=0.98, rely=0.33, relheight=0.57)

        self.load_departments()
        self.load_teachers()

    def load_departments(self):
        self.departments = get_all_departments()

        self.dept_combo["values"] = [
            f"{d[0]} - {d[1]}"
            for d in self.departments
        ]

    def load_teachers(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.teachers = get_all_teachers()

        for t in self.teachers:

            department = ""

            if len(t) > 4:
                department = t[4]

            email = t[2] if len(t) > 2 else ""
            phone = t[3] if len(t) > 3 else ""

            self.tree.insert(
                "",
                tk.END,
                values=(
                    t[0],
                    t[1],
                    email,
                    phone,
                    department
                )
            )

    def add_teacher(self):

        try:

            dept_id = int(
                self.dept_combo.get().split(" - ")[0]
            )

            add_teacher(
                self.name_entry.get(),
                self.email_entry.get(),
                self.phone_entry.get(),
                dept_id
            )

            messagebox.showinfo(
                "Success",
                "Teacher added successfully."
            )

            self.clear_form()
            self.load_teachers()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def clear_form(self):

        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.dept_combo.set("")