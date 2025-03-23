from abc import ABC, abstractmethod

class Library():
    def __init__(self, name, max_books):
        self.name = name
        self.max_books = max_books
        self.books = []

    def get_listOfbooks(self):
        for book in self.books:
            print(book.displayInfo())
            

    def add_book(self, book):
        if len(self.books) < self.max_books:
            self.books.append(book)
            return True
        return False
    
    def delete_book(self, book):
        if len(self.books) != 0:
            self.books.remove(book)
            return True
        return False

class IReadable(ABC):
    @abstractmethod
    def read(self):
        ...

class Book(IReadable):
    def __init__ (self, name, author, bookYear):
        self.name = name
        self.author = author
        self.bookYear = bookYear
    pass
    def displayInfo(self):
        print(f"Book name: {self.name}")
        print(f"Book author: {self.author}")
        print(f"Book year: {self.bookYear}")
        
    def read(self):
        print(f"{self.name} is reading by me")

class Ebook(Book, IReadable):
    def __init__ (self, name, author, bookYear, bookFormat):
        super().__init__(name, author, bookYear)
        self.bookFormat = bookFormat
        
    def displayInfo(self):
        print(f"Book name: {self.name}")
        print(f"Book author: {self.author}")
        print(f"Book year: {self.bookYear}")
        print(f"Book format: {self.bookFormat}")
    
    def read(self):
        print(f"{self.name} is reading by me")

class Magazine(Book):
    def __init__(self, name, author, bookYear, issueNymber):
        super().__init__(name, author, bookYear)
        self.issueNumber = issueNymber 

    def displayInfo(self):
        print(f"Book name: {self.name}")
        print(f"Book author: {self.author}")
        print(f"Book year: {self.bookYear}")
        print(f"Issue Number: {self.issueNumber}") 

def reading(readable : IReadable):
    print(readable.read())

if __name__ == "__main__":
    my_book = Book("Verwolf", "J.Catrick", 1976)
    my1st_electro = Ebook("1984", "Jorj Oruel", 1948, "ebook")
    my_magazine = Magazine("Playboy", "Jorj Washington DC", 2002, 67)
    library = Library("National Minsk Library", 1000)
    library.add_book(my_book)
    library.add_book(my1st_electro)
    library.add_book(my_magazine)