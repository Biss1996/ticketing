import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import (
    create_user, list_users, update_user, delete_user,
    create_event, list_events, update_event,
    add_ticket, list_tickets, update_ticket, cancel_ticket
)
def main():
    options = {
        "1": create_user,
        "2": list_users,
        "3": update_user,
        "4": delete_user,
        "5": create_event,
        "6": list_events,
        "7": update_event,
        "8": add_ticket,
        "9": list_tickets,
        "10": update_ticket,
        "11": cancel_ticket,
        "q": exit
    }

    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. List Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Create Event")
        print("6. List Events")
        print("7. Update Event")
        print("8. Add Ticket")
        print("9. List Tickets")
        print("10. Update Ticket")
        print("11. Cancel Ticket")
        print("q. Quit")

        choice = input("Select an option: ").lower()
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
