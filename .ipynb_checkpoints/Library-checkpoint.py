class Book():
    def __init__(self, title, author, year, price, pages, rating, reviews ):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = False
        self.pages = pages
        self.rating = rating
        self.reviews = reviews
    def get_info(self):
        print(f'Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nPrice: {self.price}\nStoplist: {self.stoplist}\nPages: {self.pages}\nRating: {self.rating}\n')
    
    def set_stoplist(self, stoplist_value):
        if isinstance(stoplist_value, bool):
            self.stoplist = stoplist_value
        else:
            raise ValueError('Please, input the boolean variable')
        
    def censor(self):
        author = input('Enter the author name: ')
        stop_list_value = input('Enter the value True or False: ')
        if author == self.author:
            if stop_list_value.lower() == 'true':
                self.stoplist = True
            elif stop_list_value.lower() == 'false':
                self.stoplist = False
        else:
            if stop_list_value.lower() == 'true':
                self.stoplist = False
            elif stop_list_value.lower() == 'false':
                self.stoplist = True
        print(f'The stoplist value is {self.stoplist}')
        
    @classmethod
    def get_expensive(cls, books):
        ex_book = max(books, key = lambda x: x.price)
        # return ex_book.title
        print(f'The most expensive book is {ex_book.title} by {ex_book.author}\nIts price is ${ex_book.price}')
    @classmethod
    def get_h_and_l_rating(cls,books):
        b_book = max(books, key = lambda x: x.rating)
        w_book = min(books, key = lambda x: x.rating)
        print(f'Book with the highest rating is "{b_book.title}". Its rating is {b_book.rating}')
        print(f'Book with the lowest rating is "{w_book.title}". Its rating is {w_book.rating}')
    @classmethod
    def get_longest(cls, books):
        l_book = max(books, key = lambda x: x.pages)
        print(f'The longest book is "{l_book.title}". It is {l_book.pages} long')
    @classmethod
    def get_most_reviewed(cls, books):
        r_book = max(books, key = lambda x: x.reviews)
        print(f'The most reviewed book is {r_book.title}. It has {r_book.reviews} reviews')