import sqlite3
import json
from errors import Errors
errors = Errors


class Sql:
    def __init__(self):
        pass
        self.conn = sqlite3.connect('blog.db')

    @staticmethod
    def all_sql(userid, limit, order, sort, sql, table):
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()
        if sql == 'SELECT':
            sql = f'{sql} '

    @staticmethod
    def user_get(user):
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        sql = f"select id,fname,lname,gender,email,password,createdate FROM users where id = {user}"
        cur.execute(sql)
        return cur.fetchone()

    @staticmethod
    def unique_email(email):
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        sql = f"select email from users where email = '{email}'"
        cur.execute(sql)
        return cur.fetchall()

    @staticmethod
    def users(order, sort, limit):
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        sql = f"select {order}, fname, lname, gender, email, password, createdate from users " \
              f"order by {order} {sort} limit {limit}"
        print(sql)
        cur.execute(sql)
        return cur.fetchall()

    @staticmethod
    def user_post(fname, lname, gender, email, password, createdate):
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        sql = f"insert into users(fname, lname, gender, email, password, createdate) "\
              f"values ('{fname}','{lname}','{gender}','{email}','{password}', '{createdate}');"
        conn.execute(sql)
        conn.commit()
        return Sql.last_id()

    @staticmethod
    def last_id():
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        cur.execute("select id from users order by id desc limit ?;",
                       (1,))
        return cur.fetchone()[0]

    @staticmethod
    def authority(header):
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        cur.execute("select count(*) from applicationapikeys where apikey = ?",
                       (header,))
        return cur.fetchone()[0]


    @staticmethod
    def all_posts():
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        cur.execute("select * from posts")
        return cur.fetchall()

    @staticmethod
    def add_post(id, text, user, datetime, status):
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        cur.execute("insert into posts values (?,?,?,?,?)",
                     (id, text, user, datetime, status))
        conn.commit()
        return json.dumps(Sql.last_id_post())

    @staticmethod
    def last_id_post():
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        sql = f'select * from posts order by id desc limit 1'
        cur.execute(sql)
        return cur.fetchone()

    @staticmethod
    def update_user(id, fname, lname, gender, email):
        conn = sqlite3.connect('blog.db')
        cur = conn.cursor()
        sql = f"update users set fname = '{fname}', lname = '{lname}', " \
              f"gender = '{gender}', email='{email}' where id = {id};"
        cur.execute(sql)
        conn.commit()
        return json.dumps(Sql.user_get(id))

