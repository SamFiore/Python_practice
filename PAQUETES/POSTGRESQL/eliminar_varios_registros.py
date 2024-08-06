import psycopg2

conn = psycopg2.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    with conn:
        with conn.cursor() as curs:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)
            curs.execute(sentencia,valores)
            registros_eliminados = curs.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error inesperado: {e}')
finally:
    conn.close()