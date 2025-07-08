import hashlib, time

# Proof of Concept FIM (File Integrity Monitor) 
print('Welcome to the Simple File Ingrity Monitor!')

time.sleep(1)

filepath = input('What file(s) are we monitoring? *please use the filepath ie. ~/home/user/Documents\n\n') #Need the actual file input to be fuctional
baseline_dic = {'/home/user/Documents': '11464d3b53f1b9e8ee255bcc29b599698cceed0d4f841b576fe909850e2821a5'} #Example hash  *Move to database for security or like the shadow file?

# Baseline hashing of the file(s) and/or Folder
def baseline(filepath):

    # Encodes the filepath in the utf-8 standard
    encoded_filepath = filepath.encode('utf-8')

    hasher = hashlib.sha256()

    # Update the hash object with the encoded string
    hasher.update(encoded_filepath)

    # Get the hexadecimal representation of the hash
    hex_digest = hasher.hexdigest()

    # Add baseline to baseline 'Dictionary' and if already in there it will check the integrity
    if filepath not in baseline_dic:
        baseline_dic.update({filepath:hex_digest})
        print('\nYour file has been uploaded to the Baseline!')
        print(f'\nOriginal string: {filepath}\nEncoded string (bytes): {encoded_filepath}\nSHA256 hash: {hex_digest}')
    elif filepath in baseline_dic:
        print('\nThis file is already in the baseline! Cheking integrity now...')
        check_integrity(filepath)
            
    #print(baseline_dic) #will remove/ want to have it saved to an encrypted database if possible

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