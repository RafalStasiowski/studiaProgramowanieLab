class Book:
    def __init__(self, library: str, publication_date: str, author_name: str, author_surname: str , number_of_pages: str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return "Autor: {} {}. Ilośc stron: {}".format(self.author_name,self.author_surname,self.number_of_pages)
