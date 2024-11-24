from api.models.coordinate import Coordinate
from api.models.customer import Customer

consumption_in_kwh_per_100_km = 16
velocity_in_km_per_hour = 40
rounding_decimals = 2

example_coordinate_array = [Coordinate(1, 2), Coordinate(2, 4), Coordinate(4, 6)]
#example_customer_array = [Customer(False, 1, 2, 3, 4, "1"), Customer(True, 2, 4, 6, 8, "2")


def trigger_calculation(scenario):
    vehicles = scenario.vehicles
    customers = scenario.customers
    total_distance_travelled = get_total_distance_travelled(vehicles)
    vehicle_states = get_vehicle_states(vehicles)
    total_active_time = get_total_active_time(vehicles)
    num_served = get_num_served(customers)
    num_waiting = get_num_waiting(customers)
    return total_active_time, total_distance_travelled, vehicle_states, num_served, num_waiting

def get_num_served(customers):
    return len([a for a in customers if not a.awaitingService])

def get_num_waiting(customers):
    return len([a for a in customers if a.awaitingService])

def get_vehicle_states(vehicles):
    return [v.to_json() for v in vehicles]

def get_total_active_time(vehicles):
    return sum([v.activeTime for v in vehicles])

# in kilometer: number($float)
def get_total_distance_travelled(vehicles):
    return sum([v.distanceTravelled for v in vehicles])

# in minutes
def get_time_passed():
    return 90

# in kilometer: number($float)
def get_total_distance_finished_rides():
    return 30

def getFleetData():
    carId = 1
    status = 1
    customerId = 1
    coordinate = Coordinate(1, 2)
    return {"CarId:" : carId, "Status:" : status, "CustomerId:" : customerId, "Coordinate:" : coordinate.as_tuple()}

def getFleetStatistics():
    """
    Calculates and returns fleet statistics including total consumption, productive ratio, idle ratio, and amount of customers waiting.

    Returns:
        dict: A dictionary containing the fleet statistics.

    Raises:
        Exception: If the distance of finished rides is higher than the total distance travelled.
        Exception: If the time passed is less than or equal to 0.
        Exception: If the total distance travelled is negative.
        Exception: If the car travelled faster than the set velocity.
    """
    if get_total_distance_finished_rides()>get_total_distance_travelled():
        raise Exception("The distance of finished rides cannot be higher than the total distance travelled.")
    if get_time_passed()<=0:
        raise Exception("The time passed must be bigger than 0.")
    if get_total_distance_travelled()<0:
        raise Exception("The total distance travelled cannot be negative.")
    if get_time_passed()/60*velocity_in_km_per_hour<get_total_distance_travelled():
        raise Exception("Car travelled faster than velocity is set.")
    total_consumption = (get_total_distance_travelled()*consumption_in_kwh_per_100_km)/100
    productive_ratio = get_total_distance_finished_rides()/get_total_distance_travelled() # ratio of productive driving
    idle_ratio = get_total_distance_travelled()/(get_time_passed()/60*velocity_in_km_per_hour)
    return {"Total consumption (kWh)": round(total_consumption,rounding_decimals), "Productive ratio": round(productive_ratio,rounding_decimals),
            "Idle ratio": round(idle_ratio,rounding_decimals)}

if __name__ == "__main__":
    print(getFleetData())