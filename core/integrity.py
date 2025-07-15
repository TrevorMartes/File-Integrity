import hashlib
from core.db import save_file_hash, get_stored_hash, file_exists

def hash_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
    except Exception as e:
        raise FileNotFoundError(f"Error reading file: {e}")
    
def baseline(filepath, force=False):
    file_hash = hash_file(filepath)
    
    if file_exists(filepath):
        stored_hash = get_stored_hash(filepath)

        if stored_hash == file_hash:
            return 'Baseline already exists. File is unchanged.'
        elif not force:
            return 'File already exists with a different hash. Use --force to update the baseline.'

    save_file_hash(filepath,file_hash)
    return "Baseline hash stored: '{filepath}:{file_hash}'"

def check_integrity(filepath):
    current_hash = hash_file(filepath)
    stored_hash = get_stored_hash(filepath)
    if stored_hash is None:
        return "This file {filepath} does not exist in the Baseline. Please run baseline first."
    elif current_hash != stored_hash:
        return "WARNING: The file {filepath} has been changed *Integrity may be compromised!"
    else:
        return "No changes have been made to the file {filepath}."

