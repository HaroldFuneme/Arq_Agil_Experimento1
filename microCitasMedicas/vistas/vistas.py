from flask_restful import Resource

class VistaAgendarCita(Resource):

    def get(self):
        return 'Hola mundo', 200