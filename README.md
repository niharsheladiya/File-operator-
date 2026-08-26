

---

# 📁 Personal Journal Manager — File Operator Project

A beginner-friendly Python console application built to manage a personal digital diary. The program interactively collects journal entries, tags them with precise timestamps, and demonstrates core Python file handling operations (reading, writing, appending, and deleting files), along with robust exception handling and string manipulation.

---

## 🎥 Live Demo Video Link

[Insert your live demo link here]

---

## 📌 Objective

Create an **Interactive Personal Journal Manager** application in Python that allows users to create, view, search, and delete journal entries. This project demonstrates a working understanding of:

* File I/O operations (`open()`, `read()`, `write()`, append mode `a`, read mode `r`).
* The `os` module for file deletion (`os.remove()`).
* The `datetime` module for generating formatted timestamps.
* Exception handling using `try-except` blocks (e.g., `FileNotFoundError`, `PermissionError`).
* Object-Oriented Programming (OOP) via the `JournalManager` class.

---

## ✅ Features / Requirements Covered

### 1. Add a New Entry

* Uses `input()` to collect a new journal thought or note.
* Automatically generates a timestamp using `datetime.datetime.now()` formatted as `[YYYY-MM-DD HH:MM:SS]`.
* Appends the timestamp and entry to a text file (`journal.txt`).

### 2. View All Entries

* Opens and reads the contents of `journal.txt`.
* Gracefully handles empty files and alerts the user if the journal file does not exist yet.

### 3. Search for an Entry

* Allows the user to search past entries by specific dates or text keywords.
* Performs a case-insensitive search (`.lower()`) by splitting the document content into distinct entries.
* Displays only the entries that match the search query.

### 4. Delete All Entries

* Prompts the user with a `yes/no` confirmation before taking destructive action.
* Deletes the `journal.txt` file entirely using `os.remove()` if confirmed.

### 5. Robust Error Handling

* Prevents program crashes by catching common file errors (e.g., attempting to read or delete a file that hasn't been created yet, or lacking write permissions).

---

## 🔄 Program Flow

1. **Welcome & Main Menu** – Displays an interactive, loop-driven 5-option menu.
2. **User Selection** – Prompts the user for a choice (1-5).
3. **Execution (Class Methods)** – Depending on the input, calls the respective method on the `JournalManager` object (`add_entry`, `view_entries`, `search_entry`, or `delete_entries`).
4. **Return to Menu** – After the operation is complete (or if an invalid input is entered), the menu loops back for the next command.
5. **Exit** – The loop breaks, and a polite goodbye message is printed when option 5 is selected.

---

## 💻 Example Console Interaction

```text
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
1

Enter your journal entry:
my name is nihar and my age is 18

Entry added successfully!

Welcome to Personal Journal Manager!
Please select an option:
...
User Input:
2

Your Journal Entries:
-----------------------
[2026-08-26 22:17:41]
my name is nihar and my age is 18

...
User Input:
4

Are you sure you want to delete all entries? (yes/no): yes
All journal entries have been deleted.

Welcome to Personal Journal Manager!
...
User Input:
5

Thank you for using Personal Journal Manager. Goodbye!

```

> 💡 **Note:** If you try to view or search for an entry before adding one, the program's built-in `try-except` block will safely catch the `FileNotFoundError` and tell you to create an entry first.

---

## 🚀 How to Run

```bash
python file_operator.py

```

Make sure you have **Python 3** installed. No external libraries are required — this project utilizes Python's built-in standard libraries (`os`, `datetime`).

---

## 📁 Project Structure

```text
File-Operator-Project/
├── file_operator.py   # Main application source code
├── journal.txt        # Auto-generated text file storing your entries
└── README.md          # Project documentation (this file)

```

---

## 🧠 Assumptions Made

* All entries are saved locally to a plain text file named `journal.txt` in the same directory as the script.
* Keyword searches are strictly case-insensitive to improve user experience.
* The "Delete All Entries" functionality removes the entire text file from the system rather than just clearing its contents, saving storage space.
* A blank line `\n\n` is used as the distinct separator between individual journal entries for parsing during searches.

---

## 📝 Academic Integrity

This project was completed independently as a practical application of File I/O operations and Object-Oriented principles in Python. All code is original and written specifically to satisfy the requirements outlined in the assignment brief.

---

**Python File Handling — Personal Journal Manager**
*"Bringing data to life, one file at a time!"*
