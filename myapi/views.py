from django.http import HttpResponse
import psycopg2
import json

from django.shortcuts import render
from django.template import loader


# Create your views here.
# visitor menu


def getsku(request):
    restoran = request.GET.get('restoran')

    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        cursor.execute('SELECT * FROM sku_' + restoran)
        all_items = cursor.fetchall()
        i = 0
        response = ""
        # Формируем Жсон
        response += '{"card_state":['
        for x in all_items:
            response += json.dumps({"image": all_items[i][0], "name": all_items[i][1], "name_en": all_items[i][2],
                                    "name_fr": all_items[i][3], "desc": all_items[i][4], "desc_en": all_items[i][5],
                                    "desc_fr": all_items[i][6], "price": str(all_items[i][11]),
                                    "id": str(all_items[i][13])})
            if (i != len(all_items) - 1):
                response += ','
                i += 1

        response += '],"orders":[0],"orders_loc":[0],"ordersServer":[]}'
        return HttpResponse(response)

        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение

    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')


def norder(request):
    try:
        restoran = request.GET.get('restoran')
        stolik = request.GET.get('stolik')
        zakaz = request.GET.get('zakaz')
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        sql = f"INSERT INTO orders_{restoran}(stolik,zakaz) VALUES({stolik},'{zakaz}');INSERT INTO history_{restoran}(stolik,zakaz) VALUES({stolik},'{zakaz}')"
        cursor.execute(sql)
        conn.commit()
        return HttpResponse("OK")
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse('Can`t establish connection to database')


# waiter
def getorders(request):
    restoran = request.GET.get('restoran')

    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        cursor.execute('SELECT * FROM orders_'+restoran)
        all_orders = cursor.fetchall()
        i = 0
        response = ""
        # Формируем Жсон

        for x in all_orders:
            response += json.dumps({"stolik": all_orders[i][0], "zakaz": all_orders[i][1], "id": all_orders[i][2]})
            response += ";"
            i += 1

        return HttpResponse(response)

        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')


def deleteid(request):
    try:
        restoran = request.GET.get('restoran')
        id = request.GET.get('id')
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        sql = f"DELETE FROM orders_{restoran} WHERE id={id}"
        cursor.execute(sql)
        conn.commit()
        return HttpResponse("OK")
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse('Can`t establish connection to database')


def deleteall(request):
    try:
        restoran = request.GET.get('restoran')
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        sql = f"DELETE FROM orders_{restoran}"
        cursor.execute(sql)
        conn.commit()
        return HttpResponse("OK")
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse('Can`t establish connection to database')


def redact(request):
    try:
        restoran = request.GET.get('restoran')
        id = request.GET.get('id')
        zakaz = request.GET.get('zakaz')
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        sql = f"UPDATE orders_{restoran} SET zakaz = '{zakaz}' WHERE id IN({id})"
        cursor.execute(sql)
        conn.commit()
        return HttpResponse("OK")
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse('Can`t establish connection to database')


def index(response):
    return render(response, 'main/base.html', {"name": "john"})


def addform(request):
    restoran = request.GET.get('restoran')
    return render(request, 'main/addform.html', {"test":restoran})
def add(request):
    restoran = request.GET.get('restoran')
    image = request.GET.get('image')
    name = request.GET.get('name')
    name_en = request.GET.get('name_en')
    desc = request.GET.get('desc')
    desc_en = request.GET.get('desc_en')
    price = request.GET.get('price')
    category = request.GET.get('category')
    return HttpResponse(image)


