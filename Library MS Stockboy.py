
import sys
import copy
class Book(object):

    def __init__(self, newTitle, newGenre, newAuthor, inStock):
        self.title = newTitle
        self.genre = newGenre
        self.author = newAuthor
        self.inStock = inStock



    def delete(self):
        del self

    def __repr__(self):
        return self.title + ' is a ' + self.genre + ' novel by ' + self.author

newBook1 = Book("Python Power", "programming", "Thomas Protheroe", True)
newBook2 = Book("Tickle My Ivories", "music education", "Dylan Kelk", True)
newBook3 = Book("Samurai Soup", "travel", "Jason Shenkenfelder", True)

Books = [(newBook1), (newBook2), (newBook3)]

Books.append(Book("Simulation Theory", "futurism", "Muse", True))

class Library:
      def __init__(self, Books):

            self.availablebooks = Books

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   print("================================")
                   for book in self.availablebooks:
                         print (book)

      def stockCheck(self, bookTitle):
          for i in range(0, len(self.availablebooks)):
              if self.availablebooks[i].title == bookTitle:
                  if self.availablebooks[i].inStock == True:
                      print(self.availablebooks[i].title +" is currently in stock.")
                  else:
                      print("Seems like it isn't in stock now. let me check with the head librarian.")
                  return
          print("I don't think that is even a book from this library, but this is just my part-time job.")

      def lendBook(self, bookTitle):
            for i in range(0, len(self.availablebooks)):
                if self.availablebooks[i].title == bookTitle:

                  if self.availablebooks[i].inStock == False:
                      print("That book is currently not in stock")
                      return
                  copiedBook = copy.deepcopy(self.availablebooks[i])
                  self.availablebooks[i].inStock = False
                  #self.availablebooks.pop(i)
                  #print (self.availablebooks[i].title + " - " + str(self.availablebooks[i].inStock))
                  #exit
                  print("The book you requested has now been borrowed.")
                  return copiedBook

            print("Sorry the book you have requested is currently not in the library.")

      def addBook(self,bookToReturn):

           if (type(bookToReturn) is not Book):
              print("Error. Unable to return book. Please don't contact the system admin, he's got enough to do already.")
           #else:
                #self.availablebooks.append(bookToReturn)
              return

           for i in range(0, len(self.availablebooks )):

               if bookToReturn.title == self.availablebooks[i].title and self.availablebooks[i].inStock == False:

                   self.availablebooks[i].inStock = True
                   return
           print("Sorry, but this doesn't seem to be one of our books")



class User:
      def __init__(self):
            self.borrowedBook = None

      def stockBoy(self):
          print("Enter the name of the book you'd like our stock boy to check>>")
          self.book= input()
          return self.book

      def requestBook(self):
          if (self.borrowedBook != None):
              return False
          print("Enter the name of the book you'd like to borrow>>")
          self.book= input()
          return self.book

      def returnBook(self):
          if (self.borrowedBook == None):
              return False
          bookToReturn = self.borrowedBook
          self.borrowedBook = None

          return bookToReturn
            #print("Enter the name of the book you'd like to return>>")
            #self.book= input()
            #return self.book
try:
 def main():
    library = Library(Books)
    user = User()
    done = False
    while done == False:
        print("""=====LIBRARY MENU=====
              1. Display all available books
              2. Check stock
              3. Request a book
              4. Return a book
              5. Exit
                """)
        choice = int(input("Enter Your Choice:"))
        if choice == 1:
                 library.displayAvailablebooks()
        elif choice == 2:
                 library.stockCheck(user.stockBoy())
        elif choice == 3:
                 requestedBook = user.requestBook()
                 if (requestedBook == False):
                     print("You already have a book checked out.")
                 else:
                     borrowedBook = library.lendBook(requestedBook)
                     user.borrowedBook = borrowedBook
        elif choice == 4:
                 bookToReturn = user.returnBook()
                 if (bookToReturn == False):
                     print("You don't currently have a book checked out.")
                 else:
                     library.addBook(bookToReturn)
                     print("You have returned " + bookToReturn.title + ".Thank you!")
        elif choice == 5:
            print("See you next time.")
            sys.exit()
 main()
except ValueError:
    print("Remember to input a numerical choice first. See you next time!")