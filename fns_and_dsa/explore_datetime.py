# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            # Prompt for temperature with exact string from example
            temp = input("Enter the temperature to convert: ").strip()
            temp = float(temp)  # Convert to float to handle decimals
            break
        except ValueError:
            # Raise error for non-numeric input as required
            print("Invalid temperature. Please enter a numeric value.")
    
    while True:
        # Prompt for unit with exact string from example
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break
        print("Invalid unit. Please enter 'C' or 'F'.")
    
    # Perform conversion and format output to match example
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp:.1f}°C is {converted_temp:.1f}°F")
    else:  # unit == 'F'
        converted_temp = convert_to_celsius(temp)
        print(f"{temp:.1f}°F is {converted_temp:.16f}°C")

if __name__ == "__main__":
    main()