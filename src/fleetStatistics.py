from api.models.coordinate import Coordinate
from api.models.customer import Customer

consumption_in_kwh_per_100_km = 16
velocity_in_km_per_hour = 40
rounding_decimals = 2

example_coordinate_array = [Coordinate(1, 2), Coordinate(2, 4), Coordinate(4, 6)]
#example_customer_array = [Customer(False, 1, 2, 3, 4, "1"), Customer(True, 2, 4, 6, 8, "2")


# in kilometer: number($float)
def get_total_distance_travelled():
    return 40

# in minutes
def get_time_passed():
    return 90

# in kilometer: number($float)
def get_total_distance_finished_rides():
    return 30

def get_amount_of_customers_waiting():
    return 0

def get_routePlans():
    return []

def get_fleet_data():
    carId = 1
    status = 1
    customerId = 1
    coordinate = Coordinate(1, 2)
    return {"CarId:" : carId, "Status:" : status, "CustomerId:" : customerId, "Coordinate:" : coordinate}

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
            "Idle ratio": round(idle_ratio,rounding_decimals), "Amount of customers waiting": get_amount_of_customers_waiting()}

if __name__ == "__main__":
    print(getFleetStatistics())