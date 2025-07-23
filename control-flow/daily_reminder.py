while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"

    if time_bound.lower() == "yes":
        print(f"{reminder} that requires immediate attention today!")
    else:
        print(f"{reminder}. Consider completing it when you have free time.")

    again = input("Run again? (yes/no): ")
    if again.lower() != "yes":
        break