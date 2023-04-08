restoran = "greek"
try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
    # получение объекта курсора
    cursor = conn.cursor()
    # Получаем список всех пользователей
    cursor.execute('SELECT * FROM sku_' + restoran + ' ORDER BY id')
    all_items = cursor.fetchall()
    i = 0
    response = ""
    # Формируем Жсон
    response += '{"card_state":['
    for x in all_items:
        response += json.dumps({"image": all_items[i][0], "name": all_items[i][1], "name_en": all_items[i][2],
                                "name_fr": all_items[i][3], "name_cat": all_items[i][5], "desc": all_items[i][6],
                                "desc_en": all_items[i][5],
                                "desc_fr": all_items[i][6], "desc_cat": all_items[i][10],
                                "price": str(all_items[i][11]),
                                "id": str(all_items[i][13])})
        if (i != len(all_items) - 1):
            response += ','
            i += 1

    response += ']}'
    y = json.dumps(response)
    print(y)

    cursor.close()  # закрываем курсор
    conn.close()  # закрываем соединение

except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')
