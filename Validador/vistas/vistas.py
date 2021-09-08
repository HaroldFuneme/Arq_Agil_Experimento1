from flask_restful import Resource

class VistaValidador(Resource):
    
    def get(self):
        return 'Hola mundo validador', 200