class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return "Biblioteka: {}, {}, {}. Godziny otwarcia {}, Telefon: {}".format(self.city, self.zip_code, self.street,self.open_hours,self.phone)


class Order:
    def __init__(self, employee: str, student: str, books: str, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return "Książka: {}, data: {}".format(self.books,self.order_date)


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hired_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return "{} {}. Urodzony: {}. Miejsce zamieszkania: {}, {}, {}".format(self.first_name,self.last_name,self.city, self.zip_code, self.street)


class Book:
    def __init__(self, library: str, publication_date: str, author_name: str, author_surname: str , number_of_pages: str):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return "Autor: {} {}. Ilośc stron: {}".format(self.author_name,self.author_surname,self.number_of_pages)

lib1 = Library("Katowice", "Sokolska", "123-12","8-16","634643643")
lib2 = Library("Sosnowiec", "Sosnowska", "321-12","10-18","532432432")

book1 = Book("lib1", "20-11-2021","Jan","Kowalski",53)
book2 = Book("lib2", "20-11-2021","Paweł","Nowak",53)
book3 = Book("lib3", "20-11-2021","Grzegorz","Kowalski",53)
book4 = Book("lib2", "20-11-2021","Jan","Kowalski",53)
book5 = Book("lib1", "20-11-2021","Jan","Kowalski",53)

pracownik1 = Employee("Jan","Kowalski","20-11-2021","20-11-1981","Katowice", "Sokolska", "342-42")