import hashlib, time, sqlite3, sys

# Proof of Concept FIM (File Integrity Monitor) 
print('Welcome to the Simple File Ingrity Monitor!')

time.sleep(1)

filepath = input('What file(s) are we monitoring? *please use the file name ie. FIM.py\n\n') 

# Initializing sqlite db 
with sqlite3.connect('FIM.db') as connection:
        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS File_Integrity (
            file TEXT PRIMARY KEY NOT NULL,
            hash TEXT NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        connection.commit() 

# Baseline hashing of the file(s) and/or Folder
def baseline(filepath):
   # Open the file in read mode ('r') using a 'with' statement
    # The 'with' statement ensures the file is automatically closed, even if errors occur.
    try:
        with open(filepath, 'r') as file:
        # Read the entire content of the file as a single string
            content = file.read()
    except FileNotFoundError:
        print(f'\nThe file {filepath} does not exist.')
        sys.exit()

    # Encodes the filepath in the utf-8 standard
    encoded_filepath = content.encode('utf-8')

    hasher = hashlib.sha256()

    # Update the hash object with the encoded string
    hasher.update(encoded_filepath)

    # Get the hexadecimal representation of the hash
    hex_digest = hasher.hexdigest()

    try:
            # Attempt to insert, ignoring if a duplicate exists
            cursor.execute(f'''
                INSERT OR IGNORE INTO File_Integrity (file, hash) VALUES (?, ?)''',(filepath,hex_digest))

            if cursor.rowcount == 0:
                print(f"Your file: '{filepath}' already exists in the FIM database.") 
            else:
                connection.commit()  # Commit the changes if insertion was successful
                print(f"Your file: '{filepath}:{hex_digest}' was inserted successfully into the FIM database.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

#comparing baseline to the current hash
def check_integrity(filepath):
    try:
        with open(filepath, 'r') as file:
        # Read the entire content of the file as a single string
            content = file.read()
    except FileNotFoundError:
        print(f'\nThe file {filepath} does not exist.')
        sys.exit()

    encoded_filepath = content.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(encoded_filepath)
    new_hex_digest = hasher.hexdigest()
    
    # Selects the file and hash from the database that matches the file given by the user
    cursor.execute('SELECT * FROM File_Integrity WHERE file = ?',(filepath,))
    integ_check = cursor.fetchall()[0]

    # Checks Hash in DB to the current hash to determine changes 
    if integ_check[1] == new_hex_digest:
        print(f'\nThe file {filepath} has not been changed!')
    elif integ_check[1] != new_hex_digest:
        print(f'\nWARNING: The file {filepath} has been changed *Integrity may be compromised!')
        print(f'\nCurrent Hash: {new_hex_digest} \nBaseline Hash: {integ_check[1]}')

    connection.commit()

def menu():
    menu = input('\nWould you like to: A. Add this files hash to the baseline? or B. Check this files integrity?\n')

    if menu == 'A' or menu == 'a':
        baseline(filepath)
    elif menu == 'B' or menu == 'b':
        check_integrity(filepath)

menu()