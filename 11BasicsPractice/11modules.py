class Library:
    def __init__(self, *books):
        self.books = books

    def __len__(self):
        return len(self.books)

library = Library("Book1", "Book2", "Book3")
print(len(library))  # Calls __len__
