import hashlib, time, sqlite3, sys

# Proof of Concept FIM (File Integrity Monitor) 
print('Welcome to the Simple File Ingrity Monitor!')

time.sleep(1)

filepath = input('What file(s) are we monitoring? *please use the filepath ie. ~/home/user/Documents\n\n') #Need the actual file input to be fuctional
# baseline_dic = {'FIM.py': 'd79451ce22f324fe6de47301050ca98d7ad79e3b42c6a16c617a5dcce1aaf625'} #Example hash  *Move to database for security or like the shadow file?

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
    encoded_filepath = filepath.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(encoded_filepath)
    new_hex_digest = hasher.hexdigest()

    #compares the current hash to the baseline stored in the dictionary 
    if filepath in baseline_dic:
        if new_hex_digest == baseline_dic[filepath]:
            print('\nThis file has not been changed!')
        else:
            print('\nWARNING: File has been changed *Integrity may be compromised!')
    else:
        print('\nFile not found in baseline dictionary!')

def menu():
    menu = input('\nWould you like to: A. Add this files hash to the baseline? or B. Check this files integrity?\n')

    if menu == 'A' or menu == 'a':
        baseline(filepath)
    elif menu == 'B' or menu == 'b':
        check_integrity(filepath)

menu()