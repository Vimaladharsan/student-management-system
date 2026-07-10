from db import get_connection

def mark_attendance(enrollment_id, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (enrollment_id,status) VALUES (%s,%s)", (enrollment_id,status))
    conn.commit()
    conn.close()

def get_all_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.attendance_id, s.name, c.course_name, a.status
        FROM attendance a
        JOIN enrollments e ON a.enrollment_id = e.enrollment_id
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id
    """)
    result = cursor.fetchall()
    conn.close()
    return result
