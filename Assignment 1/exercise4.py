import math

# Exercise 4: Satellite Orbit Calculation
earth_radius = 6371  # km (r)
altitude = 400       # km (h)
gm_parameter = 398600 # (GM)

# 1. Total Radius (R = r + h)
total_radius = earth_radius + altitude # Your code here

# 2. Orbital Velocity (v = sqrt(GM / R))
velocity = round(math.sqrt(gm_parameter // total_radius), 2) # Your code here

# 3. Horizon Distance (d = sqrt(R^2 - r^2))
horizon_dist = round(math.sqrt(total_radius ** 2 - earth_radius ** 2), 1) # Your code here

# Print results rounded to 2 decimal places
print(f"Total Orbital Radius: {total_radius} km")
print(f"Orbital Velocity: {velocity} km/s")
print(f"Distance to Horizon: {horizon_dist} km")