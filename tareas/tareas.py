from os import name
from celery import Celery


celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='registrarResponseCitaMedica')
def registrarResponseCitaMedica(msj, fecha):
    with open('log_rs_citasMedicas', 'a+') as file:
        file.write('Msj: {} -  Fecha: {}'.format(msj,fecha))
