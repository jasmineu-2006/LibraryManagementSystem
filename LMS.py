# Simple Library Management System

library = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("No books available.\n")
        return

    for book in library:
        status = "Available" if book["available"] else "Issued"
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")
    print()

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for book in library:
        if book["id"] == book_id and book["available"]:
            book["available"] = False
            print("Book issued successfully!\n")
            return
    print("Book not available or ID not found.\n")

def return_book():
    book_id = input("Enter Book ID to return: ")
    for book in library:
        if book["id"] == book_id and not book["available"]:
            book["available"] = True
            print("Book returned successfully!\n")
            return
    print("Invalid Book ID or book already returned.\n")

def menu():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
