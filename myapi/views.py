from django.http import HttpResponse
import psycopg2
import json
import hashlib
from django.shortcuts import render
from django.template import loader
from .forms import ResumeForm
import os

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
        cursor.execute('SELECT * FROM sku_' + restoran+' ORDER BY id')
        all_items = cursor.fetchall()
        i = 0
        response = ""
        # Формируем Жсон
        response += '{"card_state":['
        for x in all_items:
            response += json.dumps({"image": all_items[i][0], "name": all_items[i][1], "name_en": all_items[i][2],
                                    "name_fr": all_items[i][3],"name_cat": all_items[i][5], "desc": all_items[i][6], "desc_en": all_items[i][5],
                                    "desc_fr": all_items[i][6],"desc_cat": all_items[i][10], "price": str(all_items[i][11]),
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
        response = "["
        # Формируем Жсон

        for x in all_orders:
            response += json.dumps({"stolik": all_orders[i][0], "zakaz": all_orders[i][1], "id": all_orders[i][2],})
            if i<len(all_orders)-1:
                response += ","
            i += 1
        response+="]"
        return HttpResponse(response)

        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')
def getordersweb(request):
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
        response=""
        # Формируем Жсон
        for x in all_orders:
            response += json.dumps({"stolik": all_orders[i][0], "zakaz": all_orders[i][1], "id": all_orders[i][2],})
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


def redactid(request):
    restoran = request.GET.get('restoran')
    id = request.GET.get('id')
    zakaz = request.GET.get('zakaz')
    try:
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
        conn.close()
    except:
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
def getuser(request):
    user = request.GET.get('username')
    password = request.GET.get('password')
    result = hashlib.md5(password.encode())
    password = result.hexdigest()
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        cursor.execute(f"SELECT restoran,token FROM users WHERE username='{user}' AND PASSWORD='{password}'")
        all_items = cursor.fetchall()
        response='{"restoran":"'+all_items[0][0]+'","token":"'+all_items[0][1]+'"}'
        return HttpResponse(response)

        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение

    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse(f"SELECT restoran,token FROM users WHERE username='{user}' AND PASSWORD='{password}'")


def newuser(request):
    try:
        nombre = request.GET.get('nombre')
        cafe = request.GET.get('cafe')
        tel = request.GET.get('tel')
        email = request.GET.get('mail')
        ciudad = request.GET.get('ciudad')
        adress = request.GET.get('adress')
        camareros = request.GET.get('camareros')
        mesas = request.GET.get('mesas')
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        sql = f"INSERT INTO users_requests(nombre ,cafe , tel , email , ciudad , adress , camareros , mesas ) VALUES('{nombre}','{cafe}','{tel}','{email}','{ciudad}','{adress}',{camareros},{mesas})"
        cursor.execute(sql)
        conn.commit()
        return HttpResponse("OK")
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse('Can`t establish connection to database')

def addform(request):
    if request.method == 'POST':
        restoran = request.GET.get('restoran')
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            name = request.POST['name']
            if file != None:
                if(os.path.exists(f"media/{restoran}")!=True):
                    os.makedirs(f"media/{restoran}")
                filename = os.path.join(f'media/{restoran}', file.name)
                with open(filename, 'wb') as f:
                    f.write(file.read())
                name = request.POST['name']
                name_en = request.POST['name_en']
                name_cat = request.POST['name_cat']
                desc = request.POST['desc']
                desc_en = request.POST['desc_en']
                desc_cat = request.POST['desc_cat']
                price = request.POST['price']
                cat = request.POST['category']
                link= f"https://reactive-cafe.com/media/{restoran}/{file.name}"
                sql = f"INSERT INTO sku_{restoran}(image,name,name_en,name_cat,descr,descr_en,descr_cat,price,cat,isactive ) VALUES('{link}','{name}','{name_en}','{name_cat}','{desc}','{desc_en}','{desc_cat}',{price},'{cat}',TRUE)"
                conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
                # получение объекта курсора
                cursor = conn.cursor()
                # Получаем список всех пользователей
                cursor.execute(sql)
                conn.commit()
                return HttpResponse("OK")
                cursor.close()  # закрываем курсор
                conn.close()  # закрываем соединение
                return HttpResponse(sql)
            else:

                name = request.POST['name']
                name_en = request.POST['name_en']
                name_cat = request.POST['name_cat']
                desc = request.POST['desc']
                desc_en = request.POST['desc_en']
                desc_cat = request.POST['desc_cat']
                price = request.POST['price']
                cat = request.POST['category']

                sql = f"INSERT INTO sku_{restoran}(image,name,name_en,name_cat,descr,descr_en,descr_cat,price,cat,isactive ) VALUES('','{name}','{name_en}','{name_cat}','{desc}','{desc_en}','{desc_cat}',{price},'{cat}',TRUE)"
                conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
                # получение объекта курсора
                cursor = conn.cursor()
                # Получаем список всех пользователей
                cursor.execute(sql)
                conn.commit()
                return HttpResponse("OK")
                cursor.close()  # закрываем курсор
                conn.close()  # закрываем соединение
                return HttpResponse(sql)
    else:
        form = ResumeForm
    return render(request, 'main/addform.html', {'form': form, 'test':'parapa'})
def redactbyid(request):
    restoran = request.GET.get('restoran')
    id = request.GET.get('id')
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
        if request.method == 'POST':
            restoran = request.GET.get('restoran')
            form = ResumeForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES.get('file')
                if file != None:
                    name = request.POST['name']
                    if (os.path.exists(f"media/{restoran}") != True):
                        os.makedirs(f"media/{restoran}")
                    filename = os.path.join(f'media/{restoran}', file.name)
                    with open(filename, 'wb') as f:
                        f.write(file.read())
                    name = request.POST['name']
                    name_en = request.POST['name_en']
                    name_en = request.POST['name_cat']
                    desc = request.POST['desc']
                    desc_en = request.POST['desc_en']
                    desc_cat = request.POST['desc_cat']
                    price = request.POST['price']
                    cat = request.POST['category']
                    link = f"https://reactive-cafe.com/media/{restoran}/{file.name}"
                    sql = f"UPDATE sku_{restoran} SET image ='{link}' WHERE id={id}"
                    #sql = f"INSERT INTO sku_{restoran}(image,name,name_en,name_fr,name_de,name_cat,descr,descr_en,descr_fr,descr_de,descr_cat,price,cat,isactive ) VALUES('{link}','{name}','{name_en}','{name_en}','{name_en}','{name_en}','{desc}','{desc_en}','{desc_en}','{desc_en}','{desc_en}',{price},'{cat}',TRUE)"
                    conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
                    # получение объекта курсора
                    cursor = conn.cursor()
                    # Получаем список всех пользователей
                    cursor.execute(sql)
                    conn.commit()

                    cursor.close()  # закрываем курсор
                    conn.close()  # закрываем соединение
                    return HttpResponse("Not None")
                else:
                    return HttpResponse("None")
        else:
            form = ResumeForm
        return render(request, 'main/redactform.html', {'form': form, 'name': all_items[0][1],'name_en': all_items[0][2],'name_cat':all_items[0][5],'desc': all_items[0][3],'desc_en': all_items[0][4],'desc_cat': all_items[0][10],'price': all_items[0][11],'category': all_items[0][12],})

    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse(f"UPDATE sku_{restoran} SET image ={link} WHERE id={id}")


def add(request):
    name = request.POST['ff']
    return  HttpResponse(name)
def website(request):
    return render(request, 'main/index.html')