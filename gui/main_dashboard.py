import tkinter as tk
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
        self.geometry("400x400")
        tk.Button(self, text="Manage Departments", width=30, command=self.open_departments).pack(pady=10)
        tk.Button(self, text="Manage Students", width=30, command=self.open_students).pack(pady=10)
        tk.Button(self, text="Manage Teachers", width=30, command=self.open_teachers).pack(pady=10)
        tk.Button(self, text="Manage Courses", width=30, command=self.open_courses).pack(pady=10)
        tk.Button(self, text="Manage Enrollments", width=30, command=self.open_enrollments).pack(pady=10)
        tk.Button(self, text="Manage Marks", width=30, command=self.open_marks).pack(pady=10)
        tk.Button(self, text="Manage Attendance", width=30, command=self.open_attendance).pack(pady=10)

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
