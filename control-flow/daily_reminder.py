while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if time_bound == "yes":
        match priority:
            case "high":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            case "medium":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            case "low":
                print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
    else:
        match priority:
            case "high":
                print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
            case "medium":
                print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.")
            case "low":
                print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")

    again = input("Run again? (yes/no): ")
    if again.lower() != "yes":
        break