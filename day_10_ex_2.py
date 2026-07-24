try:
    temp = float(input("Enter today's temperature (in °C): ").strip())
except ValueError:
    print("Invalid temperature input. Please enter a number.")
else:
    if temp > 30:
        print("It's hot outside!")
    elif temp >= 20:
        print("Nice and warm outside!")
    elif temp >= 10:
        print("A bit cool, bring a jacket.")
    else:
        print("It's cold, stay warm!")