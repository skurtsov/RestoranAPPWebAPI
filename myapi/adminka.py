from django.http import HttpResponse
import psycopg2
import json
import hashlib
from django.shortcuts import render,redirect
from django.template import loader
from .forms import ResumeForm
from .forms import DrinkForm
import os

# Create your views here.
# visitor menu
def auth(request):
    username="marta"
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='restoran', user='myuser', password='S53em4e10', host='localhost')
        # получение объекта курсора
        cursor = conn.cursor()
        # Получаем список всех пользователей
        cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
        user_data = cursor.fetchall()
        return HttpResponse(user_data)

        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение

    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return HttpResponse('User not found')