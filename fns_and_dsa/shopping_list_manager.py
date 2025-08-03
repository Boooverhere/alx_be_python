def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty list to store shopping items
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ").strip()  # Get user choice and remove whitespace

        if choice == '1':
            # Add an item to the list
            item = input("Enter item to add: ").strip()  # Prompt for item name
            if item:  # Check if input is not empty
                shopping_list.append(item)  # Add item to the list
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
                
        elif choice == '2':
            # Remove an item from the list
            item = input("Enter item to remove: ").strip()  # Prompt for item name
            if item:  # Check if input is not empty
                # Check if item exists in the list (case-insensitive)
                item_lower = item.lower()
                for list_item in shopping_list:
                    if list_item.lower() == item_lower:
                        shopping_list.remove(list_item)  # Remove the matching item
                        print(f"'{item}' has been removed from the shopping list.")
                        break
                else:  # Executed if no matching item is found
                    print(f"'{item}' is not in the shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
                
        elif choice == '3':
            # Display the current shopping list
            if shopping_list:  # Check if the list is not empty
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):  # Number the items
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")
                
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
            
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()