import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f" File deleted: {file_path}")
            except Exception as e:
                print(f" Error while deleting the file: {e}")
        else:
            print(" No write permission for this file.")
    else:
        print(" File does not exist.")

file_to_delete = r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 6\dir-and-files\copy.txt"
delete_file(file_to_delete)
