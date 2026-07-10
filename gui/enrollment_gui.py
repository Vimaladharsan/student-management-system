import tkinter as tk
from tkinter import messagebox, ttk
from dao.enrollment_dao import enroll_student, get_all_enrollments
from dao.student_dao import get_all_students
from dao.course_dao import get_all_courses

class EnrollmentGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Enroll Students")
        self.geometry("600x400")

        tk.Label(self, text="Student").grid(row=0,column=0)
        self.student_combo = ttk.Combobox(self, state="readonly")
        self.student_combo.grid(row=0,column=1)

        tk.Label(self, text="Course").grid(row=1,column=0)
        self.course_combo = ttk.Combobox(self, state="readonly")
        self.course_combo.grid(row=1,column=1)

        tk.Button(self, text="Enroll", command=self.enroll).grid(row=2,column=0)
        tk.Button(self, text="Refresh", command=self.load_enrollments).grid(row=2,column=1)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.grid(row=3,column=0,columnspan=2,pady=10)

        self.load_students()
        self.load_courses()
        self.load_enrollments()

    def load_students(self):
        self.students = get_all_students()
        self.student_combo['values'] = [f"{s[0]} - {s[1]}" for s in self.students]

    def load_courses(self):
        self.courses = get_all_courses()
        self.course_combo['values'] = [f"{c[0]} - {c[1]}" for c in self.courses]

    def load_enrollments(self):
        self.listbox.delete(0, tk.END)
        self.enrollments = get_all_enrollments()
        for e in self.enrollments:
            self.listbox.insert(tk.END, f"{e[0]} - {e[1]} : {e[2]}")

    def enroll(self):
        try:
            student_id = int(self.student_combo.get().split(" - ")[0])
            course_id = int(self.course_combo.get().split(" - ")[0])
            enroll_student(student_id, course_id)
            self.load_enrollments()
        except Exception as e:
            messagebox.showerror("Error", str(e))
