freezing_point = 0
boiling_point = 100
input_temperature = int(input("What temperature do you want to check? "))

if input_temperature < freezing_point:
    print(f"Temperature {input_temperature}°C is below freezing point")
elif input_temperature > boiling_point:
    print(f"Temperature {input_temperature}°C is above boiling point")
else:
    print(f"Temperature {input_temperature}°C is neither boiling nor freezing")