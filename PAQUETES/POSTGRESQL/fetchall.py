import psycopg2

conn = psycopg2.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    with conn:
        with conn.cursor() as curs:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1,2,3),)
            entrada = input('Proporciona los id\'s a buscar (separados por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            curs.execute(sentencia, llaves_primarias)
            # "fetchall" capta todos los registros
            registros = curs.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrió un error inesperado: {e}')
finally:
    conn.close()