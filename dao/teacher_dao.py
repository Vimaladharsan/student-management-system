from db import get_connection


def add_teacher(name, email, phone, dept_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO teachers
        (name, email, phone, department_id)
        VALUES (%s, %s, %s, %s)
        """,
        (name, email, phone, dept_id)
    )

    conn.commit()
    conn.close()


def get_all_teachers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            t.teacher_id,
            t.name,
            t.email,
            t.phone,
            d.department_name,
            t.department_id
        FROM teachers t
        LEFT JOIN departments d
        ON t.department_id = d.department_id
    """)

    result = cursor.fetchall()

    conn.close()

    return result


def update_teacher(teacher_id, name, email, phone, dept_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE teachers
        SET
            name=%s,
            email=%s,
            phone=%s,
            department_id=%s
        WHERE teacher_id=%s
        """,
        (
            name,
            email,
            phone,
            dept_id,
            teacher_id
        )
    )

    conn.commit()
    conn.close()


def delete_teacher(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM teachers WHERE teacher_id=%s",
        (teacher_id,)
    )

    conn.commit()
    conn.close()