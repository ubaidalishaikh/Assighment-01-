def calculate_planet_weight():
    print("🌌 Welcome to the Interplanetary Weight Converter! 🌌")

    # Dictionary of planet names and their gravity % compared to Earth
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    try:
        earth_weight = float(input("Enter your weight on Earth (in kg): "))
        planet = input("Enter the name of the planet you want to travel to (e.g., Mars): ")

        if planet in gravity_factors:
            factor = gravity_factors[planet]
            planet_weight = round(earth_weight * factor, 2)
            print(f"Your weight on {planet} would be: {planet_weight} kg")
        else:
            print("Sorry, that planet is not in our list.")

    except ValueError:
        print("Please enter a valid number for weight.")

# Run the program
if __name__ == "__main__":
    calculate_planet_weight()
