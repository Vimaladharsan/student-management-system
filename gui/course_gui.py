import tkinter as tk
from tkinter import messagebox
from dao.course_dao import add_course, get_all_courses, update_course, delete_course

class CourseGUI(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Manage Courses")
        self.geometry("400x400")

        tk.Label(self, text="Course Name").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        tk.Button(self, text="Add", command=self.add_course).pack(pady=5)
        tk.Button(self, text="Update", command=self.update_course).pack(pady=5)
        tk.Button(self, text="Delete", command=self.delete_course).pack(pady=5)
        tk.Button(self, text="Refresh", command=self.load_courses).pack(pady=5)

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        self.load_courses()

    def load_courses(self):
        self.listbox.delete(0, tk.END)
        self.courses = get_all_courses()
        for c in self.courses:
            self.listbox.insert(tk.END, f"{c[0]} - {c[1]}")

    def add_course(self):
        name = self.name_entry.get()
        if name:
            add_course(name)
            self.load_courses()
            self.name_entry.delete(0, tk.END)

    def update_course(self):
        selected = self.listbox.curselection()
        if selected:
            course_id = self.courses[selected[0]][0]
            name = self.name_entry.get()
            if name:
                update_course(course_id,name)
                self.load_courses()
                self.name_entry.delete(0, tk.END)

    def delete_course(self):
        selected = self.listbox.curselection()
        if selected:
            course_id = self.courses[selected[0]][0]
            delete_course(course_id)
            self.load_courses()
            self.name_entry.delete(0, tk.END)

    def on_select(self,event):
        selected = self.listbox.curselection()
        if selected:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, self.courses[selected[0]][1])
