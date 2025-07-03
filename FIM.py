import hashlib, cryptography


filepath = input("What file(s) are we monitoring? *please use the filepath ie. ~/home/user/Documents\n\n")
baseline_dic = {}

#baseline hashing of the file(s) and/or Folder
def baseline(filepath):
    encoded_filepath = filepath.encode('utf-8')
    hasher = hashlib.sha256()

    # Update the hash object with the encoded string
    hasher.update(encoded_filepath)

    # Get the hexadecimal representation of the hash
    hex_digest = hasher.hexdigest()

    # Add baseline to baseline 'Dictionary'
    if filepath not in baseline_dic:
        baseline_dic.update({filepath:hex_digest})

    print(baseline_dic) #will remove after done with baseline/ want to have it saved to an encrypted file if possible

    print(f"\nOriginal string: {filepath}")
    print(f"Encoded string (bytes): {encoded_filepath}")
    print(f"SHA256 hash: {hex_digest}")

#comparing baseline to the current hash
def check_integrity(filepath):
    encoded_filepath = filepath.encode('utf-8')
    hasher = hashlib.sha256()
    # Update the hash object with the encoded string
    hasher.update(encoded_filepath)
    # Get the hexadecimal representation of the hash
    new_hex_digest = hasher.hexdigest()

    #compares the current hash to the baseline stored in the dictionary 
    if new_hex_digest in baseline_dic.values():
        print('This file has not been changed!')
    else:
        print('WARNING: File has been changed *Integrity may be compromised!')

baseline(filepath) #will put into a for loop/if statement to have if they choose baseline or compare to baseline.

check_integrity(filepath) #will put into a for loop/if statement to have if they choose baseline or compare to baseline.
