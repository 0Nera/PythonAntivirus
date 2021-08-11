# Python program to find SHA256 hash string of a file
import hashlib

list_hash = [
    "a300759b1e3f5e8e7996b544cdb4e5b6b2bd3ebe6d45d105ce92e86e4ee06569"
]

def init():
    try:
        filename = input("Enter the input file name: ")
        sha256_hash = hashlib.sha256()
        with open(filename,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
            for i in list_hash:
                if i == sha256_hash.hexdigest():
                    print("File is virus!")
                    break;
            print(sha256_hash.hexdigest())
            
    except Exception as e:
        print(e)
        init()


init()