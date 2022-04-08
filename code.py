from optparse import Values


bookdata=["Algorithms", "Django", "C++", "Python"]
studentdetails={'Ritik':'1901297109','Golu':'1901297108'}
admindetails={'Ritik':'12345'}

adminpassword="admin123"
def books():
    for i in bookdata:
        print(i)
def requestBook():
        book = input("Enter the name of the book you want to borrow: ")
        if book in bookdata:
            print("You have been issued "+book+" . Please keep it safe and return it within 30 days")
            bookdata.remove(book)
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False
def returnBook():
        book = input("Enter the name of the book you want to return: ")
        bookdata.append(book)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        return book
def exitlibrary():
    print("Thanks for choosing Central Library. Have a great day ahead!")
    exit()
def student():
    name=input("Enter your Name: ")
    rednum=input("Enter your Registered ID : ")
    if name in studentdetails.keys() and rednum in studentdetails.values():
        print("====== Welcome Back "+name+" ,Glad To See You ======")
        return
    else:
        print("You have not Registered With Us.Try to Resister First ")
        redmsg='''
        1.New Register
        2.Exit
        '''
        print(redmsg)
        continue_exit=int(input("Enter your choice: "))
        if continue_exit==1:
            name=input("Enter your Name: ")
            redid=input("Enter your Registration ID: ")
            studentdetails[name]=redid
            print("====== Welcome "+name+"======")
        if continue_exit==2:
            # print("Thanks for choosing Central Library. Have a great day ahead!")
            # exit()
            exitlibrary()
def detailofstudents():
    print("Student Name \t  Registered ID")
    for i in studentdetails:
        print(i + "\t \t\t"+studentdetails.get(i))
def admin():
    username=input("Enter your Username: ")
    password=input("Enter Password: ")
    if username in admindetails.keys() and password in admindetails.values():
        print("=== Welcome "+username+"====")
        return True
    else:
        print("Sorry , Admin Details Not Matched")
        return False
        # exitlibrary()




while(True):
        landingmsg='''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. Student Login
        2. Admin Login
        '''
        print(landingmsg)
        s_a=int(input("Enter a choice: "))
        student_admin=1
        welcomeMsg = '''
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        adminmsg='''
                Please choose an option:
                1. List all the books
                2. Add a book
                3. Students Detail
                4. Exit the Library
                '''
        if s_a==1:
            student()
            while(True):
                print(welcomeMsg)
                a = int(input("Enter a choice User: "))
                if a == 1:
                    books()
                elif a == 2:
                    requestBook()
                elif a == 3:
                    returnBook()
                elif a == 4:
                    exitlibrary()
                else:
                    print("Invalid Choice!")
        if s_a==2:
            valid=admin()
            
            while(valid):
                print(adminmsg)
                a = int(input("Enter a choice User: "))
                if a == 1:
                    books()
                elif a == 2:
                    returnBook()
                elif a == 3:
                    detailofstudents()
                elif a == 4:
                    exitlibrary()
                else:
                    print("Invalid Choice!")
                
        else:
            print("!!!!Invalid Choice!!!!")
            print("Invalid Choice!")

        
