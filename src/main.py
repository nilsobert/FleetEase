from flask import Flask, request, jsonify
import threading
import time
from algo import Assigner
from api.api import API
import asyncio
from synchronizer import Synchronizer

app = Flask(__name__)

# Shared data and lock
synchronizer = Synchronizer()
data_lock = threading.Lock()

# Worker thread function
def assignement_worker(scenario, vehicles, customers, api, algorithm="basic"):
    global synchronizer
    assigner = Assigner(scenario=scenario, vehicles=vehicles, customers=customers, api=api, algorithm=algorithm)
    assigner.assign(synchronizer, data_lock)
    time.sleep(1)  # Prevent busy-waiting

# Flask route to update shared data
@app.route('/send_message', methods=['POST'])
def send_message():
    global synchronizer
    data = request.json
    message = data.get("message")
    
    if not message:
        return jsonify({"error": "Message is required"}), 400
    
    
    return jsonify({"status": "Message received"}), 200

def init():
    print("Initializing api...")
    api = API()
    num_vehicles = 30
    num_customers = 70
    scenario, vehicles, customers = asyncio.run(api.create_and_query_scenario(num_of_customers = num_customers, num_of_vehicles = num_vehicles))
    asyncio.run(api.launch_scenario(speed=0.1, scenario=scenario))
    print("    finished")
    return scenario, vehicles, customers, api


if __name__ == "__main__":
    scenario, vehicles, customers, api = init()
    # Start the worker thread
    thread = threading.Thread(target=assignement_worker, args=(scenario, vehicles, customers, api))
    thread.start()
    time.sleep(2)

    # Start the Flask server
    app.run(debug=True)
