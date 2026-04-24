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

def ask_user():
    name = input("Enter the robot's name: ").strip() .title()
    

def ask_delivery_zone():
    zone = input("Enter the delivery zone (Downtown, Suburbs, Industrial): ").strip() .title()
    

# gets the total delivery distance from the user (between 5 and 500 km)
def ask_total_delivery():
    while True: 
        try: 
            distance = int(input("Enter the total delivery distance (5-500 km): ").strip())
            if 5 <= distance <= 500:
                return distance
            else:
                print("Distance must be between 5 and 500 km.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# gets the cargo weight for each robot(between 1 and 50 kg)
def ask_cargo_weight():
    while True:
        try:
            weight = int(input("Enter the cargo weight (1-50 kg): "))
            if 1 <= weight <= 50:
                return weight
            else:
                print("Weight must be between 1 and 50 kg.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


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

    print("🤖 Robot Delivery Team System\n")

    # Ask distance
    distance = ask_total_delivery()

    # Store cargo weights in list
    cargo_weights = []

    print("\nEnter cargo weights:")

    for robot in summary_of_robots:
        weight = ask_cargo_weight()
        cargo_weights.append(weight)

    # Ask weather
    weather = ask_weather()

    # Final result
    if is_deployment_safe(distance, cargo_weights, weather):

        print("\n--- Robot Summary ---")

        index = 0
        for robot in summary_of_robots:
            zone = summary_of_robots[robot]
            weight = cargo_weights[index]

            print(f"{robot}: {zone}, {weight}kg")

            index += 1

        print("🤖 Robots Ready for Delivery!")

    else:
        print("\n🚨 Deployment Unsafe!")


# Run program
if __name__ == "__main__":
    main()