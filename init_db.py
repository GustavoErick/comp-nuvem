import sqlite3

# connection = sqlite3.connect('database.db')


# with open('schema.sql') as f:
#    connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
  #          ('First Post', 'Content for the first post')
   #         )
# print("Primeiro post inserido.")

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
   #         ('Second Post', 'Content for the second post')
  #          )
#print("Segundo post inserido.")


#connection.commit()
#connection.close()

def init_db():
    conn = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.close()

if __name__ == "__main__":
    init_db()
