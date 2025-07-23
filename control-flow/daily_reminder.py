while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            base_reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            base_reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            base_reminder = f"Note: '{task}' is a low priority task"

    if time_bound == "yes":
        print(f"{base_reminder} that requires immediate attention today!")
    else:
        print(f"{base_reminder}. Consider completing it when you have free time.")

    again = input("Run again? (yes/no): ")
    if again.lower() != "yes":
        break