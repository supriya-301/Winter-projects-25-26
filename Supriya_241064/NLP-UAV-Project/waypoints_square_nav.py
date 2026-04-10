from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    print("Arming...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    print("Taking off...")
    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        alt = vehicle.location.global_relative_frame.alt
        print("Altitude:", alt)
        if alt >= aTargetAltitude * 0.95:
            print("Reached altitude")
            break
        time.sleep(1)

arm_and_takeoff(10)

d = 0.0003

lat = vehicle.location.global_frame.lat
lon = vehicle.location.global_frame.lon

points = [
    (lat + d, lon),
    (lat + d, lon + d),
    (lat, lon + d),
    (lat, lon)
]

for i, (lat_i, lon_i) in enumerate(points):
    print(f"Going to point {i+1}")
    wp = LocationGlobalRelative(lat_i, lon_i, 10)
    vehicle.simple_goto(wp)
    time.sleep(10)
  
print("Ready to land")
vehicle.mode = VehicleMode("RTL")

time.sleep(20)

vehicle.close()
    time.sleep(10)
