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

# Flask route to update shared data
@app.route('/send_message', methods=['POST'])
def send_message():
    global synchronizer
    data = request.json
    message = data.get("message")
    
    if not message:
        return jsonify({"error": "Message is required"}), 400
    
    
    return jsonify({"status": "Message received"}), 200

def create_app():

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

    @app.route('/fleetData', methods=['GET'])
    def get_fleet_data():
        return jsonify(getFleetData())

    @app.route('/test_streaming')
    def test_streaming():
        def generate():
            for i in range(100000):
                time.sleep(1)
                # Yield a JSON object as a string
                yield json.dumps({"value": i}) + "\n"

        return app.response_class(generate(), mimetype='application/json')

    return app
