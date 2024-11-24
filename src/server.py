import json
import time
from flask import Flask, jsonify, request
#from api.src.systemStatistics import getApplicationStatistics
from fleetStatistics import getFleetStatistics, getFleetData
from synchronizer import Synchronizer
import threading

app = Flask(__name__)

# Shared data and lock
global synchronizer
synchronizer = Synchronizer()
data_lock = threading.Lock()


@app.route('/car_state', methods=['GET'])
def get_car_state():
    global synchronizer
    return jsonify(synchronizer.fleet.vehicles_states)

@app.route('/service', methods=['GET'])
def get_arrivals():
    global synchronizer
    num_waiting = synchronizer.fleet.num_waiting
    num_served = synchronizer.fleet.num_served
    out = {
        "num_waiting": num_waiting,
        "num_served": num_served
    }
    return jsonify(out)

@app.route('/consumption', methods=['GET'])
def get_consumption():
    global synchronizer
    total_active_time = synchronizer.fleet.total_active_time
    energy_consumed_total = synchronizer.fleet.energy_consumed_total
    total_distance_travelled = synchronizer.fleet.total_distance_travelled
    out = {
        "total_active_time":total_active_time,
        "energy_consumed_total":energy_consumed_total,
        "total_distance_travelled":total_distance_travelled
    }
    return jsonify(out)

@app.route('/system', methods=['GET'])
def get_system():
    global synchronizer
    return jsonify(synchronizer.system)

