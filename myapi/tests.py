from django.http import HttpResponse
import psycopg2
import os

def getskuid(request):
    restoran = 'greek'
    id = 1
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        cursor.execute(f'SELECT * FROM sku_{restoran} WHERE id={id}' )
        all_items = cursor.fetchall()

        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
        print(all_items)

    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
       print(f'SELECT * FROM sku_{restoran} WHERE id={id}')
