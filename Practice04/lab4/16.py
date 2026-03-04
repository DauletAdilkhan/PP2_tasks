from datetime import datetime, timedelta
import re

def to_utc(dt_str):
    dt_part, tz_part = dt_str.split(' UTC')
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    
    
    match = re.match(r'([+-])(\d{2}):(\d{2})', tz_part)
    sign, hours, minutes = match.groups()
    
    offset = int(hours) * 3600 + int(minutes) * 60
    if sign == '-':
        offset = -offset
    
    return dt - timedelta(seconds=offset)

start = to_utc(input().strip())
end = to_utc(input().strip())

diff = int((end - start).total_seconds())
print(diff)