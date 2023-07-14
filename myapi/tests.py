token = 'marta'
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        cursor.execute(f"SELECT restoran FROM users WHERE token='{token}'")
        user_data = cursor.fetchall()
        #return HttpResponse(f'SELECT * FROM sku_{user_data} ORDER BY id')
        print(user_data)
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение

    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse('User not found')