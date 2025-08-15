class Book:
    
    # Constructor to initialize the book's attributes
    def __init__(self, ISBN, title, author, id=None):
        self.__ISBN = ISBN
        self.__title = title
        self.__author = author
        self.__id = id
    
    # Methods to get the book's
    # attributes
    def get_ISBN(self):
        return self.__ISBN
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_id(self):
        return self.__id
    
    # Method to set the book's id

    def set_id(self, id):
        self.__id = id

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author 

    def edit_fields(self, title, author):
        pass
    
    # This methos assigns and requests the book data
    def book_data(self, id):
        self.set_id(id)
        self.set_ISBN(input("Enter ISBN: "))
        self.set_title(input("Enter title: "))
        self.set_author(input("Enter author: "))



