import hashlib
from core.db import save_file_hash, get_stored_hash, file_exists

def hash_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            encoded_filepath = content.encode('utf-8')
            hasher = hashlib.sha256()
            hasher.update(encoded_filepath)
            hex_digest = hasher.hexdigest()
        return (hex_digest)
    except FileNotFoundError:
        return(f"Error reading file: {filepath}. File does not exist.")
    
def baseline(filepath, force=False):
    file_hash = hash_file(filepath)
    
    if file_exists(filepath):
        stored_hash = get_stored_hash(filepath)

        if stored_hash == file_hash:
            return (f'Baseline for {filepath} already exists. File is unchanged.')
        elif not force:
            return 'File already exists with a different hash. Use --force to update the baseline.'
    else:
        save_file_hash(filepath, file_hash) 
        return (f'Baseline created or updated for {filepath}. Hash: {file_hash}')

def check_integrity(filepath):
    current_hash = hash_file(filepath)
    stored_hash = get_stored_hash(filepath)
    if stored_hash is None:
        return (f"This file {filepath} does not exist in the Baseline. Please run baseline first.")
    elif current_hash != stored_hash:
        return (f"WARNING: The file {filepath} has been changed *Integrity may be compromised! * Current hash: {current_hash}, Stored hash: {stored_hash}")
    else:
        return (f"No changes have been made to the file {filepath}:{stored_hash}.")

