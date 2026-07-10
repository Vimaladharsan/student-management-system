from db import get_connection

def add_student(name, email, phone, dept_id, dob, admitted_year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name,email,phone,department_id,dob,admitted_year) VALUES (%s,%s,%s,%s,%s,%s)",
        (name,email,phone,dept_id,dob,admitted_year)
    )
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            s.student_id,
            s.name,
            s.email,
            s.phone,
            s.department_id,
            d.department_name,
            s.dob,
            s.admitted_year
        FROM students s
        LEFT JOIN departments d
            ON s.department_id = d.department_id
    """)

    result = cursor.fetchall()
    conn.close()
    return result

def update_student(student_id, name, email, phone, dept_id, dob, admitted_year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=%s,email=%s,phone=%s,department_id=%s,dob=%s,admitted_year=%s WHERE student_id=%s",
        (name,email,phone,dept_id,dob,admitted_year,student_id)
    )
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
    conn.commit()
    conn.close()
