""" 
This is a test for creating 3 robots, their assigned zones(" Downtown ", " Suburbs ", " Industrial ") in a dictionary.
The name of the robots are Max for Downtown, Advil for Suburbs and Robby for Industrial.
The purpose for the robots is to deliver the packages to their respective zones within 5-500km.
The weight of the cargo for each user needs to be asked from the user.
We need to get the weather conditions from the user(Clear, Rain, Storm)
If the distance is over 300 km, any robot carries more than 50 kg, or weather is Storm, print "🚨 Deployment Unsafe!".
Otherwise, print a summary of robot names, zones, and cargo weights with the message: "🤖 Robots Ready for Delivery!".

"""


# creating a dictionary for the robots and their assigned delivery zones((" Downtown ", " Suburbs ", " Industrial ")
summary_of_robots = {}

def ask_zone(name):
    while True:
        zone = input(f"Choose a delivery zone for {name} (Downtown, Suburbs, Industrial): ").strip().title()

        if zone in ["Downtown", "Suburbs", "Industrial"]:
            return zone
        else:
            print("Invalid zone. Try again.")
    

# gets the total delivery distance from the user (between 5 and 500 km)
def ask_total_delivery():
    while True:
        try:
            distance = int(input("\nEnter total delivery distance (5-500 km): ").strip())

            if 5 <= distance <= 500:
                return distance
            else:
                print("Distance must be between 5 and 500.")

        except ValueError:
            print("Enter a valid number.")
    


# gets the cargo weight for each robot(between 1 and 50 kg)
def ask_cargo_weight(name):
    while True:
        try:
            weight = int(input(f"{name}: ").strip())

            if 1 <= weight <= 50:
                return weight
            else:
                print("Weight must be between 1 and 50.")

        except ValueError:
            print("Enter a valid number.")


# gets the weather condition( "Clear", "Rain", or "Storm")
def ask_weather():
    while True:

        weather = input("Enter the weather condition (Clear, Rain, or Storm): ").strip().title()

        if weather in ["Clear", "Rain", "Storm"]:
            return weather
        
        else:
            print("Invalid input. Please enter a valid weather condition.")

# If distance is over 300km, any robot carries more than 50 kg, or the weather is Storm. print "🚨 Deployment Unsafe!"  otherwise. print a summary of robot names, zones, and cargo weights
def is_deployment_safe(distance, cargo_weights, weather):

    if distance > 300:
        return False
    
    if any(weight > 50 for weight in cargo_weights):
        return False
    
    if weather == "Storm":
        return False
    return True


# Main function
def main():

    cargo = {} # Dictionary to store cargo weights

    # Get 3 robot names and zones
    for i in range(3): # loop through each robot
        name = input("Enter robot name: ").strip().title() # ask for robot name
        zone = ask_zone(name) # ask for delivery zone
        summary_of_robots[name] = zone # store robot and zone in dictionary
        print() # print a blank line

    # Distance
    distance = ask_total_delivery()

    if distance <= 300:
        print("Distance Check: Within Range")
    else:
        print("Distance Check: Too Far")

    # Cargo
    print("\nEnter cargo weight for each robot (1-50 kg):")

    for robot in summary_of_robots: # loop through each robot
        cargo[robot] = ask_cargo_weight(robot) # ask for cargo weight for each robot

    # Weather
    weather = ask_weather() # ask for weather conditions

    if weather == "Storm":
        print("Weather Check: Unsafe")
    else:
        print("Weather Check: Safe")

    # Final Result
    if distance > 300 or weather == "Storm":
        print("\n🚨 Deployment Unsafe!")

    else:
        print()

        for robot in summary_of_robots: # loop through each robot
            print(f"{robot}: {summary_of_robots[robot]}, {cargo[robot]}kg") # print robot details

        print("🤖 Robots Ready for Delivery!")


# Run program
if __name__ == "__main__":
    main()