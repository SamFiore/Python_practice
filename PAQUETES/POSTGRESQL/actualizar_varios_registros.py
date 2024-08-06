import psycopg2

conn = psycopg2.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    with conn:
        with conn.cursor() as curs:
            sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            valores = (('Matias','Argovich','margovich@gmail.com',1),('Marge','Simpsons','msimpsons@gmail.com',2))
            curs.executemany(sentencia,valores)
            registros_actualizados = curs.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error inesperado: {e}')
finally:
    conn.close()