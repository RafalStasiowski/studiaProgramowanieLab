from model.Pojazd import Pojazd
from model.Kurs import Kurs
from model.Odcinek import Odcinek

odcinki = [Odcinek(10,"Katowice","Sosnowiec",2000,True),Odcinek(10,"Katowice","Sosnowiec",2000,True),Odcinek(10,"Katowice","Sosnowiec",2000,True),]

pojazd = Pojazd("ciężarowy",4.5, 10, "MAN", "SK 42123")
kurs = Kurs(odcinki,pojazd,"świeże bułki",7,"Jan Kowalski")

print(kurs.__str__())
print(kurs.marka_pojazdu())
print(kurs.wylicz_sume_kilometrow())


