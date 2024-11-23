from api.api import API
import algo
import fleetStatistics
import applicationStatistics
import server
import threading
import time

lock = threading.Lock()

def run_server():
    app = server.create_app()
    app.run(port=5000, use_reloader=False)

def start_algorithm():
    pass

def calculate_stats():
    pass

def main():
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    print("Server started. Main program running...")

    try:
        while True:
            start_algorithm()
            calculate_stats()

            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down main program.")


if __name__ == "__main__":
    main()