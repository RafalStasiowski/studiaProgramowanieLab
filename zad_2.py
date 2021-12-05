from model.Library import Library
from model.Book import Book
from model.Employee import Employee
from model.Order import Order

lib1 = Library("Katowice", "Sokolska", "123-12","8-16","634643643")
lib2 = Library("Sosnowiec", "Sosnowska", "321-12","10-18","532432432")

book1 = Book("lib1", "20-11-2021","Jan","Kowalski",53)
book2 = Book("lib2", "20-11-2021","Paweł","Nowak",53)
book3 = Book("lib3", "20-11-2021","Grzegorz","Kowalski",53)
book4 = Book("lib2", "20-11-2021","Jan","Kowalski",53)
book5 = Book("lib1", "20-11-2021","Jan","Kowalski",53)

pracownik1 = Employee("Jan","Kowalski","20-11-2021","20-11-1981","Katowice", "Sokolska", "342-42", "123123123")