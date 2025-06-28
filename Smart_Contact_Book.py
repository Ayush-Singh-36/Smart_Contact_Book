contacts = []
print("Smart Contact Book\n 1. Add new contact\n 2. Display all contacts\n 3. Search contact\n 4. Edit contact\n 5. Delete contact\n 6. Sort contacts ny name\n 7. Exit\n\n Choose an option :-\n")
def add_contact():
    name = input("Enter your name-\n ")
    phone = input("Enter your number-\n ")
    email = input("Enter your e-mail-\n ")
    contact = {"name": name, "phone": phone, "email": email}

    contacts.append(contact)
    print("Contact added successfully!")

def display_all_contacts():
    print("-- All Contacts --")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")


def search_contact():
    search_term = input("Search by name or phone: ").strip()
    found = False
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            print("Contact Found.")
            print(f'{contact["name"]} | {contact["phone"]} | {contact["email"]}')
            found = True
            break
    if not found:
        print("Sorry, contact not found.")
def edit_contact():
    search_term = input("Enter name to call the contact-\n ").strip()
    found = False
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            print("Contact found.")
            print(f'Name: {contact["name"]}\nPhone-no: {contact["phone"]}\n Email: {contact["e-mail"]}')
            new_name = input("New Name ").strip()
            new_phone = input("New Phone ").strip()
            new_email = input("New Email ").strip()
            if new_name:
                contact["name"] = new_name
            if new_phone:  
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email

            print("Contact updated successfully!")
            found = True
            break

    if not found:
        print("Contact not found.")
def delete_contact():
    search_term = input("Enter name or phone to delete contact:\n").strip()
    found = False

    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            print("Contact Found:")
            print(f'{contact["name"]} | {contact["phone"]} | {contact["email"]}')

            surity = input("Are you sure you want to delete this contact? (yes/no):\n").strip().lower()
            if surity == "yes":
                contacts.remove(contact)  
                print("Contact is deleted successfully!")
                found = True
                break
            else:
                print("Deletion cancelled.")
                found = True
                break

    if not found:
        print("Contact not found.")
def sort_contacts_by_name():
    if contacts:
        contacts.sort(key=lambda contact: contact["name"].lower())
        print("Contacts sorted by name!")
    else:
        print("No contacts to sort.")
def menu():
    while True:
        print("\nSmart Contact Book")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Sort Contacts by Name")
        print("7. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            display_all_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            sort_contacts_by_name()
        elif choice == '7':
            print("👋 Exiting Smart Contact Book. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

menu()
