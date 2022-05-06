class library:
    def __init__(self,listofbooks):
        self.books=listofbooks 
        
    def borrowbook(self,book):
        if book in self.books:
            print(book+" is been issued to you. please return it in 14 days")
            self.books.remove(book)
        else :
         print("This book is not available in Library" )

    def returnbook(self,book):
            self.books.append(book)
            print( book +" book has been returned to Library" )

    def booksAtlibrary(self):
        print("Availble books at library are: ")
        for book in self.books:
            print("\t*" + book)
        
class student:
    def needbook(self):
        self.book= input("please enter the book you want:")
        return self.book
    def returnbook(self):
        self.book= input("please enter the book you want to return or add: ")
        return self.book
try:      
    if __name__ == "__main__":
        bhujlibrary = library (["harry potter","himym","friends","got"])
        kid = student()
        while(True):
            print('''**** welcome to Bhuj library****
            1 : list of books
            2 : borrow book
            3 : return or add book
            4 : exit the library  ''')
            a=int(input("enter the choice: "))
            if a==1:
                bhujlibrary.booksAtlibrary()
            elif a==2:
                bhujlibrary.borrowbook(kid.needbook())
            elif a==3:
                bhujlibrary.returnbook(kid.returnbook())
            elif a==4:
                print("thanks for using library")
                exit()
            else:
                print("invalid number")

except:
    print("This is not valid")

        

