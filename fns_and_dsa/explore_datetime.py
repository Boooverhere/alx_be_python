from datetime import datetime, timedelta

def display_current_datetime():
       """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
       current_date = datetime.now()
       formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
       print(f"Current date and time: {formatted_date}")
       return current_date

def calculate_future_date(current_date, days):
       """Calculate and display the future date after adding specified days."""
       future_date = current_date + timedelta(days=days)
       formatted_future_date = future_date.strftime("%Y-%m-%d")
       print(f"Future date: {formatted_future_date}")
       return future_date

def main():
       current_date = display_current_datetime()
       while True:
           try:
               days = input("Enter the number of days to add to the current date: ").strip()
               days = int(days)
               if days < 0:
                   print("Please enter a non-negative number of days.")
                   continue
               calculate_future_date(current_date, days)
               break
           except ValueError:
               print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
       main()