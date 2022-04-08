bookdata=["Algorithms", "Django", "C++", "Python"]
adminpassword="admin123"
def books():
    for i in bookdata:
        print(i)
def requestBook():
        book = input("Enter the name of the book you want to borrow: ")
        if book in bookdata:
            print("You have been issued {book}. Please keep it safe and return it within 30 days")
            bookdata.remove(book)
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False
def returnBook():
        book = input("Enter the name of the book you want to return: ")
        bookdata.append(book)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        return book
while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            books()
        elif a == 2:
            requestBook()
        elif a == 3:
            returnBook()
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
