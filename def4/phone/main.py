import db
def main():
    db.create_table()
    while True:
        print("\nPhoneBook Menu:")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update user")
        print("4. Query users")
        print("5. Delete user")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            db.insert_from_console(name, phone)
        elif choice == '2':
            filename = 'C:/Users/One/Desktop/phonebook/' + input("Enter CSV filename: ")
            db.insert_from_csv(filename)
        elif choice == '3':
            name = input("Enter current name to update: ")
            new_name = input("Enter new name (or press Enter to skip): ")
            new_phone = input("Enter new phone (or press Enter to skip): ")
            db.update_user(name, new_name if new_name else None, new_phone if new_phone else None)
        elif choice == '4':
            filter_name = input("Filter by name (or press Enter to skip): ")
            filter_phone = input("Filter by phone (or press Enter to skip): ")
            users = db.query_users(filter_name if filter_name else None, filter_phone if filter_phone else None)
            for user in users:
                print(f"Name: {user[0]}, Phone: {user[1]}")
        elif choice == '5':
            name = input("Enter name to delete (or press Enter to skip): ")
            phone = input("Enter phone to delete (or press Enter to skip): ")
            db.delete_user(name if name else None, phone if phone else None)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
if __name__ == '__main__':
    main()