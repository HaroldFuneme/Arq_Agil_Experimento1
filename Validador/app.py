from Validador.vistas.vistas import VistaValidador
from Validador import create_app
from flask_restful import Resource, Api
from flask import Flask, request
# import requests


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaValidador, '/validar')
