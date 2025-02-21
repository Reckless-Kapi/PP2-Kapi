from datetime import datetime, timedelta

def dates():
    today = datetime.now().date()
    yest = today - timedelta(days=1)
    tomm = today + timedelta(days=1)

    print(yest)
    print(today)
    print(tomm)

dates()
