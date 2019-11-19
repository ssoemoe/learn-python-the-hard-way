from datetime import datetime, timedelta

current_utc = datetime.utcnow()
for i in range(0, 100):
    print(current_utc + timedelta(hours=i))