from datetime import datetime
import math

today = datetime.today()
break_time = datetime(today.year, today.month, today.day, 12)
minutes =  math.ceil((break_time - today).total_seconds() / 60)
if minutes <= 0:
    print('C\'est l\'heure de la pause !')
else:
    print(f'il reste {minutes} avant la pause')