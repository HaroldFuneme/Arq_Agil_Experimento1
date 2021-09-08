
from flask_restful import Resource
from datetime import datetime
from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='registrarResponseCitaMedica')
def registrarResponseCitaMedica(*args):
    pass

class VistaAgendarCita(Resource):
    
    def get(self):
        args=('Mensaje preuba', datetime.utcnow())
        registrarResponseCitaMedica.apply_async(args=args, queue ='logs')
        return 'Hola mundo', 200