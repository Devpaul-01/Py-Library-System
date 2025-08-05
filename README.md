🏛️ Oluwaseyi Library System

A simple but powerful **Library Borrowing System** built with Python.  
It manages books, tracks borrowing and returning, and provides live analytics — just like a real-world library backend.



🚀 Features

- 📚 Borrow and return books with real-time timestamp logging
- 👤 Tracks complete user borrowing and return history
- 🔄 Automatically updates available book copies
- 🧠 Prevents users from borrowing more than one book per day without returning
- 📊 Built-in analytics dashboard:
  - Top 3 most borrowed books
  - Top 3 most active users
  - Live list of currently borrowed books
  - Books with zero available copies
  - Borrowing and return history for each user


🧱 Built With

- Python 3
- `datetime` module for timestamp tracking
- Lists and Dictionaries for state management and data storage

---

 📂 File Structure

- `library.py` → Core backend logic: borrowing, returning, analytics, and data handling
- `librarymain.py` → CLI-based menu system for user interaction and command handling
