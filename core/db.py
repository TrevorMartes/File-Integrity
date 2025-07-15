import sqlite3

DB_File = "FIM.db"

def connect():
        return sqlite3.connect(DB_File)

def initialize():
    with connect() as conn:
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS File_Integrity (
            file TEXT PRIMARY KEY NOT NULL,
            hash TEXT NOT NULL
        );
        '''
        conn.execute(create_table_query)
        conn.commit() 

def save_file_hash(filepath,file_hash):
    initialize()
    with connect() as conn:
        conn.execute(
            "INSERT OR REPLACE INTO File_Integrity (file, hash) VALUES (?, ?)",
            (filepath, file_hash)
        )
        conn.commit()

def get_stored_hash(filepath):
    initialize()
    with connect() as conn:
        cursor = conn.execute(
            "SELECT hash FROM File_Integrity WHERE file = ?", (filepath,)
        )
        result = cursor.fetchone()
        return result[0] if result else None
    
def file_exists(filepath):
    initialize()
    with connect() as conn:
        cursor = conn.execute(
            "SELECT 1 FROM File_Integrity WHERE file = ?", (filepath,)
            )
        return cursor.fetchone() is not None 