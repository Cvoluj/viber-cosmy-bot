import sqlite3


def add_user_to_db(user_id, number, is_admin=0):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR REPLACE INTO user (user_id, number, is_admin)
        VALUES (?, ?, ?)
    ''', (user_id, number, is_admin))

    conn.commit()
    conn.close()

def clear_number_for_user_id(user_id):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE user SET number = "" WHERE user_id = ?', (user_id,))
        conn.commit()
    finally:
        conn.close()

def get_number_from_user_id(user_id):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT number FROM user WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()

        if result:
            return result[0][2:]
        else:
            return None
    finally:
        conn.close()

def get_is_admin_from_user_id(user_id):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT is_admin FROM user WHERE user_id = ?', (user_id,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None
    finally:
        conn.close()

def get_user_ids():
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT user_id FROM user')
        results = cursor.fetchall()

        if results:
            return [result[0] for result in results]
        else:
            return None
    finally:
        conn.close()

def give_admin_rules(user_id):
    conn = sqlite3.connect('viber_users.db')
    cursor = conn.cursor()

    try:
        cursor.execute('UPDATE user SET is_admin=1 WHERE user_id = ?', (user_id,))
        conn.commit()

        cursor.execute('SELECT is_admin FROM user WHERE user_id = ?', (user_id,))
        is_admin = cursor.fetchone()

        return is_admin
    finally:
        conn.close()

if __name__ == "__main__":
    print(get_number_from_user_id("2Tln9NcxXDho6zX8h4rjpw=="))
    print(get_user_ids())
    