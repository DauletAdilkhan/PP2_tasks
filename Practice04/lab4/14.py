from datetime import datetime, timedelta
import re
def parse_datetime_with_tz(date_str):
    date_part, tz_part = date_str.split(' UTC')

    date = datetime.strptime(date_part, "%Y-%m-%d")

    match = re.match(r'([+-])(\d{2}):(\d{2})', tz_part)
    sign, hours, minutes = match.groups()
    
    offset = int(hours) * 3600 + int(minutes) * 60
    if sign == '-':
        offset = -offset
    
    utc_moment = date - timedelta(seconds=offset)
    
    return utc_moment

x= input()
y=input()

moment1_utc = parse_datetime_with_tz(x)
moment2_utc = parse_datetime_with_tz(y)

diff_seconds = abs((moment2_utc - moment1_utc).total_seconds())

diff_days = int(diff_seconds // 86400)

print(diff_days)
