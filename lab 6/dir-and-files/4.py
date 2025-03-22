def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines() 
            print(f" File: {file_path}")
            print(f" Total lines: {len(lines)}")
    except FileNotFoundError:
        print(f" Error: File not found - {file_path}")
    except Exception as e:
        print(f" An error occurred: {e}")

file_path = r"C:\Users\kasym\Documents\Kapi Labs for PP\lab 6\dir-and-files\test.txt"
count_lines(file_path)
