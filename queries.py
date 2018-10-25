import connection


@connection.connection_handler
def get_locations_for_user(user_id):
    dict_cur.execute("""
                     SELECT id, title FROM locations
                     WHERE user_id = %(user_id)s
                     ORDER BY id;
                     """,
                     {"user_id": user_id})
    return dict_cur.fetchall()