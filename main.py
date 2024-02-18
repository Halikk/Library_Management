import sys


def menu():         # Define a function to display the menu options and perform operations based on user input
    choice = ""
    while choice != "q":
        # Display the menu options
        print("*** MENU ***" + "\n"
                               "1) List Books" + "\n"
                                                 "2) Add Book" + "\n"
                                                                 "3) Remove Book" + "\n"
                                                                                    "q) Quit" + "\n")

        choice = input("Enter the operation you want to perform:")     # Get user input for choice

        if choice == "1":       # Perform actions based on user choice
            Library.list_book(lib)
        elif choice == "2":
            Library.add_book(lib)
        elif choice == "3":
            Library.remove_book(lib)
        elif choice == "q" or choice == "Q":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid input")


class Library:      # Define a class named Library for managing books
    def __init__(self):
        try:        # Open the file containing book information (or create it if not exist)

            self.file = open("books.txt", "a+")
        except FileNotFoundError:
            print("File not found.")

    def __del__(self):
        self.file.close()

    def list_book(self):        # Method to list all books in the library # Method to list all books in the library
        print("*** Books in the Library ***")
        self.file.seek(0)       # Move the file pointer to the beginning
        readfile = self.file.read()
        book_list = readfile.splitlines()  # Split the content into lines (each line represents a book)

        for book in book_list:
            split_list = book.split(",")
            print("Book name: " + split_list[0] + " Author: " + split_list[1] + "\n")

        if len(book_list) == 0:            # If there are no books, display a message
            print("There are no books in the library!")

    def add_book(self):        # Method to add a new book to the library
        print("Please enter the book's information")
        book_name = input("Book name:")
        author = input("Author name:")
        release_date = input("Release date:")
        page_no = input("Number of pages:")
        # Create a string containing book information
        book_info = book_name + "," + author + "," + release_date + "," + page_no + "\n"
        print(book_name + " has been added.")
        self.file.write(book_info)

    def remove_book(self):    # Method to remove a book from the library
        flag = False
        book_name = input("Enter the name of the book you want to delete:")
        self.file.seek(0)
        readfile = self.file.read()
        book_list = readfile.splitlines()

        for i in range(len(book_list)):
            split_list = book_list[i].split(",")

            if split_list[0] == book_name:      # If the book name matches, remove the book from the list
                print(book_name + " has been deleted.")
                book_list.pop(i)
                flag = True
                break

        if flag:                                # If the book was found and removed, update the file
            self.file.truncate(0)
            for i in range(len(book_list)):
                split_list = book_list[i].split(",")
                for j in range(len(split_list)):
                    if len(split_list) != j + 1:
                        self.file.write(split_list[j] + ",")
                    else:
                        self.file.write(split_list[j] + "\n")
        else:
            print("Book not found!")


lib = Library()
menu()             # Display the menu and start the program
input()
