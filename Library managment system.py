class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" ♦-- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE \n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)


class Student():
    def requestBook(self):
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book



if __name__ == "__main__":

    Library = Library(
        ["vistas", "invention", "rich&poor", "indian", "macroeconomics", "microeconomics"])
    student = Student()
    track = []

    print("\t\t\t\t\t\t\t♦♦♦♦♦♦♦ WELCOME TO THE LIBRARY ♦♦♦♦♦♦♦\n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Track books\n5. exit the library\n""")

    while (True):
        # print(track)
        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                Library.displayAvailableBooks()
            elif usr_response == 2:  # borrow
                Library.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:  # return
                Library.returnBook(student.returnBook())
            elif usr_response == 4:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            
            elif usr_response == 5: #exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")
