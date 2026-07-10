import tkinter as tk
from tkinter import messagebox, ttk
from dao.attendance_dao import mark_attendance, get_all_attendance
from dao.enrollment_dao import get_all_enrollments

class AttendanceGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Mark Attendance")
        self.geometry("600x400")

        tk.Label(self, text="Enrollment").grid(row=0, column=0)
        self.enrollment_combo = ttk.Combobox(self, state="readonly")
        self.enrollment_combo.grid(row=0, column=1)

        tk.Label(self, text="Status").grid(row=1, column=0)
        self.status_combo = ttk.Combobox(self, state="readonly")
        self.status_combo['values'] = ["Present", "Absent"]
        self.status_combo.grid(row=1, column=1)

        tk.Button(self, text="Mark", command=self.mark).grid(row=2, column=0)
        tk.Button(self, text="Refresh", command=self.load_attendance).grid(row=2, column=1)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.grid(row=3, column=0, columnspan=2, pady=10)

        self.load_enrollments()
        self.load_attendance()

    def load_enrollments(self):
        self.enrollments = get_all_enrollments()
        self.enrollment_combo['values'] = [f"{e[0]} - {e[1]} : {e[2]}" for e in self.enrollments]

    def load_attendance(self):
        self.listbox.delete(0, tk.END)
        self.attendance = get_all_attendance()
        for a in self.attendance:
            self.listbox.insert(tk.END, f"{a[0]} - {a[1]} : {a[2]} = {a[3]}")

    def mark(self):
        try:
            enrollment_id = int(self.enrollment_combo.get().split(" - ")[0])
            status = self.status_combo.get()
            mark_attendance(enrollment_id, status)
            self.load_attendance()
        except Exception as e:
            messagebox.showerror("Error", str(e))
