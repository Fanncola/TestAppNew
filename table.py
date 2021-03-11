import sqlite3
conn = sqlite3.connect('orders.db')
# cur = conn.execute("""CREATE TABLE IF NOT EXISTS applicationapikeys(
#     apikey TEXT,
#     name TEXT)
#     """)

# conn.execute("""INSERT INTO applicationapikeys
#     VALUES ('fbe04d08-a7a1-441f-8673-dd2a7aad0eef','Users')
# """)
# conn.commit()

cur = conn.execute("""ALTER TABLE USERS ADD PASSWORD TEXT
""")