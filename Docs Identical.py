import hashlib

def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as file:
        while chunck := file.read(1024):
            h.update(chunck)
    return h.hexdigest()

msg1 = hash_file(r"C:\Users\qossa\OneDrive\Desktop\Del\1.txt")
msg2 = hash_file(r"C:\Users\qossa\OneDrive\Desktop\Del\3.txt")

if msg1 != msg2:
    print("File are not same")
else:
    print("File content Matched")
    
