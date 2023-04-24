from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.post_salones_model import SalonModel
model = SalonModel()


salones_blueprint = Blueprint('salones_blueprint', __name__)


@salones_blueprint.route('/salon', methods=['PUT'])
@cross_origin()
def create_salon():
    content = model.create_salon(request.json['pabellon'], request.json['numero'])    
    return jsonify(content)

@salones_blueprint.route('/salon', methods=['PATCH'])
@cross_origin()
def update_salon():
    content = model.update_salon(request.json['codigo'], request.json['pabellon'], request.json['numero'])    
    return jsonify(content)

@salones_blueprint.route('/salon', methods=['DELETE'])
@cross_origin()
def delete_salon():
    return jsonify(model.delete_salon(request.json['codigo']))

@salones_blueprint.route('/salon', methods=['POST'])
@cross_origin()
def get_salon():
    return jsonify(model.get_salon(request.json['codigo']))

@salones_blueprint.route('/salones', methods=['POST'])
@cross_origin()
def get_salones():
    return jsonify(model.get_salones())