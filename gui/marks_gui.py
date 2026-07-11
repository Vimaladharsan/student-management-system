import tkinter as tk
from tkinter import ttk, messagebox

from dao.mark_dao import add_marks, get_all_marks
from dao.enrollment_dao import get_all_enrollments


class MarksGUI(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Marks Management")
        self.geometry("900x600")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            self,
            text="Marks Management",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        form = ttk.LabelFrame(self, text="Marks Details")
        form.pack(fill="x", padx=20)

        ttk.Label(form, text="Enrollment").grid(row=0, column=0, padx=10, pady=10)

        self.enrollment_combo = ttk.Combobox(
            form,
            width=40,
            state="readonly"
        )
        self.enrollment_combo.grid(row=0, column=1)

        ttk.Label(form, text="Total Marks").grid(row=0, column=2, padx=10)

        self.marks_entry = ttk.Entry(form, width=20)
        self.marks_entry.grid(row=0, column=3)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Add Marks",
            command=self.add_marks
        ).grid(row=0, column=0, padx=6)

        ttk.Button(
            button_frame,
            text="Refresh",
            command=self.load_marks
        ).grid(row=0, column=1, padx=6)

        columns = (
            "Mark ID",
            "Student",
            "Course",
            "Marks"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.column("Mark ID", width=90, anchor="center")
        self.tree.column("Student", width=220)
        self.tree.column("Course", width=220)
        self.tree.column("Marks", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        scrollbar.place(
            relx=0.98,
            rely=0.33,
            relheight=0.56
        )

        self.load_enrollments()
        self.load_marks()

    def load_enrollments(self):

        self.enrollments = get_all_enrollments()

        self.enrollment_combo["values"] = [
            f"{e[0]} - {e[1]} : {e[2]}"
            for e in self.enrollments
        ]

    def load_marks(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.marks = get_all_marks()

        for mark in self.marks:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    mark[0],
                    mark[1],
                    mark[2],
                    mark[3]
                )
            )

    def add_marks(self):

        try:

            enrollment_id = int(
                self.enrollment_combo.get().split(" - ")[0]
            )

            total_marks = float(
                self.marks_entry.get()
            )

            add_marks(
                enrollment_id,
                total_marks
            )

            messagebox.showinfo(
                "Success",
                "Marks added successfully."
            )

            self.marks_entry.delete(0, tk.END)

            self.load_marks()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )