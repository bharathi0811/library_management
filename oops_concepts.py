class LibraryItem:
    def __init__(self, id_no, title, year):
        self.id_no = int(id_no)
        self.title = title
        self.year = year
    def show_private(self):
        print(self.id_no, self.title,self.year)

class Book(LibraryItem):
    def __init__(self, id_no, title, year, author):
        super().__init__(id_no, title, year)
        self.author = author
    def show(self):
        print(self.id_no, self.title,self.year,self.author)

class Magazine(LibraryItem):
    def __init__(self, id_no, title, year, issue):
        super().__init__(id_no, title, year)
        self.issue = issue
    def show(self):
        print(self.id_no, self.title,self.year,self.issue)

# Creating objects
book1 = Book("6", "python", 1991, "guido van rossum")
magazine1 = Magazine(2, "National Geographic", 2022, 12)
book1.show_private()
book1.show()
magazine1.show()
magazine1.show_private()

+
