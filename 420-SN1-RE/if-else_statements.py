# %%
## Boiling or not? ##
freezing_point = 0
boiling_point = 100
input_temperature = int(input("What temperature do you want to check? "))

if input_temperature < freezing_point:
    print(f"Temperature {input_temperature}°C is below freezing point")
elif input_temperature > boiling_point:
    print(f"Temperature {input_temperature}°C is above boiling point")
else:
    print(f"Temperature {input_temperature}°C is neither boiling nor freezing")

# %%
## Grade Converter ##

score = int(input("What is your score out of a 100? "))
grade = "--"

if score >= 90:
    grade = "A"
elif 90 > score >= 80:
    grade = "B"
elif 80 > score >= 70:
    grade = "C"
elif 70 > score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"With a score of {score}%, your grade is {grade}.")

# %%
## Temperature ##

temperature = int(input("What is the temperature right now? "))

if temperature >= 30:
    condition = "really hot"
elif 25 <= temperature < 30:
    condition = "hot"
elif 19 <= temperature < 25:
    condition = "nice"
elif 11 <= temperature < 19:
    condition = "warm"
elif 10 <= temperature < -5:
    condition = "chilly"
elif temperature < -5:
    condition = "cold"

print(f"It is {condition} outside.")