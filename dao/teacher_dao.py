from db import get_connection

def add_teacher(name, email, phone, dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (name,email,phone,department_id) VALUES (%s,%s,%s,%s)",
                   (name,email,phone,dept_id))
    conn.commit()
    conn.close()

def get_all_teachers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.teacher_id, t.name, d.department_name
        FROM teachers t
        LEFT JOIN departments d ON t.department_id = d.department_id
    """)
    result = cursor.fetchall()
    conn.close()
    return result
