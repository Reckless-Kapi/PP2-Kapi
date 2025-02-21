from datetime import datetime

def difference():
    print("First date: ")
    date1_str = input() 
    print("Second date: ")
    date2_str = input()

    format_str = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.strptime(date1_str, format_str)
    date2 = datetime.strptime(date2_str, format_str)

    diff_seconds = (date2 - date1).total_seconds()
    print(diff_seconds)

difference()
