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
summary_of_robots = {
    "Max": "Downtown",
    "Advil": "Suburbs",
    "Robby": "Industrial"
}

# gets the total delivery distance from the user (between 5 and 500 km)
def ask_total_delivery():
    while True: 
        try: 
            distance = float(input("Enter the total delivery distance (5-500 km): "))
            if 5 <= distance <= 500:
                return distance
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# gets the cargo weight for each robot(between 1 and 50 kg)
def ask_cargo_weight():
    while True:
        try:
            weight = float(input("Enter the cargo weight (1-50 kg): "))
            if 1 <= weight <= 50:
                return weight
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# gets the weather condition( "Clear", "Rain", or "Storm")
def ask_weather():
    while True:
        weather = input("Enter the weather condition (Clear, Rain, or Storm): ").strip()
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



# if the conditions are all met, print "🤖 Robots Ready for Delivery!"

# the main function to run the code
def main():

















# Run program
if      __name__ == "__main__":
    main()