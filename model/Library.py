class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return "Biblioteka: {}, {}, {}. Godziny otwarcia {}, Telefon: {}".format(self.city, self.zip_code, self.street,self.open_hours,self.phone)
