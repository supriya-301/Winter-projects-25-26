from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import json


vehicle = connect('127.0.0.1:14550', wait_ready=True)


def arm_and_takeoff(target_alt):
    print("Arming...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    print("Taking off...")
    vehicle.simple_takeoff(target_alt)

    while True:
        alt = vehicle.location.global_relative_frame.alt
        print("Altitude:", alt)
        if alt >= target_alt * 0.95:
            print("Reached altitude")
            break
        time.sleep(1)


def get_waypoints(command):

    if "square" in command:
        return {
            "waypoints": [
                {"north": 25, "east": 0, "alt": 10},
                {"north": 25, "east": 25, "alt": 10},
                {"north": 0, "east": 25, "alt": 10},
                {"north": 0, "east": 0, "alt": 10}
            ]
        }

    elif "north" in command:
      
    elif "pole" in command:
        return {
            "waypoints": [
                {"north": 25, "east": 0, "alt": 10},
                {"north": 25, "east": 25, "alt": 10},
                {"north": 0, "east": 25, "alt": 10},
                {"north": 0, "east": 0, "alt": 10}
            ]
        }

    elif "ground level" in command:
        return {
            "waypoints": [
                {"north": 25, "east": 0, "alt": 0},
                {"north": 25, "east": 25, "alt": 0},
                {"north": 0, "east": 25, "alt": 0},
                {"north": 0, "east": 0, "alt": 0}
            ]
        }

    else:
        return {"waypoints": [{"north": 0, "east": 0, "alt": 10}]}

def validate_waypoints(data):
    for wp in data["waypoints"]:
        if wp["alt"] <= 0:
            return False, "Altitude too low"
        if abs(wp["north"]) > 100 or abs(wp["east"]) > 100:
            return False, "Waypoint too far"

    return True, "OK"

def execute_mission(waypoints):
    home = vehicle.location.global_frame

    for i, wp in enumerate(waypoints):
        print(f"Going to waypoint {i+1}")

        target = LocationGlobalRelative(
            home.lat + wp["north"] * 1e-5,
            home.lon + wp["east"] * 1e-5,
            wp["alt"]
        )

        vehicle.simple_goto(target)
        time.sleep(8)

if __name__ == "__main__":
    cmd = input("Enter command: ")

    data = get_waypoints(cmd)

    print("Generated waypoints:", json.dumps(data, indent=2))

    valid, msg = validate_waypoints(data)

    if not valid:
        print("Safety check failed:", msg)
    else:
        print("Safety passed")

        arm_and_takeoff(10)

        execute_mission(data["waypoints"])

        print("Returning home...")
        vehicle.mode = VehicleMode("RTL")

        time.sleep(10)
        vehicle.close()












      
        return {"waypoints": [{"north": 25, "east": 0, "alt": 10}]}
