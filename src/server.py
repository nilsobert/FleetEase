import json
from flask import Flask, jsonify, request

app = Flask(__name__)

vehicles = []
customers = []
fleet_statistics = []
application_statistics = []

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
 return jsonify(vehicles)

@app.route('/customers', methods=['GET'])
def get_customers():
 return jsonify(customers)

@app.route('/getFleetStatistics', methods=['GET'])
def get_fleet_statistics():
 return jsonify(fleet_statistics)

@app.route('/getApplicationStatistics', methods=['GET'])
def get_application_statistics():
 return jsonify(application_statistics)

@app.route('/updateParameters', methods=['PUT'])
def update_parameters():
 return jsonify({'message': 'parameters updated'})