import logging as log

# HANDLER = Manejador, es un recurso donde se manda la información
# asctime = Tiempo del lanzamiento
# levelname = Nombre del nivel
# filename = Nombre del archivo
# lineno = Número de línea
# datefmt = Formato de fecha y hora (%I=Horas,%M=Minutos,%S=Segundos,%p=AM/PM)
log.basicConfig(level=log.DEBUG,format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',datefmt='%I:%M:%S %p', handlers=[log.FileHandler('capa_datos.log'),log.StreamHandler()])

if __name__ == '__main__':
    log.debug('Mensaje a nivel DEBUG')
    log.info('Mensaje a nivel de INFO')
    log.warning('Mensaje a nivel de WARNING')
    log.error('Mensake a nivel ERROR')
    log.critical('Mensaje a nivel CRITICAL')
