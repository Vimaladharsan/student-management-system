from db import get_connection

def add_course(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (course_name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT course_id, course_name FROM courses")
    result = cursor.fetchall()
    conn.close()
    return result

def update_course(course_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE courses SET course_name=%s WHERE course_id=%s",
        (name, course_id)
    )
    conn.commit()
    conn.close()


def delete_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM courses WHERE course_id=%s",
        (course_id,)
    )
    conn.commit()
    conn.close()