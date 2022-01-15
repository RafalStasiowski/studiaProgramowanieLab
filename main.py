from model.Zamowienie import Zamowienie
from model.Dieta import Dieta
from model.Pacjent import Pacjent
from model.Dietetyk import Dietetyk

dieta1 = Dieta("Ketogeniczna", 300, 2000, "Dieta bez węglowodanów")
dieta2 = Dieta("Owocowa", 150, 1860, "Dieta zawierająca tylko owoce")
dieta3 = Dieta("Warzywna", 200, 2000, "Dieta zawierająca tylko warzywa")
dieta4 = Dieta("Dieta cud", 700, 2300, "Dobra dieta")

diety = [dieta1, dieta2, dieta3, dieta4]

pacjent = Pacjent("Jan", "Kowalski", "M", 21)
dietetyk = Dietetyk("Paweł", "Nowak", "M", 37, 200)

zamowienie = Zamowienie()
zamowienie.diety = diety
zamowienie.pacjent = pacjent
zamowienie.dietetyk = dietetyk
zamowienie.opis = "Zamowienie numer 1"


print(zamowienie.__str__())

print(zamowienie.suma())
print(zamowienie.suma_kalorii())
