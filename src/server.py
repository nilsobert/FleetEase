import json
import time
from flask import Flask, jsonify, request
from src.systemStatistics import getApplicationStatistics
from fleetStatistics import getFleetStatistics, getFleetData
from synchronizer import Synchronizer
import threading

app = Flask(__name__)

# Shared data and lock
synchronizer = Synchronizer()
data_lock = threading.Lock()

def create_app():
    global synchronizer
    fleet = synchronizer.fleet
    scenario = synchronizer.fleet.scenario()
    vehicles = scenario.vehicles
    customers = scenario.customers
    system = synchronizer.system

    @app.route('/vehicles', methods=['GET'])
    def get_vehicles():
        return jsonify(vehicles)

    @app.route('/customers', methods=['GET'])
    def get_customers():
        return jsonify(customers)

    @app.route('/fleetStatistics', methods=['GET'])
    def get_fleet_statistics():
        return fleet.to_json()

    @app.route('/applicationStatistics', methods=['GET'])
    def get_application_statistics():
        return system.to_json()

    @app.route('/fleetData', methods=['GET'])
    def get_scenario_data():
        return scenario.to_json()

    return app
