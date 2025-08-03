import json
import os

filename = "contacts.json"

# Load existing contacts from file
def load_contacts():
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Save contacts to file
def save_contacts(contacts):
    try:
        with open(filename, "w") as f:
            json.dump(contacts, f, indent=4)
    except Exception as e:
        print("Error saving contacts:", e)

# Add contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print("Contact added successfully!\n")

# View contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
    else:
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}")
        print()

# Update contact
def update_contact():
    name = input("Enter name to update: ")
    contacts = load_contacts()
    for c in contacts:
        if c['name'].lower() == name.lower():
            new_phone = input("Enter new number: ")
            c['phone'] = new_phone
            save_contacts(contacts)
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

# Delete contact
def delete_contact():
    name = input("Enter name to delete: ")
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(contacts) == len(new_contacts):
        print("Contact not found.\n")
    else:
        save_contacts(new_contacts)
        print("Contact deleted successfully!\n")

# Main Menu
def main():
    while True:
        print("1. Add")
        print("2. View")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        try:
            choice = int(input("Choose: "))
            if choice == 1:
                add_contact()
            elif choice == 2:
                view_contacts()
            elif choice == 3:
                update_contact()
            elif choice == 4:
                delete_contact()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!\n")
        except ValueError:
            print("Please enter a valid number.\n")

main()