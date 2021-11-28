class Firma:
    def __init__(self,nazwa:str, lokalizacja: str, ilosc_pracownikow: int):
        self.__nazwa = nazwa
        self.__lokalizacja = lokalizacja
        self.__ilosc_pracownikow = ilosc_pracownikow

    @property
    def nazwa(self):
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, nowa_nazwa):
        self.__nazwa = nowa_nazwa

    @property
    def lokalizacja(self):
        return self.__lokalizacja

    @lokalizacja.setter
    def lokalizacja(self, nowa_lokalizacja):
        self.__lokalizacja = nowa_lokalizacja

    @property
    def ilosc_pracownikow(self):
        return self.__ilosc_pracownikow

    @ilosc_pracownikow.setter
    def ilosc_pracownikow(self, nowa_ilosc_pracownikow):
        self.__nowa_ilosc_pracownikow = nowa_ilosc_pracownikow



    def __str__(self) -> None:
        return ("Firma {}, znajdująca się pod adresem {}".format(self.__nazwa, self.__lokalizacja,self.__ilosc_pracownikow))


class Pojazd:
    def __init__(self, rodzaj: str, waga: float, maksymalny_udzwig: float, marka: str, numer_rejestracyjny: str):
        self.__rodzaj = rodzaj
        self.__waga = waga
        self.__maksymalny_udzwig = maksymalny_udzwig
        self.__marka = marka
        self.__numer_rejestracyjny = numer_rejestracyjny

    @property
    def rodzaj(self):
        return self.__rodzaj

    @rodzaj.setter
    def nazwa(self, nowy_rodzaj):
        self.__rodzaj = nowy_rodzaj

    @property
    def waga(self):
        return self.__waga

    @waga.setter
    def waga(self, nowa_waga):
        self.__waga = nowa_waga

    @property
    def maksymalny_udzwig(self):
        return self.__maksymalny_udzwig

    @maksymalny_udzwig.setter
    def maksymalny_udzwig(self, nowy_maksymalny_udzwig):
        self.__maksymalny_udzwig = nowy_maksymalny_udzwig

    @property
    def marka(self):
        return self.__marka

    @marka.setter
    def marka(self, nowa_marka):
        self.__maksymalny_udzwig = nowa_marka

    @property
    def numer_rejestracyjny(self):
        return self.__numer_rejestracyjny

    @numer_rejestracyjny.setter
    def numer_rejestracyjny(self, nowy_numer_rejestracyjny):
        self.__numer_rejestracyjny = nowy_numer_rejestracyjny


    def __str__(self) -> None:
        return ("Pojazd marki {}, o numerze rejestracyjnym: {}. Max udźwig: {}, waga: {}".format(self.__marka,self.__numer_rejestracyjny, self.__maksymalny_udzwig, self.__waga))

class Odcinek:
    def __init__(self, dystans: float, miejsce_startowe: str, miejsce_docelowe: str, wartosc: float, czy_krajowy: bool):
        self.__dystans = dystans
        self.__miejsce_startowe = miejsce_startowe
        self.__miejsce_docelowe = miejsce_docelowe
        self.__wartosc = wartosc
        self.__czy_krajowy = czy_krajowy

    @property
    def dystans(self):
        return self.__dystans

    @dystans.setter
    def dystans(self, nowy_dystans):
        self.__dystans = nowy_dystans

    @property
    def miejsce_startowe(self):
        return self.__miejsce_startowe

    @miejsce_startowe.setter
    def miejsce_startowe(self, nowe_miejsce_startowe):
        self.__miejsce_startowe = nowe_miejsce_startowe

    @property
    def miejsce_startowe(self):
        return self.__miejsce_docelowe

    @miejsce_startowe.setter
    def miejsce_startowe(self, nowe_miejsce_docelowe):
        self.__miejsce_docelowe = nowe_miejsce_docelowe

    @property
    def wartosc(self):
        return self.__wartosc

    @wartosc.setter
    def wartosc(self, nowa_wartosc):
        self.__wartosc = nowa_wartosc

    @property
    def czy_krajowy(self):
        return self.__czy_krajowy

    @czy_krajowy.setter
    def czy_krajowy(self, nowy_czy_krajowy):
        self.__czy_krajowy = nowy_czy_krajowy


    def __str__(self) -> None:
        return ("Odcinek pomiędzy {} a {}, wartość: {} zł, dystans: {} km".format(self.__miejsce_startowe,self.__miejsce_docelowe, self.__wartosc, self.__dystans))

