class Library:
    def __init__(self):
        self.noBook = 0
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        self.noBook = len(self.books)

    def showInfo(self):
        print(f"The Library hs {self.noBook} books")


li = Library()
li.addBook("Harry Potter")
li.addBook("Harry Potter")
li.addBook("Harry Potter")
li.showInfo()
