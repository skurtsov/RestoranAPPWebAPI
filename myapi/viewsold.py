from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index(request):
    try:
        conn = psycopg2.connect(dbname='users', user='myuser', password='123456', host='localhost')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_users')
        all_items = cursor.fetchall()
        return HttpResponse(all_items)
        cursor.close()
        conn.close()
    except:
        return HttpResponse('Can`t establish connection to dbq')


