import psycopg2

try:
        conn = psycopg2.connect(dbname='users', user='myuser', password='123456', host='localhost')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM my_users')
        all_items = cursor.fetchall()
        print(all_items)
	#return HttpResponse(all_items)
        cursor.close()
        conn.close()
except:
        print('Can`t establish connection to database')
