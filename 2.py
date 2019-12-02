import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT genre FROM films WHERE year > 2010 
            AND year < 2011""").fetchall()
for elem in result:
    print(elem[0])

con.close()