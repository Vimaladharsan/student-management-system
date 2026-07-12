# 🎓 Student Management System

A desktop-based **Student Management System** built with **Python, Tkinter, and MariaDB** to efficiently manage academic records such as students, teachers, departments, courses, enrollments, marks, and attendance.

---

## ✨ Features

- 🏢 Department Management
- 👨‍🎓 Student Management
- 👨‍🏫 Teacher Management
- 📚 Course Management
- 📝 Student Enrollment
- 📊 Marks Management
- 📅 Attendance Management

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- MariaDB
- Python Database Connector

---

## 📂 Project Structure

```text
student-management-system/
│
├── app.py
├── db.py
├── requirements.txt
├── README.md
│
├── dao/
│   ├── attendance_dao.py
│   ├── course_dao.py
│   ├── department_dao.py
│   ├── enrollment_dao.py
│   ├── mark_dao.py
│   ├── student_dao.py
│   └── teacher_dao.py
│
├── gui/
│   ├── attendance_gui.py
│   ├── course_gui.py
│   ├── department_gui.py
│   ├── enrollment_gui.py
│   ├── main_dashboard.py
│   ├── marks_gui.py
│   ├── student_gui.py
│   └── teacher_gui.py
│
├── database/
│   └── sms_db.sql
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <repository-url>
cd student-management-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Import the database

Create a database named:

```text
sms_db
```

Import the SQL file located in:

```text
database/sms_db.sql
```

Update the database credentials inside:

```text
db.py
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 📸 Screenshots

Screenshots of the application are available in the **screenshots/** directory.

---

## 👨‍💻 Author

Developed as a Student Management System using Python, Tkinter, and MariaDB.
