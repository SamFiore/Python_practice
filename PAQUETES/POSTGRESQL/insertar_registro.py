import psycopg2

conn = psycopg2.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    with conn:
        with conn.cursor() as curs:
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores = ('Carlos','Alfonsin','calfonsin@gmail.com')
            curs.execute(sentencia,valores)
            # La función 'commit' guarda los cambios en la base de datos
            # conn.commit() Al usar with, la función se ejecuta automaticamente
            registros_insertados = curs.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error inesperado: {e}')
finally:
    conn.close()