# Python program to find SHA256 hash string of a file
import hashlib
import os

list_hash = []

with open("list", "r") as ins:
    for line in ins:
        list_hash.append(line)

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
            print("SHA256: ", sha256_hash.hexdigest())
            
    except Exception as e:
        print(e)
        init()

list = os.listdir("./virus/")
number_files = len(list)
print("Infected: ", number_files)
print("Database: ", len(list_hash))


init()