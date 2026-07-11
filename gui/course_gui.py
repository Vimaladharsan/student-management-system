import tkinter as tk
from tkinter import ttk, messagebox

from dao.course_dao import (
    add_course,
    get_all_courses,
    update_course,
    delete_course
)


class CourseGUI(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Course Management")
        self.geometry("750x500")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            self,
            text="Course Management",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        form = ttk.LabelFrame(self, text="Course Details")
        form.pack(fill="x", padx=20)

        ttk.Label(
            form,
            text="Course Name"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = ttk.Entry(form, width=45)
        self.name_entry.grid(row=0, column=1, padx=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Add",
            command=self.add_course
        ).grid(row=0, column=0, padx=6)

        ttk.Button(
            button_frame,
            text="Update",
            command=self.update_course
        ).grid(row=0, column=1, padx=6)

        ttk.Button(
            button_frame,
            text="Delete",
            command=self.delete_course
        ).grid(row=0, column=2, padx=6)

        ttk.Button(
            button_frame,
            text="Refresh",
            command=self.load_courses
        ).grid(row=0, column=3, padx=6)

        ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_form
        ).grid(row=0, column=4, padx=6)

        self.tree = ttk.Treeview(
            self,
            columns=("ID", "Course"),
            show="headings",
            height=14
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Course", text="Course Name")

        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Course", width=520)

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
            relx=0.97,
            rely=0.32,
            relheight=0.56
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.on_select
        )

        self.load_courses()

    def load_courses(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.courses = get_all_courses()

        for course in self.courses:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    course[0],
                    course[1]
                )
            )

    def add_course(self):

        name = self.name_entry.get().strip()

        if not name:

            messagebox.showwarning(
                "Validation",
                "Course name is required."
            )
            return

        add_course(name)

        messagebox.showinfo(
            "Success",
            "Course added successfully."
        )

        self.clear_form()
        self.load_courses()

    def update_course(self):

        selected = self.tree.selection()

        if not selected:
            return

        course_id = self.tree.item(
            selected[0]
        )["values"][0]

        name = self.name_entry.get().strip()

        if not name:
            return

        update_course(
            course_id,
            name
        )

        messagebox.showinfo(
            "Success",
            "Course updated successfully."
        )

        self.clear_form()
        self.load_courses()

    def delete_course(self):

        selected = self.tree.selection()

        if not selected:
            return

        if not messagebox.askyesno(
            "Confirm",
            "Delete selected course?"
        ):
            return

        course_id = self.tree.item(
            selected[0]
        )["values"][0]

        delete_course(course_id)

        messagebox.showinfo(
            "Deleted",
            "Course deleted successfully."
        )

        self.clear_form()
        self.load_courses()

    def clear_form(self):

        self.name_entry.delete(
            0,
            tk.END
        )

    def on_select(self, event):

        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(
            selected[0]
        )["values"]

        self.clear_form()

        self.name_entry.insert(
            0,
            values[1]
        )