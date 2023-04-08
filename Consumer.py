import sqlite3
class SQLitreConsumer:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
    def create_connection(self):
        self.conn = sqlite3.connect(self.db_file)
    def create_CTF_table(self):
        sql = ''' CREATE TABLE IF NOT EXISTS CTFs (name CHAR UNIQUE, date CHAR, format CHAR, online BOOL, organizer CHAR, location CHAR, url CHAR);'''
        cur = self.conn.cursor()
        cur.execute(sql)
    def insert(self, ctf):
        sql = ''' INSERT INTO CTFs(name,date,format,online,organizer,location,url)
                VALUES(?,?,?,?,?,?,?) '''
        cur = self.conn.cursor()
        try:
            cur.execute(sql, ctf)
            self.conn.commit()
        except sqlite3.IntegrityError : 
            print("WARNING: dup data")
        return cur.lastrowid
    def close_connection(self):
        self.conn.close()