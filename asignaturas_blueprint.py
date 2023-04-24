from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_asignaturas_model import AsignaturaModel
model = AsignaturaModel()


asignaturas_blueprint = Blueprint('asignaturas_blueprint', __name__)


@asignaturas_blueprint.route('/asignatura', methods=['PUT'])
@cross_origin()
def create_asignatura():
    content = model.create_asignatura(request.json['nombre'], int(request.json['semestre']), 
                                request.json['carrera'])    
    return jsonify(content)

@asignaturas_blueprint.route('/asignatura', methods=['PATCH'])
@cross_origin()
def update_asignatura():
    content = model.update_asignatura(request.json['codigo'], request.json['nombre'], request.json['semestre'], 
                                request.json['carrera'])    
    return jsonify(content)

@asignaturas_blueprint.route('/asignatura', methods=['DELETE'])
@cross_origin()
def delete_asignatura():
    return jsonify(model.delete_asignatura(request.json['codigo']))

@asignaturas_blueprint.route('/asignatura', methods=['POST'])
@cross_origin()
def get_asignatura():
    return jsonify(model.get_asignatura(request.json['codigo']))

@asignaturas_blueprint.route('/asignaturas', methods=['POST'])
@cross_origin()
def get_asignaturas():
    return jsonify(model.get_asignaturas())