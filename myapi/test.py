import psycopg2

restoran = "greek"
stolik = 55
zakaz = "miasa"
# пытаемся подключиться к базе данных
conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
# получение объекта курсора
cursor = conn.cursor()
# Получаем список всех пользователей
sql = f"INSERT INTO orders_{restoran}(stolik,zakaz) VALUES({stolik},'{zakaz}');INSERT INTO history_{restoran}(stolik,zakaz) VALUES({stolik},'{zakaz}')"
cursor.execute(sql)
conn.commit()
print('ok')
cursor.close()  # закрываем курсор
conn.close()  # закрываем соединение
