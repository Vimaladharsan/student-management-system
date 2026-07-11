import tkinter as tk
from tkinter import ttk, messagebox

from dao.enrollment_dao import enroll_student, get_all_enrollments
from dao.student_dao import get_all_students
from dao.course_dao import get_all_courses


class EnrollmentGUI(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Enrollment Management")
        self.geometry("900x600")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            self,
            text="Enrollment Management",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        form = ttk.LabelFrame(self, text="Enrollment Details")
        form.pack(fill="x", padx=20)

        ttk.Label(form, text="Student").grid(row=0, column=0, padx=10, pady=10)

        self.student_combo = ttk.Combobox(
            form,
            width=35,
            state="readonly"
        )
        self.student_combo.grid(row=0, column=1)

        ttk.Label(form, text="Course").grid(row=0, column=2, padx=10)

        self.course_combo = ttk.Combobox(
            form,
            width=35,
            state="readonly"
        )
        self.course_combo.grid(row=0, column=3)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Enroll",
            command=self.enroll
        ).grid(row=0, column=0, padx=6)

        ttk.Button(
            button_frame,
            text="Refresh",
            command=self.load_enrollments
        ).grid(row=0, column=1, padx=6)

        columns = (
            "Enrollment ID",
            "Student",
            "Course"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.column("Enrollment ID", width=120, anchor="center")
        self.tree.column("Student", width=280)
        self.tree.column("Course", width=280)

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

        self.load_students()
        self.load_courses()
        self.load_enrollments()

    def load_students(self):

        self.students = get_all_students()

        self.student_combo["values"] = [
            f"{s[0]} - {s[1]}"
            for s in self.students
        ]

    def load_courses(self):

        self.courses = get_all_courses()

        self.course_combo["values"] = [
            f"{c[0]} - {c[1]}"
            for c in self.courses
        ]

    def load_enrollments(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.enrollments = get_all_enrollments()

        for e in self.enrollments:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    e[0],
                    e[1],
                    e[2]
                )
            )

    def enroll(self):

        try:

            student_id = int(
                self.student_combo.get().split(" - ")[0]
            )

            course_id = int(
                self.course_combo.get().split(" - ")[0]
            )

            enroll_student(
                student_id,
                course_id
            )

            messagebox.showinfo(
                "Success",
                "Student enrolled successfully."
            )

            self.load_enrollments()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )