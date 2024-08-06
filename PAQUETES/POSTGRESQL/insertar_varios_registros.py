import psycopg2

conn = psycopg2.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    with conn:
        with conn.cursor() as curs:
            # Sentencia = Query
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores = (('Martin','Ram','mram@gmail.com'),('Armando','Rolfin','arolfin@gmail.com'),('Juan','Kalavsnicov','jkalavsnicov@gmail.com'))
            # La función 'executemany' permite ejecutar una sentencia con varios valores
            curs.executemany(sentencia,valores)
            registros_insertados = curs.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error inesperado: {e}')
finally:
    conn.close()