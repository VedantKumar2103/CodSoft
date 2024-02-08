# Contact Book

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        print("\nContact List:")
        for index, contact in enumerate(self.contacts):
            print(f"{index + 1}. {contact.name} - {contact.phone}")

    def search_contacts(self, search_term):
        search_results = []
        for contact in self.contacts:
            if (
                search_term.lower() in contact.name.lower()
                or search_term in contact.phone
            ):
                search_results.append(contact)
        return search_results

    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]

def main():
    contact_list = ContactList()

    while True:
        print("\nContact Management Application")
        print("-------------------------------")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nAdd Contact")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact_list.add_contact(Contact(name, phone, email, address))
            print("Contact added.")

        elif choice == "2":
            print("\nView Contact List")
            contact_list.view_contacts()

        elif choice == "3":
            print("\nSearch Contact")
            search_term = input("Enter search term: ")
            search_results = contact_list.search_contacts(search_term)
            if search_results:
                print("\nSearch Results:")
                for index, contact in enumerate(search_results):
                    print(f"{index + 1}. {contact.name} - {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            print("\nUpdate Contact")
            index = int(input("Enter index of contact to update: ")) - 1
            if 0 <= index < len(contact_list.contacts):
                name = input("New Name: ")
                phone = input("New Phone: ")
                email = input("New Email: ")
                address = input("New Address: ")
                new_contact = Contact(name, phone, email, address)
                contact_list.update_contact(index, new_contact)
                print("Contact updated.")
            else:
                print("Invalid index.")

        elif choice == "5":
            print("\nDelete Contact")
            index = int(input("Enter index of contact to delete: ")) - 1
            if 0 <= index < len(contact_list.contacts):
                contact_list.delete_contact(index)
                print("Contact deleted.")
            else:
                print("Invalid index.")

        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
