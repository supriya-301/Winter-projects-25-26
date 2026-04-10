import math

def generate_circle(center_n, center_e, radius, num_points, alt):
    waypoints = []

    for i in range(num_points):
        theta = 2 * math.pi * i / num_points

        n = center_n + radius * math.cos(theta)
        e = center_e + radius * math.sin(theta)

        waypoints.append({
            "north": n,
            "east": e,
            "alt": alt
        })

    return waypoints

def generate_helix(radius, start_alt, end_alt, laps, num_points):
    waypoints = []

    total_points = laps * num_points

    for i in range(total_points):
        theta = 2 * math.pi * i / num_points

        alt = start_alt + (end_alt - start_alt) * (i / total_points)

        n = radius * math.cos(theta)
        e = radius * math.sin(theta)

        waypoints.append({
            "north": n,
            "east": e,
            "alt": alt
        })

    return waypoints

def generate_orbit(pole_n, pole_e, radius, alt, num_points):
    waypoints = []
  
    for i in range(num_points):
        theta = 2 * math.pi * i / num_points

        n = pole_n + radius * math.cos(theta)
        e = pole_e + radius * math.sin(theta)

        waypoints.append({
            "north": n,
            "east": e,
            "alt": alt
        })

    return waypoints
