# Program Name: Automobile Data Input
# File Name: automobile_app.py
# Description: This program prompts the user for details of an automobile (year, make, model, number of doors, and type of roof),
# stores the information in an object, and prints the details in a formatted output.
# Variables:
#     vehicle_type - str: stores the type of vehicle (e.g., "car")
#     year - str: stores the year of the vehicle, validated to be a 4-digit number
#     make - str: stores the make of the vehicle
#     model - str: stores the model of the vehicle
#     doors - str: stores the number of doors of the vehicle, validated to be '2' or '4'
#     roof - str: stores the type of roof of the vehicle, validated to be 'solid' or 'sun roof'
#     car - Automobile: object that stores the above information
# Date: November 13, 2023
# Author: Kyrylo Mizernyuk

class Vehicle:
    # The Vehicle class serves as a base class for different types of vehicles.
    def __init__(self, vehicle_type: str):
        # Initialize the vehicle with a type (e.g., car, truck, plane, boat, or broomstick).
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    # The Automobile class inherits from Vehicle and represents a more specific vehicle type with additional attributes.
    def __init__(self, vehicle_type: str, year: str, make: str, model: str, doors: str, roof: str):
        # Call the __init__ of the parent class to set the vehicle type.
        super().__init__(vehicle_type)
        # Initialize the automobile with year, make, model, doors, and roof attributes.
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        # Provide a human-readable format when printing an Automobile object.
        return (f"Vehicle type: {self.vehicle_type}\n"
                f"Year: {self.year}\n"
                f"Make: {self.make}\n"
                f"Model: {self.model}\n"
                f"Number of doors: {self.doors}\n"
                f"Type of roof: {self.roof}")

# Main execution block to run the program in an interactive environment like VS Code.
if __name__ == "__main__":
    vehicle_type = "car"  # The assignment specifies the vehicle type is 'car', hence we set it directly.
    
    # Prompt the user for vehicle details with input validation.
    year = input("Enter the year of the car (e.g., 2023): ")
    while not (year.isdigit() and len(year) == 4):
        print("Invalid year. Please enter a 4-digit year.")
        year = input("Enter the year of the car (e.g., 2023): ")

    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")

    doors = input("Enter the number of doors (2 or 4): ")
    while doors not in ("2", "4"):
        print("Invalid number of doors. Please enter 2 or 4.")
        doors = input("Enter the number of doors (2 or 4): ")

    roof = input("Enter the type of roof (solid or sun roof): ")
    while roof not in ("solid", "sun roof"):
        print("Invalid type of roof. Please enter 'solid' or 'sun roof'.")
        roof = input("Enter the type of roof (solid or sun roof): ")
    
    # Create an Automobile object with the provided input.
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    # Print the details of the car in a formatted string.
    print("\n" + str(car))
