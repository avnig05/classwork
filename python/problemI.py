'''
Avni Gandhi
CIS 41A, Spring 2023
Unit I, Problem I
'''
class LibraryPatron:
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = []

    def checkOutBook(self, checkOutLimit, bookTitle):
        if (len(self.booksCheckedOut) >= checkOutLimit):
            print(f"Sorry {self.name} you are at your limit of {len(self.booksCheckedOut)}")
        else:
            self.booksCheckedOut.append(bookTitle)
            print(f"{self.name} has checked out {bookTitle}")
        

    def returnBook(self, book):
        bookTitle = book[0]
        if bookTitle in self.booksCheckedOut:
            self.booksCheckedOut.remove(bookTitle)
            print(f"{self.name} has returned {bookTitle}")

    def printCheckedOutBooks(self):
        print(f"{self.name} has the following books checked out:")
        for bookTitle in self.booksCheckedOut:
            print(bookTitle)


class AdultPatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 4

    def checkOutBook(self, book):
        super().checkOutBook(self.checkOutLimit, book[0]) 

class JuvenilePatron(LibraryPatron):
    def __init__(self, name):
        super().__init__(name)
        self.checkOutLimit = 2
        
    def checkOutBook(self, book):
        if book[1] == 'Adult':
            print(f"Sorry {self.name} {book[0]} is an adult book")
        else:
            super().checkOutBook(self.checkOutLimit, book[0])

book1 = ["Alice in Wonderland", "Juvenile"]
book2 = ["The Cat in the Hat", "Juvenile"]
book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
book4 = ["The Hobbit", "Juvenile"]
book5 = ["The Da Vinci Code", "Adult"]
book6 = ["The Girl with the Dragon Tattoo", "Adult"]

patron1 = JuvenilePatron("Jimmy")
patron2 = AdultPatron("Sophia")

patron1.checkOutBook(book6)
patron1.checkOutBook(book1)
patron1.checkOutBook(book2)
patron1.printCheckedOutBooks()
patron1.checkOutBook(book3)
patron1.returnBook(book1)
patron1.checkOutBook(book3)
patron1.printCheckedOutBooks()
patron2.checkOutBook(book5)
patron2.checkOutBook(book4)
patron2.printCheckedOutBooks()

'''
Execution results:
Sorry Jimmy The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit
'''

    
