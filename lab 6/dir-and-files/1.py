import os

def list_directories_and_files(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    all_items = os.listdir(path)
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("Directories:", directories)
    print("Files:", files)
    print("All items:", all_items)


list_directories_and_files(r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 6\dir-and-files")
