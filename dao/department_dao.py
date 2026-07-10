from db import get_connection

def add_department(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO departments (department_name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def get_all_departments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT department_id, department_name FROM departments")
    result = cursor.fetchall()
    conn.close()
    return result

def update_department(dept_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE departments SET department_name=%s WHERE department_id=%s", (name, dept_id))
    conn.commit()
    conn.close()

def delete_department(dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM departments WHERE department_id=%s", (dept_id,))
    conn.commit()
    conn.close()
