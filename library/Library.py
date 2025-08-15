class Library:
    
    def __init__(self,number_of_copies, school_name, address, ISBN, title, author, rack):
        self.__number_of_copies = number_of_copies
        self.__school_name = school_name
        self.__address = address
        self.__ISBN = ISBN
        self.__title = title
        self.__author = author
    
    def library(self):
        try:
            for i in range(self.number_of_copies):


    