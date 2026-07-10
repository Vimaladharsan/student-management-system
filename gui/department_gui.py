import tkinter as tk
from tkinter import ttk, messagebox

from dao.department_dao import (
    add_department,
    get_all_departments,
    update_department,
    delete_department
)


class DepartmentGUI(tk.Toplevel):

    def __init__(self, master):
        super().__init__(master)

        self.title("Department Management")
        self.geometry("750x500")
        self.configure(bg="#eef2f7")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            self,
            text="Department Management",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=15)

        form = ttk.Frame(self)
        form.pack(fill="x", padx=20)

        ttk.Label(form, text="Department Name").grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )

        self.name_entry = ttk.Entry(form, width=40)
        self.name_entry.grid(row=0, column=1, padx=10)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=15)

        ttk.Button(
            button_frame,
            text="Add",
            command=self.add_department
        ).grid(row=0, column=0, padx=8)

        ttk.Button(
            button_frame,
            text="Update",
            command=self.update_department
        ).grid(row=0, column=1, padx=8)

        ttk.Button(
            button_frame,
            text="Delete",
            command=self.delete_department
        ).grid(row=0, column=2, padx=8)

        ttk.Button(
            button_frame,
            text="Refresh",
            command=self.load_departments
        ).grid(row=0, column=3, padx=8)

        columns = ("ID", "Department")

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=12
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Department", text="Department")

        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Department", width=500)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.place(relx=0.97, rely=0.25, relheight=0.58)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.load_departments()

    def load_departments(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.departments = get_all_departments()

        for dept in self.departments:
            self.tree.insert(
                "",
                tk.END,
                values=(dept[0], dept[1])
            )

    def add_department(self):
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showwarning(
                "Validation",
                "Department name is required."
            )
            return

        add_department(name)

        messagebox.showinfo(
            "Success",
            "Department added successfully."
        )

        self.name_entry.delete(0, tk.END)
        self.load_departments()

    def update_department(self):
        selected = self.tree.selection()

        if not selected:
            return

        dept_id = self.tree.item(selected[0])["values"][0]
        name = self.name_entry.get().strip()

        if not name:
            return

        update_department(dept_id, name)

        messagebox.showinfo(
            "Success",
            "Department updated successfully."
        )

        self.load_departments()

    def delete_department(self):
        selected = self.tree.selection()

        if not selected:
            return

        if not messagebox.askyesno(
            "Confirm",
            "Delete selected department?"
        ):
            return

        dept_id = self.tree.item(selected[0])["values"][0]

        delete_department(dept_id)

        messagebox.showinfo(
            "Deleted",
            "Department deleted successfully."
        )

        self.load_departments()

    def on_select(self, event):
        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(selected[0])["values"]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[1])