import tkinter as tk
from tkinter import ttk, messagebox

from dao.attendance_dao import (
    mark_attendance,
    get_all_attendance
)

from dao.enrollment_dao import get_all_enrollments


class AttendanceGUI(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Attendance Management")
        self.geometry("900x600")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            self,
            text="Attendance Management",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        form = ttk.LabelFrame(
            self,
            text="Attendance Details"
        )

        form.pack(fill="x", padx=20)

        ttk.Label(
            form,
            text="Enrollment"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.enrollment_combo = ttk.Combobox(
            form,
            width=40,
            state="readonly"
        )

        self.enrollment_combo.grid(row=0, column=1)

        ttk.Label(
            form,
            text="Status"
        ).grid(row=0, column=2, padx=10)

        self.status_combo = ttk.Combobox(
            form,
            width=20,
            state="readonly",
            values=[
                "Present",
                "Absent"
            ]
        )

        self.status_combo.grid(row=0, column=3)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Mark Attendance",
            command=self.mark
        ).grid(row=0, column=0, padx=6)

        ttk.Button(
            button_frame,
            text="Refresh",
            command=self.load_attendance
        ).grid(row=0, column=1, padx=6)

        columns = (
            "Attendance ID",
            "Student",
            "Course",
            "Status"
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)

        self.tree.column(
            "Attendance ID",
            width=110,
            anchor="center"
        )

        self.tree.column(
            "Student",
            width=220
        )

        self.tree.column(
            "Course",
            width=220
        )

        self.tree.column(
            "Status",
            width=120,
            anchor="center"
        )

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
        self.load_attendance()

    def load_enrollments(self):

        self.enrollments = get_all_enrollments()

        self.enrollment_combo["values"] = [
            f"{e[0]} - {e[1]} : {e[2]}"
            for e in self.enrollments
        ]

    def load_attendance(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.attendance = get_all_attendance()

        for attendance in self.attendance:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    attendance[0],
                    attendance[1],
                    attendance[2],
                    attendance[3]
                )
            )

    def mark(self):

        try:

            enrollment_id = int(
                self.enrollment_combo.get().split(" - ")[0]
            )

            status = self.status_combo.get()

            if not status:

                messagebox.showwarning(
                    "Validation",
                    "Please select attendance status."
                )

                return

            mark_attendance(
                enrollment_id,
                status
            )

            messagebox.showinfo(
                "Success",
                "Attendance marked successfully."
            )

            self.status_combo.set("")
            self.load_attendance()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )