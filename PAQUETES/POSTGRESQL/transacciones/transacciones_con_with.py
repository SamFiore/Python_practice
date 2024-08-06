import psycopg2 as bd

conn = bd.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    with conn:
        with conn.cursor() as curs:
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores = ('Mariana','Kawasaki','mkawasaki@gmail.com')
            curs.execute(sentencia,valores)
            sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona = %s'
            valores = ('Vanessa','Doofersmith','Vdoofersmith@gmail.com',2)
            curs.execute(sentencia, valores)
            print('Termino la ejecucion, se hizo commit')
except Exception as e:
    conn.rollback()
    print(f'Ocurrió un error inesperado, se hizo rollback: {e}')
finally:
    conn.close()