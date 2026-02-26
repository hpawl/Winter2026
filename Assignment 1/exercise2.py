# Exercise 2: Smartphone Data & Battery Planner
# Constants
BATTERY_CAPACITY = 4500  # mAh
CONSUMPTION_PER_HOUR = 425  # mAh
TOTAL_HOURS = 12

# 1. Calculate total power required
total_power = CONSUMPTION_PER_HOUR * TOTAL_HOURS # Your code here

# 2. Calculate power deficit (Total power - one full charge)
deficit = total_power % BATTERY_CAPACITY # Your code here

# 3. Calculate full charges needed using //
full_charges = int(total_power / BATTERY_CAPACITY) - 1 # Your code here

# 4. Calculate remaining power needed using %
remaining_power = total_power - (full_charges * BATTERY_CAPACITY)# Your code here

# Print results

print("| Item                    | Result   |")
print("|-------------------------|----------|")
print(f"| Total Power             | {total_power} mAh |")
print(f"| Deficit after 1 Charge  | {deficit} mAh  |")
print(f"| Full Recharges Needed   | {full_charges}        |")
print(f"| Leftover Power Required | {remaining_power} mAh |")