import sqlite3
import json


class Sql:
    def __init__(self):
        pass
        self.conn = sqlite3.connect('orders.db')

    @staticmethod
    def all_sql(userid, limit, order, sort, sql, table):
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        if sql == 'SELECT':
            sql = f'{sql} '

    @staticmethod
    def user_get(user):
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute("select userid,fname,lname,gender,email,password FROM users where userid = ?",
                       (user,))
        return cursor.fetchone()

    @staticmethod
    def unique_email(email):
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute("select email from users where email = ?", (email,))
        return cursor.fetchall()


    @staticmethod
    def users(order, sort, limit):
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute(f"select userid, fname, lname, gender, email, password from users "
                       f"order by {order} {sort} limit {limit}")
        return cursor.fetchall()


    @staticmethod
    def user_post(userid, fname, lname, gender, email, password):
        conn = sqlite3.connect('orders.db')
        conn.execute("insert into users values (?,?,?,?,?,?);",
                     (userid, fname, lname, gender, email, password))
        conn.commit()
        return json.dumps(Sql.last_id())

    @staticmethod
    def last_id():
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute("select * from users order by userid desc limit ?;",
                       (1,))
        return cursor.fetchone()

    @staticmethod
    def authority(header):
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute("select count(*) from applicationapikeys where apikey = ?",
                       (header,))
        return cursor.fetchone()[0]


    @staticmethod
    def all_posts():
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        cursor.execute("select * from posts")
        return cursor.fetchall()

    @staticmethod
    def add_post(id, text, user, datetime, status):
        conn = sqlite3.connect('orders.db')
        conn.execute("insert into posts values (?,?,?,?,?)",
                     (id, text, user, datetime, status))
        conn.commit()
        return json.dumps(Sql.last_id_post())

    @staticmethod
    def last_id_post():
        conn = sqlite3.connect('orders.db')
        cursor = conn.cursor()
        sql = f'select * from posts order by id desc limit 1'
        cursor.execute(sql)
        return cursor.fetchone()

    @staticmethod
    def update_user(userid,fname, lname, gender):
        conn = sqlite3.connect('orders.db')
        conn.execute("update users set fname = ?, lname = ?, gender = ? where userid = ?;",
                     (fname, lname, gender, userid))
        conn.commit()
        return json.dumps(Sql.user_get(userid))

