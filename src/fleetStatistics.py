consumption_in_kwh_per_km = 16
velocity_in_km_per_hour = 40
rounding_decimals_for_ratios = 2

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

def getStatistics():
    if get_total_distance_finished_rides()>get_total_distance_travelled():
        raise Exception("The distance of finished rides cannot be higher than the total distance travelled.")
    if get_time_passed()<=0:
        raise Exception("The time passed must be bigger than 0.")
    if get_total_distance_travelled()<0:
        raise Exception("The total distance travelled cannot be negative.")
    if get_time_passed()/60*velocity_in_km_per_hour<get_total_distance_travelled():
        raise Exception("Car travelled faster than velocity is set.")
    total_consumption = get_total_distance_travelled()*consumption_in_kwh_per_km
    productive_ratio = get_total_distance_finished_rides()/get_total_distance_travelled() # ratio of productive driving
    idle_ratio = get_total_distance_travelled()/(get_time_passed()/60*velocity_in_km_per_hour)
    return {"Total consumption (kWh)": total_consumption, "Productive ratio": round(productive_ratio,rounding_decimals_for_ratios),
            "Idle ratio": round(idle_ratio,rounding_decimals_for_ratios), "Amount of customers waiting": get_amount_of_customers_waiting()}

if __name__ == "__main__":
    print(getStatistics())