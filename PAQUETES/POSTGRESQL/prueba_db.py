import psycopg2

conexion = psycopg2.connect(dbname='put_db',user='put_user',password='put_psw',host='put_host',port=7777)

#Un cursor es un objeto que nos va a permitir ejecutar secuencias SQL en postgres
cursor = conexion.cursor()
#Definir la sentencia
sentencia = 'SELECT * FROM persona'
#Ejecuta la sentencia
cursor.execute(sentencia)
#Almacenar una lista de los registros
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()