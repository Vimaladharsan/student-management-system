from db import get_connection


def add_marks(enrollment_id, total_marks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO marks
        (enrollment_id, total_marks)
        VALUES (%s, %s)
        """,
        (
            enrollment_id,
            total_marks
        )
    )

    conn.commit()
    conn.close()


def get_all_marks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            m.mark_id,
            s.name,
            c.course_name,
            m.total_marks
        FROM marks m
        JOIN enrollments e
            ON m.enrollment_id = e.enrollment_id
        JOIN students s
            ON e.student_id = s.student_id
        JOIN courses c
            ON e.course_id = c.course_id
        ORDER BY s.name
    """)

    result = cursor.fetchall()

    conn.close()

    return result