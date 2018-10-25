import connection
import psycopg2


@connection.connection_handler
def get_locations_for_user(dict_cur, user_id):
    dict_cur.execute("""
                         SELECT id, title FROM locations
                         WHERE user_id = %(user_id)s
                         ORDER BY id;
                     """,
                     {"user_id": user_id})
    return dict_cur.fetchall()


@connection.connection_handler
def get_people_for_user(dict_cur, user_id):
    dict_cur.execute("""
                         SELECT id, name FROM people
                         WHERE user_id = %(user_id)s;
                         """,
                     {"user_id": user_id})
    return dict_cur.fetchall()


@connection.connection_handler
def save_new_person(dict_cur, name, phone, color, user_id):
    dict_cur.execute("""
                        INSERT INTO people (name, phone, color, status, user_id)
                        VALUES (%(name)s, %(phone)s, %(color)s, 'pending', %(user_id)s)
                        RETURNING id, name, phone, color, status;
                     """,
                     {'name': name, 'phone': phone, 'color': color, 'user_id': user_id})
    return dict_cur.fetchone()


@connection.connection_handler
def insert_user(dict_cur, user_name, password, email, phone):
    try:
        dict_cur.execute("""
                            INSERT INTO users (user_name, password, email, phone)
                            VALUES (%(user_name)s, %(password)s, %(email)s, %(phone)s);
                         """,
                         {"user_name": user_name, "password": password, "email": email, "phone": phone})
    except psycopg2.IntegrityError:
        return {"valid_username": False}
    return {"valid_username": True}


@connection.connection_handler
def get_password(dict_cur, user_name):
    dict_cur.execute("""
                    SELECT password FROM users
                    WHERE user_name = %(user_name)s;
                   """,
                     {"user_name": user_name})
    return dict_cur.fetchone()


@connection.connection_handler
def get_user_id(dict_cur, user_name):
    dict_cur.execute("""
                        SELECT id FROM users
                        WHERE user_name = %(user_name)s;
                     """,
                     {'user_name': user_name})
    return dict_cur.fetchone()
