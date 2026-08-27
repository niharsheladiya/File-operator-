# welcome to File Operator project


import datetime


class JournalManager:

    def add_entry(self):
        entry = input("\nEnter your journal entry: ")

        now = datetime.datetime.now()
        timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")

        try:
            with open("journal.txt", "a") as file:
                file.write(timestamp + "\n")
                file.write(entry + "\n\n")

            print("\nEntry added successfully!\n")

        except PermissionError:
            print("\nPermission denied.\n")


    def view_entries(self):
        try:
            with open("journal.txt", "r") as file:
                content = file.read()

            if content.strip() == "":
                print("\nNo journal entries found.\n")
            else:
                print("\nYour Journal Entries:")
                print("---------------------")
                print(content)

        except FileNotFoundError:
            print("\nNo journal file found. Add an entry first.\n")


    def search_entry(self):
        keyword = input("\nEnter keyword or date: ")

        try:
            with open("journal.txt", "r") as file:
                content = file.read()

            entries = content.strip().split("\n\n")
            found = False

            print("\nMatching Entries:")
            print("-----------------")

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if not found:
                print("No matching entries found.\n")

        except FileNotFoundError:
            print("\nNo journal file found. Add an entry first.\n")


    def delete_entries(self):
        confirmation = input(
            "\nAre you sure you want to delete all entries? (yes/no): "
        )

        if confirmation.lower() == "yes":
            try:
                with open("journal.txt", "w") as file:
                    file.write("")

                print("\nAll journal entries deleted.\n")

            except PermissionError:
                print("\nPermission denied.\n")

        else:
            print("\nDeletion cancelled.\n")


def main():

    manager = JournalManager()

    while True:

        print("\nWelcome to Personal Journal Manager!")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.add_entry()

        elif choice == "2":
            manager.view_entries()

        elif choice == "3":
            manager.search_entry()

        elif choice == "4":
            manager.delete_entries()

        elif choice == "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()

