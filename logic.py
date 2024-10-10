import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database
        

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
    def get_genre(self, genre):
        conn = sqlite3.connect(self.database)
        with conn:
            cur  = conn.cursor()
            cur.execute("SELECT * FROM games WHERE Genres LIKE '%' || ? || '%' ORDER BY Rating DESC LIMIT 10",(genre,))
            return(cur.fetchall())
        

    def get_random_game(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur  = conn.cursor()
            cur.execute("SELECT Title FROM games ORDER BY RANDOM() LIMIT 3")
            return(cur.fetchall())
        


        
if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    print(manager.get_genre('Simulator'))
