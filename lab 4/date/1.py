from datetime import datetime, timedelta

def subtraction():
    today = datetime.now().date()
    new_date = today - timedelta(days=5)
    print(new_date)

subtraction()
