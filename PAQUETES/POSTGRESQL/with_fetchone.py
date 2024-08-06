import psycopg2

conn = psycopg2.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

try:
    with conn:
        with conn.cursor() as curs:
            #Para pasar un parametro debemos poner "%s" (parámetro posicional / PlaceHolder)
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = int(input('Proporciona el valor de id_persona: '))
            #Tenemos que pasar una tupla
            curs.execute(sentencia, (id_persona,))
            # "fetchall" capta todos los registros
            # "fetchone" capta un solo registro
            registros = curs.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error inesperado: {e}')
finally:
    conn.close()