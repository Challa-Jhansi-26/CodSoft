# Contact Book Application

# Initialize an empty contact book
contact_book = []

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contact_book.append(contact)
    print("Contact added.")

def view_contact_list():
    if not contact_book:
        print("Your contact book is empty.")
    else:
        print("\nYour Contact List:")
        for i, contact in enumerate(contact_book, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contact_book if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if results:
        for contact in results:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("No contact found.")

def update_contact():
    search_term = input("Enter name or phone number to update: ").lower()
    for contact in contact_book:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print(f"\nCurrent details: {contact}")
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated.")
            return
    print("No contact found to update.")

def delete_contact():
    search_term = input("Enter name or phone number to delete: ").lower()
    for i, contact in enumerate(contact_book):
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            del contact_book[i]
            print("Contact deleted.")
            return
    print("No contact found to delete.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
