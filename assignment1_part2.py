class Book:
    def __init__(self, name, title):
#Used __init__ to establish what attributes I wanted to call into the class set
        self.name = name
        self.title = title
#Requested that we have an author and title of their book as attributes
#Im assuming that each data set is an object ?
    def display(self):
        print( self.title, self.name)
#Researching this function was interesting because I kept getting calling errors because of syntax
#Made this function called display to print out our objects. Using self. made it so that we can pass through what ever
#data we atached to the attribute

author1 = Book("John Seinbeck " ," Of Mice Of Men, written by")
author2= Book("Harper Lee" , " To Kill a Mocking Bird, written by")

author1.display()
author2.display()

