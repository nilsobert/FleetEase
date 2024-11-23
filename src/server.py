import json
from flask import Flask, jsonify, request

from applicationStatistics import getApplicationStatistics
from fleetStatistics import getFleetStatistics

app = Flask(__name__)

vehicles = [1, 2, 3, 4, 5]
customers = ["Alan", "Tod", "Jane"]
fleet_statistics = []
application_statistics = []

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
 return jsonify(vehicles)

@app.route('/customers', methods=['GET'])
def get_customers():
 return jsonify(customers)

@app.route('/fleetStatistics', methods=['GET'])
def get_fleet_statistics():
 return jsonify(getFleetStatistics())

@app.route('/applicationStatistics', methods=['GET'])
def get_application_statistics():
 return jsonify(getApplicationStatistics(5))

@app.route('/updateParameters', methods=['PUT'])
def update_parameters():
 return jsonify({'message': 'parameters updated'})

if __name__ == '__main__':
 app.run(port=5000)