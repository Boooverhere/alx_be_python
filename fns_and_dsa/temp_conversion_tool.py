# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0  # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0  # Equivalent to 9/5, correcting 5*9/5 misinterpretation

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ").strip()
            temp = float(temp_input)
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
    
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            break
        print("Invalid unit. Please enter 'C' or 'F'.")
    
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp:.1f}°C is {converted_temp:.1f}°F")
    else:
        converted_temp = convert_to_celsius(temp)
        print(f"{temp:.1f}°F is {converted_temp:.16f}°C")

if __name__ == "__main__":
    main()