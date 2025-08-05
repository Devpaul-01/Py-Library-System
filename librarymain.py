def borrow_book():
    name = input("Enter your name").lower()
    book_title = input("Enter the name of book you want to borrow").title()
    borrow_books(name, book_title)
def return_book():
    name = input("Enter your name").lower()
    book_title = input("Enter name of book you want to return").title()
    return_books(name, book_title)
def check_active():
    active_users()
def most_books():
    most_borrowed()
def borrowed_books():
    borrowed_list()
def non_available():
    zero_copies()
def history():
    name = input("Enter your name").lower()
    user_history(name)
while True:
    print("Welcome to oluwaseyi library")
    print("Kindly choose from the option below")
    print("Exit")
    print("Borrow book")
    print("Return book")
    print("Check most borrowed book")
    print("Check most active library users")
    print("Check currently borrowed books")
    print("Non available books")
    print("Check your library usage history")
    option = input("Enter your choice")
    if option == "1":
        print("Goodbye have a nice day")
    elif option == "2":
        borrow_book()
    elif option == "3":
        return_book()
    elif option == "4":
        most_books()
    elif option == "5":
        check_active()
    elif option == "6":
        borrowed_books()
    elif option == "7":
        non_available()
    elif option == "8":
        history()
        


    