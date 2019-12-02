from datetime import datetime, date, timedelta

# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime


date_string ="01/01/17 12:10:03.234567"
dt_now = datetime.today()
dt_now = dt_now.strftime('%d-%m-%y')
print (dt_now)
dt_now = datetime.today()
dt_yesterday=date.today() - timedelta(days=1)
print(dt_yesterday)
dt_30days_ago=date.today() - timedelta(days=30)
print(dt_30days_ago)
dt_str= datetime.strptime(date_string , '%d/%m/%y %H:%M:%S.%f')
print(dt_str)
