RideType = str(input("Which ride will you do (Car or Bike?) \n"))

if RideType.lower() == "car":
    print("You have chosen a Car ride.")
    print("What type of car do you want to drive?")
    print("1. Sedan \n2. SUV")
    car_choice = int(input("Enter your choice (1 or 2): "))
    if car_choice == 1:
        print("You have chosen a Sedan.")
    elif car_choice == 2:   
        print("You have chosen an SUV.")
elif RideType.lower() == "bike":
    print("You have chosen a Bike ride.")
    print("What type of bike do you want to ride?")
    print("1. Mountain \n2. Sport")
    bike_choice = int(input("Enter your choice (1 or 2): "))
    if bike_choice == 1:
        print("You have chosen a Cruiser bike.")
    elif bike_choice == 2:
        print("You have chosen a Sport bike.")
