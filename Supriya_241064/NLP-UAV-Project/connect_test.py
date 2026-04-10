from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

vehicle = connect('127.0.0.1:14550', wait_ready=True)

print("Connected!")

def arm_and_takeoff(target_altitude):
    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {altitude}")
        if altitude >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

arm_and_takeoff(10)

print("Hovering...")
time.sleep(5)

print("Landing...")
vehicle.mode = VehicleMode("LAND")

time.sleep(10)

print("Closing connection")
vehicle.close()
