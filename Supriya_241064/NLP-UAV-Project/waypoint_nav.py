from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

vehicle = connect('127.0.0.1:14550', wait_ready = True)

def arm_and_takeoff(targetAlt):
        print("Arming....")
        vehicle.mode = VehicleMode("GUIDED")
        vehicle.armed = True

        while not vehicle.armed:
                time.sleep(1)

        print("Taking off .....")
        vehicle.simple_takeoff(targetAlt)

        while True:
                alt = vehicle.location.global_relative_frame.alt
                print("Altitude:", alt)
                if alt >= targetAlt * 0.95:
                        print("Reached altitude")
                        break
                time.sleep(1)

arm_and_takeoff(10)

print("Going to waypoint 1")
wp1 = LocationGlobalRelative(vehicle.location.global_frame.lat + 0.0001,
                             vehicle.location.global_frame.lon,
                             10)
vehicle.simple_goto(wp1)
time.sleep(10)

print("Going to waypoint 2")
wp2 = LocationGlobalRelative(vehicle.location.global_frame.lat,
                             vehicle.location.global_frame.lon + 0.0001,
                             10)
vehicle.simple_goto(wp2)
time.sleep(10)

print("Going to waypoint 3")
wp3 = LocationGlobalRelative(vehicle.location.global_frame.lat - 0.0001,
                             vehicle.location.global_frame.lon,
                                                          10)
vehicle.simple_goto(wp3)
time.sleep(10)

print("Returning to launch")
vehicle.mode = VehicleMode("RTL")

time.sleep(20)

vehicle.close()
