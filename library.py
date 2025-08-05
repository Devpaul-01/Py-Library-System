from datetime import datetime

books = {
    "1984": {"author": "George Orwell", "available_copies": 3},
    "The Hobbit": {"author": "J.R.R. Tolkien", "available_copies": 2},
    "To Kill a Mockingbird": {"author": "Harper Lee", "available_copies": 4},
    "Pride and Prejudice": {"author": "Jane Austen", "available_copies": 1},
    "The Catcher in the Rye": {"author": "J.D. Salinger", "available_copies": 2},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "available_copies": 3},
    "Moby Dick": {"author": "Herman Melville", "available_copies": 1}
}

borrowing_history = []
borrowed_books = []

def borrow_books(name, book_title):
    if not book_title:
        print("Please enter a book title.")
        return

    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    history_entry = {"user": name, "book": book_title, "action": "borrowed", "date": time}

    if book_title in books:
        book_info = books[book_title]
        if book_info["available_copies"] > 0:
            # Check if user has borrowed a book today
            for s in borrowing_history:
                if s["user"] == name and s["date"].split()[0] == time.split()[0]:
                    print("You borrowed a book today. Kindly return it before borrowing another one.")
                    return

            print("You are eligible to borrow a book.")
            borrowed_books.append(history_entry)
            borrowing_history.append(history_entry)
            book_info["available_copies"] -= 1
            print(f"Book '{book_title}' borrowed successfully.")
        else:
            print("No copies available at the moment.")
    else:
        print("Book not found.")

def return_books(name, book_title):
    if not book_title:
        print("Please enter a book title.")
        return

    found = False
    for s in borrowed_books:
        if s["user"] == name and s["book"] == book_title and s["action"] == "borrowed":
            found = True
            borrowed_books.remove(s)
            books[book_title]["available_copies"] += 1
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return_entry = {"user": name, "book": book_title, "action": "returned", "date": now}
            borrowing_history.append(return_entry)
            print(f"Book '{book_title}' returned successfully.")
            break

    if not found:
        print("Book not found in borrowed list.")

def most_borrowed():
    if not borrowing_history:
        print("No borrowing history yet.")
        return

    book_counts = {}
    for s in borrowing_history:
        book = s["book"]
        if book in book_counts:
            book_counts[book] += 1
        else:
            book_counts[book] = 1

    sorted_dict = dict(sorted(book_counts.items(), key=lambda item: item[1], reverse=True))
    print("📚 Most Borrowed Books:")
    for i, (book, count) in enumerate(sorted_dict.items()):
        if i >= 3:
            break
        print(f"{i+1}. {book} - borrowed {count} times")

def active_users():
    if not borrowing_history:
        print("No borrowing history yet.")
        return

    user_counts = {}
    for s in borrowing_history:
        user = s["user"]
        if user in user_counts:
            user_counts[user] += 1
        else:
            user_counts[user] = 1

    sorted_users = dict(sorted(user_counts.items(), key=lambda item: item[1], reverse=True))
    print("🏆 Top Active Users:")
    for i, (user, count) in enumerate(sorted_users.items()):
        if i >= 3:
            break
        print(f"{i+1}. {user} - borrowed {count} times")

def borrowed_list():
    if not borrowed_books:
        print("No books are currently borrowed.")
        return

    print("📖 Borrowed Books:")
    for s in borrowed_books:
        print(f"{s['user']} borrowed '{s['book']}' on {s['date']}")

def zero_copies():
    print("📕 Books with Zero Copies:")
    for title, details in books.items():
        if details["available_copies"] == 0:
            print(f"- {title}")

def user_history(name):
    if not borrowing_history:
        print("No history found.")
        return
    found_borrow = False
    found_return = False
    print(f"\n📘 Borrowing history for {name}:")
    for h in borrowing_history:
        if h["user"] == name and h["action"] == "borrowed":
            print(f"Borrowed '{h['book']}' on {h['date']}")
            found_borrow = True

    print(f"\n📗 Returning history for {name}:")
    for h in borrowing_history:
        if h["user"] == name and h["action"] == "returned":
            print(f"Returned '{h['book']}' on {h['date']}")
            found_return = True
    if not found_borrow:
        print("You are not among user borrowed history")
    if not found_return:
        print("You are not among the user return list")