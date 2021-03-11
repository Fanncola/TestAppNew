import sqlite3
conn = sqlite3.connect('blog.db')
cur = conn.cursor()
cur.executescript("""
CREATE TABLE IF NOT EXISTS users (
    "id" INTEGER PRIMARY KEY,
    "fname"	TEXT,
    "lname"	TEXT,
    "gender"	TEXT,
    "EMAIL"	TEXT,
    "PASSWORD"	TEXT,
    "CreateDate" TEXT
);

CREATE TABLE IF NOT EXISTS applicationapikeys (
    "apikey"	TEXT,
    "name"	TEXT
);
CREATE TABLE IF NOT EXISTS posts (
    "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
    "text"	TEXT,
    "user"	INTEGER,
    "datetime"	TEXT,
    "status"	INTEGER
);
INSERT INTO "applicationapikeys" VALUES ('ed8fdde1-3fb7-4e23-adf4-e39264e1fafd','Developer');
INSERT INTO "applicationapikeys" VALUES ('fbe04d08-a7a1-441f-8673-dd2a7aad0eef','Users');
INSERT INTO "users"(fname,lname,gender,email,password,createdate) values ('Jon','Snow','M','winter@is.coming',
'king of the night','01.01.1970')
""")


