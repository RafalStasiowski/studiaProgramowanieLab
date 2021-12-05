import model.Firma as Firma

class FirmaSpozwcza(Firma):
    def __init__(self,nazwa:str, lokalizacja: str, ilosc_pracownikow: int, branza: str, powierzchnia_magazynu: float, nr_telefonu: str):
        super(FirmaSpozwcza, self).__init__(nazwa,lokalizacja,ilosc_pracownikow)
        self.__branza = branza
        self.__powierzchnia_magaznu = powierzchnia_magazynu
        self.__nr_telefonu = nr_telefonu

    def __str__(self) -> None:
        super.__str__()
        return (" branza: {}, powierzchnia magazynu: {}, numer telefonu: {}".format(self.__branza,self.__powierzchnia_magaznu, self.__nr_telefonu))

