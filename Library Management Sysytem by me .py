class Library :

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("BOOKS PRESENT IN THIS LIBRARY ARE : ")
        for books in self.books:
            print("  -",books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"YOU HAVE BEEN ISSUED THE BOOK '{bookName}'. PLEASE RETURN IT WITHIN 30 DAYS")
            self.books.remove(bookName)
            return True
        else:
            print(f"THE BOOK '{bookName}' IS EITHER NOT AVAILABLE OR HAS ALREADY BEEN ISSUED TO A STUDENT. PLZ WAIT UNTIL THE BOOK IS AVAILABLE")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("THANKS FOR RETURNING THE BOOK. HOPE YOU ENJOYED READING IT!")

class Students:
    def requestBook(self):
        self.books = input("ENTER THE NAME OF THE BOOK YOU WANT TO BORROW : ")
        return self.books

    def returnBook(self):
        self.books = input("ENTER THE NAME OF THE BOOK YOU WANT TO RETURN : ")
        return self.books

if __name__ == "__main__":
    centralLibrary = Library(["Algorithm", "Django", "Clrs", "Python Notes"])
    student = Students()
    while(True):
        welcomeMsg = '''\n
        =====WELCOME TO CENTRAL LIBRARY=====
        PLAESE CHOOSE FROM THE FOLLOWING OPTIONS:
        1. LISTING ALL THE BOOKS
        2. REQUEST A BOOK
        3. RETURN/DONATE A BOOK
        4. EXIT THE LIBRARY
        '''
        print(str(welcomeMsg))
        a = int(input("ENTER A CHOICE : "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("THANKS FOR CHOOSING CENTRAL LIBRARY. HAVE A GREAT DAY!")
            exit()

        else:
            print("INVALID CHOICE")