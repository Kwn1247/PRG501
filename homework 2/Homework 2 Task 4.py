# Homework 2
# @Author  : Haixiang Yu

def email_manager():
    email_set = set()

    while True:
        print("\n--- Email Manager ---")
        print("1. Add Email Address")
        print("2. Check Email Address")
        print("3. View All Emails")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            email = input("Enter email to add: ").strip().lower()
            if email in email_set:
                print("Email already exists.")
            else:
                email_set.add(email)
                print("Email added successfully.")

        elif choice == '2':
            email = input("Enter email to check: ").strip().lower()
            if email in email_set:
                print("Email is already in the list.")
            else:
                print("Email is not in the list.")

        elif choice == '3':
            if email_set:
                print("\nStored Emails:")
                for email in sorted(email_set):
                    print(email)
            else:
                print("No emails stored yet.")

        elif choice == '4':
            print("Exiting Email Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    email_manager()
