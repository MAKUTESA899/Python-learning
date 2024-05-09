drinkingAge = 18
drivingAge = 21
age = 12

if age >= drinkingAge and age >= drivingAge:
    print("Can drink and drive")
elif age >= drinkingAge and age <= drivingAge:
    print("can drink but cannot drive")
else:
    print("is not an adult")