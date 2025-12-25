import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DB = os.path.join(BASE_DIR, "files.txt")
NOTES_DIR = os.path.join(BASE_DIR, "notes")

def add_study_file():
    filename = input("Enter study file name (example: os_notes.txt): ").strip()

    if not filename:
        print("File name cannot be empty.")
        return

    if not os.path.exists(FILES_DB):
        open(FILES_DB, "w").close()

    with open(FILES_DB, "r") as file:
        files = file.read().splitlines()

    if filename in files:
        print("File already exists.")
        return

    with open(FILES_DB, "a") as file:
        file.write(filename + "\n")

    print("Study file added successfully.")

def view_study_files():
    if not os.path.exists(FILES_DB):
        print("No study files found.")
        return

    with open(FILES_DB, "r") as file:
        files = file.read().splitlines()

    if not files:
        print("No study files available.")
        return

    print("\nYour Study Files:")
    for index, name in enumerate(files, start=1):
        print(f"{index}. {name}")

def study_and_add_notes():
    if not os.path.exists(FILES_DB):
        print("No study files available.")
        return

    with open(FILES_DB, "r") as file:
        files = file.read().splitlines()

    if not files:
        print("No study files available.")
        return

    print("\nSelect a study file:")
    for index, name in enumerate(files, start=1):
        print(f"{index}. {name}")

    try:
        choice = int(input("Enter file number: "))
        if choice < 1 or choice > len(files):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    selected_file = files[choice - 1]
    notes_file = os.path.join(NOTES_DIR, f"notes_{selected_file}")

    print(f"\nStudying: {selected_file}")
    print("Enter important points (type 'done' to finish):")

    with open(notes_file, "a") as file:
        while True:
            note = input("> ")
            if note.lower() == "done":
                break
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            file.write(f"[{timestamp}] {note}\n")

    print("Notes saved successfully.")

def view_notes():
    if not os.path.exists(FILES_DB):
        print("No study files available.")
        return

    with open(FILES_DB, "r") as file:
        files = [f for f in file.read().splitlines() if f.strip()]

    if not files:
        print("No study files available.")
        return

    print("\nSelect a study file to view notes:")
    for index, name in enumerate(files, start=1):
        print(f"{index}. {name}")

    try:
        choice = int(input("Enter file number: "))
        if choice < 1 or choice > len(files):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    selected_file = files[choice - 1]
    notes_file = os.path.join(NOTES_DIR, f"notes_{selected_file}")

    if not os.path.exists(notes_file):
        print("No notes found for this file.")
        return

    print(f"\nNotes for {selected_file}:\n")

    with open(notes_file, "r") as file:
        notes = file.read()

    if not notes.strip():
        print("Notes file is empty.")
    else:
        print(notes)

def main_menu():
    if not os.path.exists(NOTES_DIR):
        os.mkdir(NOTES_DIR)

    while True:
        print("\n--- Study Notes Organizer ---")
        print("1. Add study file")
        print("2. View study files")
        print("3. Study file & add notes")
        print("4. View notes")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_study_file()
        elif choice == "2":
            view_study_files()
        elif choice == "3":
            study_and_add_notes()
        elif choice == "4":
            view_notes()
        elif choice == "5":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()
