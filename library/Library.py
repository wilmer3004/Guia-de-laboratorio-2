import Book
class Library:
    def __init__(self, school_name="", address=""):
        self.number_of_copies = 3   # same as in Java
        self.school_name = school_name
        self.address = address
        self.shelf = {}  # dictionary instead of Hashtable

        try:
            for i in range(self.number_of_copies):
                book = Book("", "", "", id=i)
                book.book_data(i)   # asks the user for ISBN, title, author
                self.shelf[i] = book
        except Exception as e:
            print("Error adding book:", e)

    def generate_report(self):
        report = ""
        for i in range(self.number_of_copies):
            temp_book = self.shelf.get(i)
            report += (
                f"{temp_book.get_ISBN()} - "
                f"{temp_book.get_title()} "
                f"({temp_book.get_author()})\n"
            )
        print("\n--- Books Report ---")
        print(report)


if __name__ == "__main__":
    solution = Library("Central School", "123 Street")
    solution.generate_report()
