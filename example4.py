class book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def __repr__(self):
        return f"book(title='{self.title}', author='{self.author}',isbn='{self.isbn}')"
    def __eq__(self,other):
        return self.isbn==other.isbn

class library:
    def __init__(self):
        self.books=[]
    def __repr__(self):
        return f"library with {len(self.books)} books"
    def __len__(self):
        return len(self.books)
    def __contains__(self,book):
        return book in self.books
    def __iter__(self):
        return iter(self.books)
    def add_book(self,book):
        if book in self.books:
            raise ValueError("book aready in the library")
        self.books.append(book)
    def remove_book(self,book):
        if book not in self.books:
            raise ValueError("book not found in the library")
        self.books.remove(book)
    def find_books_by_title(self,title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    def find_book_by_author(self,author):
        return[book for book in self.books if author.lower() in book.author.lower()]

book1=book("the catchter in the rye", "J.D salinger", "122345666667890")
book2=book("to kill a mockingbird", "harper lee", "2345663456")
book3=book("1984", "george orwell", "67667676778")
Library = library()
Library.add_book(book1)
Library.add_book(book2)
Library.add_book(book3)

print (Library)

for book in Library:
    print(book)

print(Library.find_books_by_title("1984"))

print(Library.find_book_by_author("harper lee"))

Library.remove_book(book2)

print (Library)

print(book2 in Library)
print(book1 in Library)
