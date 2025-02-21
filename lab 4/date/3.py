from datetime import datetime

def microseconds():
    now = datetime.now()
    no_microseconds = now.replace(microsecond=0) 
    print( no_microseconds)

microseconds()
