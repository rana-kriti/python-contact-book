# Contact Book Program

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print(f"\n Contact '{name}' added successfully!\n")


def view_contacts():
    if not contacts:
        print("\n⚠ No contacts found.\n")
        return

    print("\n Contact List:")
    print("---------------------------")
    for name, info in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("---------------------------")


def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("\n Contact Found:")
        print(f"Name : {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}\n")
    else:
        print("\n Contact not found.\n")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"\n🗑 Contact '{name}' deleted successfully.\n")
    else:
        print("\n Contact not found.\n")


def menu():
    while True:
        print(" Contact Book Menu")
        print("----------------------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            add_contact()

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            search_contact()

        elif choice == '4':
            delete_contact()

        elif choice == '5':
            print("\n Exiting Contact Book. Goodbye!")
            break

        else:
            print("\n⚠ Invalid choice. Please try again.\n")


# Run program
menu()