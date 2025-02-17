contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print("Contact added successfully!\n")

def view_contacts():
    if contacts:
        for name, info in contacts.items():
            print(f"{name} - {info['Phone']}")
    else:
        print("No contacts found.")
    print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    for name, info in contacts.items():
        if query in name or query in info['Phone']:
            print(f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}\n")
            return
    print("Contact not found.\n")

def update_contact():
    name = input("Enter name of the contact to update: ")
    if name in contacts:
        contacts[name]['Phone'] = input("Enter new phone number: ")
        contacts[name]['Email'] = input("Enter new email: ")
        contacts[name]['Address'] = input("Enter new address: ")
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.\n")

main()
