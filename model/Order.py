
class Order:
    def __init__(self, employee: str, student: str, books: str, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return "Książka: {}, data: {}".format(self.books,self.order_date)
