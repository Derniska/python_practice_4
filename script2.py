from Library import Book

book1 = Book('The secret history', 'Donna Tart', 1993, 9.54, 503, 4.3, 818266)
book2 = Book('Harry Portter and the Deathly Hallows','Joanne Rowling', 2007, 14.85, 640, 4.9, 3821354)
book3 = Book('Normal People', 'Sally Rooney', 2018, 3.04, 288, 4.3, 1521531)
book4 = Book('The Mixer: The Story of Premier League Tactics, from Route One to False Nines',
           'Michael Cox', 2017, 11.45,571, 4.39, 4851)

books = [book1, book2, book3, book4]
choices = [1,2,3,4,5,6]
num_choice = int(input('Please select one of the options:\n1: Get the info about the books\n2: Find the most expensive book \
                      \n3: Find the book with the highest and lowest rating\n4: Find the longest book \
                      \n5: Find the most reviewed book\n6: Check the author name\n'))
if num_choice in choices:
    if num_choice == 1:
        for book in books:
            book.get_info()
    if num_choice == 2:
        Book.get_expensive(books)
    if num_choice == 3:
        Book.get_h_and_l_rating(books)
    if num_choice == 4:
        Book.get_longest(books)
    if num_choice == 5:
        Book.get_most_reviewed(books)
    if num_choice == 6:
        book1.censor()
else:
    raise ValueError('Enter the correct number')
        
