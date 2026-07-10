import tkinter as tk
from tkinter import messagebox, ttk
from dao.mark_dao import add_marks, get_all_marks
from dao.enrollment_dao import get_all_enrollments

class MarksGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Manage Marks")
        self.geometry("600x400")

        tk.Label(self, text="Enrollment").grid(row=0, column=0)
        self.enrollment_combo = ttk.Combobox(self, state="readonly")
        self.enrollment_combo.grid(row=0, column=1)

        tk.Label(self, text="Total Marks").grid(row=1, column=0)
        self.marks_entry = tk.Entry(self)
        self.marks_entry.grid(row=1, column=1)

        tk.Button(self, text="Add Marks", command=self.add_marks).grid(row=2, column=0)
        tk.Button(self, text="Refresh", command=self.load_marks).grid(row=2, column=1)

        self.listbox = tk.Listbox(self, width=80)
        self.listbox.grid(row=3, column=0, columnspan=2, pady=10)

        self.load_enrollments()
        self.load_marks()

    def load_enrollments(self):
        self.enrollments = get_all_enrollments()
        self.enrollment_combo['values'] = [f"{e[0]} - {e[1]} : {e[2]}" for e in self.enrollments]

    def load_marks(self):
        self.listbox.delete(0, tk.END)
        self.marks = get_all_marks()
        for m in self.marks:
            self.listbox.insert(tk.END, f"{m[0]} - {m[1]} : {m[2]} = {m[3]}")

    def add_marks(self):
        try:
            enrollment_id = int(self.enrollment_combo.get().split(" - ")[0])
            total_marks = float(self.marks_entry.get())
            add_marks(enrollment_id, total_marks)
            self.load_marks()
            self.marks_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))
