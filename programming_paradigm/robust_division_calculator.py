# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling.
    
    Args:
        numerator: The dividend (can be string or number)
        denominator: The divisor (can be string or number)
    
    Returns:
        str: Result message or error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."


# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()