import sqlite3


def execute_query(filename):
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()

    with open(filename, "r", encoding="utf-8") as f:
        sql_query = f.read()
        cursor.execute(sql_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

    conn.close()


execute_query("query_1.sql")
