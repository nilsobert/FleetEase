from flask import Flask, request, jsonify
import threading
import time
from algo import Assigner
from api.api import API
import asyncio

app = Flask(__name__)

# Shared data and lock
shared_data = {"message": None}
data_lock = threading.Lock()

# Worker thread function
def assignement_worker(scenario, vehicles, customers, api, algorithm="basic"):
    global shared_data
    assigner = Assigner(scenario=scenario, vehicles=vehicles, customers=customers, api=api, algorithm=algorithm)
    while True:
        with data_lock:
            if shared_data["message"]:
                print(f"Worker received message: {shared_data['message']}")
                # Clear the message after processing
                shared_data["message"] = None
        time.sleep(1)  # Prevent busy-waiting

# Flask route to update shared data
@app.route('/send_message', methods=['POST'])
def send_message():
    global shared_data
    data = request.json
    message = data.get("message")
    
    if not message:
        return jsonify({"error": "Message is required"}), 400
    
    with data_lock:
        shared_data["message"] = message
    
    return jsonify({"status": "Message received"}), 200

def init():
    print("Initializing api...")
    api = API()
    num_vehicles = 10
    num_customers = 35
    scenario, vehicles, customers = asyncio.run(api.create_and_query_scenario(num_of_customers = num_customers, num_of_vehicles = num_vehicles))
    asyncio.run(api.launch_scenario(speed=0.5, scenario=scenario))
    print("    finished")
    return scenario, vehicles, customers, api


if __name__ == "__main__":
    scenario, vehicles, customers, api = init()
    # Start the worker thread
    thread = threading.Thread(target=assignement_worker, args=(scenario, vehicles, customers, api))
    thread.start()

    # Start the Flask server
    app.run(debug=True)
