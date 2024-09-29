import sqlite3


def add_user_to_db(user_id, number, is_admin=0):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR IGNORE INTO user (user_id, number, is_admin)
        VALUES (?, ?, ?)
    ''', (user_id, number, is_admin))

    conn.commit()
    conn.close()

def get_number_from_user_id(user_id):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT number FROM user WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None
    finally:
        conn.close()
