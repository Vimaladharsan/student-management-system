import tkinter as tk
from tkinter import ttk

from gui.department_gui import DepartmentGUI
from gui.student_gui import StudentGUI
from gui.teacher_gui import TeacherGUI
from gui.course_gui import CourseGUI
from gui.enrollment_gui import EnrollmentGUI
from gui.marks_gui import MarksGUI
from gui.attendance_gui import AttendanceGUI


class MainDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Management System")
        self.geometry("950x650")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 24, "bold"),
            foreground="#1f3b73",
            background="#eef2f7"
        )

        style.configure(
            "Sub.TLabel",
            font=("Segoe UI", 11),
            background="#eef2f7",
            foreground="#555555"
        )

        style.configure(
            "Dashboard.TButton",
            font=("Segoe UI", 12, "bold"),
            padding=15
        )

        # ---------------- HEADER ----------------

        ttk.Label(
            self,
            text="🎓 Student Management System",
            style="Title.TLabel"
        ).pack(pady=(25, 5))

        ttk.Label(
            self,
            text="Python • Tkinter • MariaDB",
            style="Sub.TLabel"
        ).pack(pady=(0, 20))

        # ---------------- BUTTON FRAME ----------------

        frame = tk.Frame(self, bg="#eef2f7")
        frame.pack(expand=True)

        buttons = [
            ("🏢 Departments", self.open_departments),
            ("👨‍🎓 Students", self.open_students),
            ("👨‍🏫 Teachers", self.open_teachers),
            ("📚 Courses", self.open_courses),
            ("📝 Enrollments", self.open_enrollments),
            ("📊 Marks", self.open_marks),
            ("📅 Attendance", self.open_attendance),
        ]

        rows = 3
        cols = 3

        for index, (text, command) in enumerate(buttons):
            r = index // cols
            c = index % cols

            btn = ttk.Button(
                frame,
                text=text,
                command=command,
                style="Dashboard.TButton",
                width=22
            )

            btn.grid(
                row=r,
                column=c,
                padx=20,
                pady=20,
                ipadx=10,
                ipady=15
            )

        # ---------------- FOOTER ----------------

        footer = tk.Frame(self, bg="#1f3b73", height=40)
        footer.pack(side="bottom", fill="x")

        tk.Label(
            footer,
            text="Student Management System | Python + MariaDB",
            fg="white",
            bg="#1f3b73",
            font=("Segoe UI", 10)
        ).pack(pady=10)

    def open_departments(self):
        DepartmentGUI(self)

    def open_students(self):
        StudentGUI(self)

    def open_teachers(self):
        TeacherGUI(self)

    def open_courses(self):
        CourseGUI(self)

    def open_enrollments(self):
        EnrollmentGUI(self)

    def open_marks(self):
        MarksGUI(self)

    def open_attendance(self):
        AttendanceGUI(self)


if __name__ == "__main__":
    app = MainDashboard()
    app.mainloop()