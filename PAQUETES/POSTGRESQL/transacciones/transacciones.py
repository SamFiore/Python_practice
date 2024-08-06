import psycopg2 as bd

conn = bd.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    # conn.autocommit = False
    curs = conn.cursor()
    sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    valores = ('Maribel','Imawaka','mimawaka@gmail.com')
    curs.execute(sentencia,valores)
    sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona = %s'
    valores = ('Dr.','Doofersmith','doofersmith_malvados_y_asociados@gmail.com',1)
    curs.execute(sentencia, valores)
    conn.commit()
    print('Termino la ejecucion, se hizo commit')
except Exception as e:
    conn.rollback()
    print(f'Ocurrió un error inesperado, se hizo rollback: {e}')
finally:
    conn.close()