from db import get_connection

def enroll_student(student_id, course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s,%s)", (student_id, course_id))
    conn.commit()
    conn.close()

def get_all_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.enrollment_id, s.name, c.course_name
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id
    """)
    result = cursor.fetchall()
    conn.close()
    return result
