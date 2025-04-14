def calculate_mars_weight():
    print("Welcome to the Earth-to-Mars Weight Converter!")
    
    try:
        # User input for Earth weight
        earth_weight = float(input("Enter your weight on Earth (in kg): "))

        # Mars gravity is 37.8% of Earth's
        mars_weight = earth_weight * 0.378

        # Rounded to 2 decimal places
        mars_weight_rounded = round(mars_weight, 2)

        print(f"Your weight on Mars would be: {mars_weight_rounded} kg")
    
    except ValueError:
        print("Please enter a valid number!")

# Run the program
if __name__ == "__main__":
    calculate_mars_weight()
