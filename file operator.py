# Welcome to File operator project



import os
import datetime


class JournalManager:
    

    def __init__(self):
        
        self.filename = "journal.txt"


    def add_entry(self):
        entry_text = input("\nEnter your journal entry:\n")
        
        
        now = datetime.datetime.now()
        
        timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")


        try:
             
            
            with open(self.filename, 'a') as file:
                file.write(f"{timestamp}\n")
                file.write(f"{entry_text}\n\n") 
            print("\nEntry added successfully!\n")
        except PermissionError:
            print("\nError: You do not have permission to write to this file.\n")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}\n")




    def view_entries(self):
        try:
            
            with open(self.filename, 'r') as file:
                content = file.read()
                
                
                if content.strip() == "":

                    print("\nNo journal entries found. Start by adding a new entry!\n")

                else:

                    print("\nYour Journal Entries:")
                    print("---------------------------")
                    print(content.strip())
                    print() 
                    
        except FileNotFoundError:
            
            print("\nError: The journal file does not exist. Please add a new entry first.\n")




    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ")
        
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                
                
                entries = content.strip().split('\n\n')
                found = False
                
                print("\nMatching Entries:")
                print("---------------------------")
                
            
                for entry in entries:
                    
                    if keyword.lower() in entry.lower():
                        print(entry + "\n")
                        found = True
                        
                if not found:
                    print(f"No entries were found for the keyword: {keyword}\n")
                    
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.\n")





    def delete_entries(self):
        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")
        
        if confirm.lower() == 'yes':
            try:
                
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.\n")
            except FileNotFoundError:
                print("\nNo journal entries to delete.\n")
        else:
            print("\nDeletion cancelled.\n")






def main():
    
    manager = JournalManager()
    
    while True:
        print("Welcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        choice = input("\nUser Input:\n")
        
        if choice == '1':
            manager.add_entry()
        elif choice == '2':
            manager.view_entries()
        elif choice == '3':
            manager.search_entry()
        elif choice == '4':
            manager.delete_entries()
        elif choice == '5':
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break 
        else:
            print("\nInvalid option. Please select a valid option from the menu.\n")


if __name__ == "__main__":
    main()