class Kurs:
    def __init__(self, odcinki: list, pojazd: Pojazd, towar: str, masa_towaru: float, kierowca: str):
        self.__odcinki = odcinki
        self.__pojazd = pojazd
        self.__towar = towar
        self.__masa_towaru = masa_towaru
        self.__kierowca = kierowca

    @property
    def odcinki(self):
        return self.__odcinki

    @odcinki.setter
    def odcinki(self, nowe_odcinki):
        self.__odcinki = nowe_odcinki

    @property
    def pojazd(self):
        return self.__pojazd

    @pojazd.setter
    def pojazd(self, nowy_pojazd):
        self.__pojazd = nowy_pojazd

    @property
    def towar(self):
        return self.__towar

    @towar.setter
    def towar(self, nowy_towar):
        self.__towar = nowy_towar

    @property
    def masa_towaru(self):
        return self.__masa_towaru

    @masa_towaru.setter
    def masa_towaru(self, nowa_masa_towaru):
        self.__masa_towaru = nowa_masa_towaru

    @property
    def kierowca(self):
        return self.__kierowca

    @kierowca.setter
    def kierowca(self, nowy_kierowca):
        self.__kierowca = nowy_kierowca


    def wylicz_sume_kilometrow(self) -> float:
        odleglosc = 0
        for odcinek in self.__odcinki:
            odleglosc = odleglosc + odcinek.dystans
        return odleglosc

    def marka_pojazdu(self) -> str:
        return self.__pojazd.marka

    def __str__(self) -> None:
        return ("Pojazd: {}, towar: {}, masa_towaru: {}, kierowca: {}".format(self.__pojazd,self.__towar, self.__masa_towaru, self.__kierowca))


class FirmaTransportowa(Firma):
    def __init__(self,nazwa:str, lokalizacja: str, ilosc_pracownikow: int, pojazdy: list, kursy: list, kierowcy: list):
        super.__init__(nazwa,lokalizacja,ilosc_pracownikow)
        self.__pojazdy = pojazdy
        self.__kursy = kursy
        self.__kierowcy = kierowcy

    @property
    def pojazdy(self):
        return self.__pojazdy

    @pojazdy.setter
    def pojazdy(self, nowe_pojazdy):
        self.__pojazdy = nowepojazdy

    def __str__(self) -> None:
        super.__str__()
        return (" Pojazdy: {}, kursy: {}, kierowcy: {}, kierowca: {}".format(self.__pojazdy,self.__kursy, self.__kierowcy))


class FirmaSpozwcza(Firma):
    def __init__(self,nazwa:str, lokalizacja: str, ilosc_pracownikow: int, branza: str, powierzchnia_magazynu: float, nr_telefonu: str):
        super(FirmaSpozwcza, self).__init__(nazwa,lokalizacja,ilosc_pracownikow)
        self.__branza = branza
        self.__powierzchnia_magaznu = powierzchnia_magazynu
        self.__nr_telefonu = nr_telefonu

    def __str__(self) -> None:
        super.__str__()
        return (" branza: {}, powierzchnia magazynu: {}, numer telefonu: {}".format(self.__branza,self.__powierzchnia_magaznu, self.__nr_telefonu))


odcinki = [Odcinek(10,"Katowice","Sosnowiec",2000,True),Odcinek(10,"Katowice","Sosnowiec",2000,True),Odcinek(10,"Katowice","Sosnowiec",2000,True),]

pojazd = Pojazd("ciężarowy",4.5, 10, "MAN", "SK 42123")
kurs = Kurs(odcinki,pojazd,"świeże bułki",7,"Jan Kowalski")

print(kurs.__str__())
print(kurs.marka_pojazdu())
print(kurs.wylicz_sume_kilometrow())


