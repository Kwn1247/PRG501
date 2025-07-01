# Homework 2
# @Author  : Haixiang Yu

import csv

contacts = {}

def load_contacts(fremont):
    try:
        with open(fremont.csv, mode='r', encoding='ISO-8859-1') as file:
            reader = csv.reader(fremont.csv)
            for row in reader:
                if len(row) >= 2:
                    name = row[1].strip()
                    number = row[2].strip()
                    contacts[name] = number
            print(f"Contacts loaded from '{fremont.csv}'.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error loading contacts: {e}")

def view_contacts():
    if contacts:
        print("\n--- Contact List ---")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("No contacts found.")

def add_contact():
    name = input("Enter contact name: ").strip()
    number = input("Enter phone number: ").strip()
    if name:
        contacts[name] = number
        print(f"Contact '{name}' added.")
    else:
        print("Invalid name.")

def delete_contact():
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Load Contacts from CSV")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            filename = input("Enter the CSV filename (e.g., fremont.csv): ")
            load_contacts(filename)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
