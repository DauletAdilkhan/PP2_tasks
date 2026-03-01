from datetime import datetime, timedelta
import re

def to_utc(dt_str):
    # Разделяем дату-время и часовой пояс
    dt_part, tz_part = dt_str.split(' UTC')
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    
    # Парсим часовой пояс
    match = re.match(r'([+-])(\d{2}):(\d{2})', tz_part)
    sign, hours, minutes = match.groups()
    
    # Смещение в секундах
    offset = int(hours) * 3600 + int(minutes) * 60
    if sign == '-':
        offset = -offset
    
    # Переводим в UTC
    return dt - timedelta(seconds=offset)

# Читаем
start = to_utc(input().strip())
end = to_utc(input().strip())

# Разница в секундах
diff = int((end - start).total_seconds())
print(diff)