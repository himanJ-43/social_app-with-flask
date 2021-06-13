from os import path
import sqlite3 as sql 


ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("insert into posts (name, content) values(?,?)",( name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts


'''def delete ():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("delete * from posts")
    posts = cur.del 
    con.close()'''