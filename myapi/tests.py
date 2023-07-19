token = 'marta'

# пытаемся подключиться к базе данных
conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
# получение объекта курсора
cursor = conn.cursor()
# Получаем список всех пользователей
cursor.execute(f"SELECT restoran FROM users WHERE token='{token}'")
user_data = cursor.fetchall()
# return HttpResponse(f'SELECT * FROM sku_{user_data} ORDER BY id')
str = str(user_data)
print(str[3:len(str)-4])
cursor.close()  # закрываем курсор
conn.close()  # закрываем соединение
