import difflib
contacts = []
interaction_log = {}
print("Smart Contact Book\n 1. Add new contact\n 2. Display all contacts\n 3. Search contact\n 4. Edit contact\n 5. Delete contact\n 6. Sort contacts ny name\n 7. Exit\n\n Choose an option :-\n")
def suggest_name_correction(name):
    known_names = [contact["name"] for contact in contacts]
    suggestions = difflib.get_close_matches(name, known_names, n=1, cutoff = 0.8)
    return suggestions[0] if suggestions else None

def show_missing_info_alert(contact):
    missing_fields = [key for key in ["name", "phone", "email"] if not contact [key].strip()]
    if missing_fields:
        print(f"missing info: {', '.join(missing_fields)}")

def is_duplicate(new_contact):
    for contact in contacts:
        if (new_contact["name"].lower() == contact["name"].lower() and 
            new_contact["phone"] == contact["phone"]):
            return True
    return False

def increment_interaction(name):
    interaction_log[name] = interaction_log.get(name, 0) + 1

def auto_fill_suggestions(term):
      suggestions = [contact for contact in contacts if term.lower() in contact ["name"].lower()]
      return suggestions[:3]

def add_contact():
    name = input("Enter your name-\n ")
    phone = input("Enter your number-\n ")
    email = input("Enter your e-mail-\n ")
    contact = {"name": name, "phone": phone, "email": email}
    corrected = suggest_name_correction(name)
    if corrected:
        confirm = input(f"Did you mean'{corrected}'? (yes/no): ").strip().lower()
        if confirm =="yes":
            contact["name"] = corrected
    show_missing_info_alert(contact)
    if is_duplicate(contact):
        print("this contact already exists")  
        merge = input("Do you want to merge it anyway? (yes/no): ").strip().lower()
        if merge != "yes":
            return
        
        contacts.append(contact)
    print("Contact added successfully!")

def display_all_contacts():
    if not contacts:
        print("No contacts available!")
        return
    print("-- All Contacts --")
    sorted_contacts = sorted(contacts, key=lambda c: -interaction_log.get(c["name"], 0))
    for i, contact in enumerate(sorted_contacts, 1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
        show_missing_info_alert(contact)


def search_contact():
    search_term = input("Search by name or phone: ").strip()
    suggestions = auto_fill_suggestions(search_term)
    if suggestions:
        print("suggestions:")
        for i, contact in enumerate(suggestions, 1):
            print(f"{i}. {contact ['name']} | {contact ['phone']} | {contact ['email']}")
    found = False
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            print("Contact Found.")
            print(f'{contact["name"]} | {contact["phone"]} | {contact["email"]}')
            increment_interaction(contact["name"])
            found = True
            break
    if not found:
        print("Sorry, contact not found.")
def edit_contact():
    search_term = input("Enter name to call the contact-\n ").strip()
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            print("Contact found.")
            print(f'Name: {contact["name"]}\nPhone-no: {contact["phone"]}\n Email: {contact["email"]}')
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
            increment_interaction(contact["name"])
            return
        print("Contact not found.")
def delete_contact():
    search_term = input("Enter name or phone to delete contact:\n").strip()
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
                return
    print("contact no found!")
    
def sort_contacts_by_name():
    if contacts:
        contacts.sort(key=lambda contact: contact["name"].lower())
        print("Contacts sorted by name!")
    else:
        print("No contacts to sort.")
def menu():
    while True:
        print("\nSmart Contact Book\n1. Add Contact\n2. Display All Contacts\n3. Search Contact\n4. Edit Contact\n5. Delete Contact\n6. Sort Contacts by Name\n7. Exit")
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
