from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route ("/login", methods=['POST', 'get'])
def login():
    if request.method == 'POST':
    try:
        un=request.from['un']
        pwd=request.from['pwd']
        with sql.conect("database.db") as con
           cur =con.cursor()
           try:
              sqlite_insert_query = """SELECT * from login where
              username='""" + un + """' and pwd='""" + pwd + """'"""
              cur.execute(sqlite_insert_query)
              records = cur.fetchall()
              if (len(records) >= 1):
                  msg = "bingo" + " " + str(records)
              else:
                 msg = "nope"
    
        except:
            msg = "nope2"
    
    except:
    msg= "error in insert operation" + " " + msg
    finally:
        return render_template("result.html", msg=msg)
    con.close()
    
    
    
@app.route ('/addrec', methods=['post,'get])
def addrec():
    
    
