from DOMAIN.Medicament import Medicament
from SERVICE.ServiceError import ServiceError
import random


class MedicamentService:

    def __init__(self, repository, transaction_repository, validator):
        self.__repository = repository
        self.__transaction_repository = transaction_repository
        self.__validator = validator

    def AddMedicament(self, id_medicament, name, producer, price, recipe):
        """
                 Creates a medicament
                    :param id_medicament: int, the medicament id.
                    :param name: str, the name of the medicament.
                    :param producer: str, producer of the medicament
                    :param price: float
                    :param recipe: str, bool
         """
        if recipe == "Yes":
            recipe = True
        else:
            recipe = False
        medicament = Medicament(id_medicament, name, producer, price, recipe)
        self.__validator.validate(medicament)
        self.__repository.create(medicament)

    def remove_medicament(self, id_medicament):
        if self.__repository.read(id_medicament) is not None:
            self.__repository.delete(id_medicament)
        else:
            raise ServiceError()

    def get_all(self):
        return self.__repository.read()

    def random_medicament(self, idm):
        name = ["Propolis", "Nurofen", "Strepsils", "RinoSun", "System Well", "Respiratory Protect", "Paracetamol",
                "Aspirina", "Lioton Gel", "Vitamina C", "Colebil", "Nose Protect", "Health Care", "Decasept"]
        producer = ["Sun Wave", "UK Meds", "ZenPharma", "Catena", "Biofarm", "RoDrugs", "USDrugs", "Paracetamol", "MD3",
                    "Bayern", "Labormed", "Abbott", "Sanofi", "Pfizer", "Servier", "Merck & Co", "Astellas Pharma"]
        price = [46.6, 78.4, 34.7, 89.5, 14.2, 456.7, 35.6, 139.4, 356.9, 24.8, 9.9, 567.8, 34.78, 96.4, 5.9, 45.9, 8.9]
        medicament = Medicament(idm, random.choice(name), random.choice(producer), float(random.choice(price)),
                                random.choice(["Yes", "No"]))
        return medicament

    def populate(self, n):
        lis = sorted(self.get_all(), key=lambda medicament: medicament.id_entity)
        i = 0
        while i <= n:
            for med in lis:
                if med.id_entity == i:
                    i += 1
                    n += 1
            medicament = self.random_medicament(i)
            self.__repository.create(medicament)
            i += 1
    '''
    def load_f(self, file):
        lista = []
        try:
            f = open(file, "r")
            line = f.readline().strip()
            while line != "":
                word = line
                line = f.readline().strip()
                lista.append(word)
            f.close()
        except FileNotFoundError:
            print("The File does not exits")
        return lista
    '''

    def raisePriceByOne(self, increaseprice):
        for medicament in self.__repository.read():
            if increaseprice > medicament.price:
                newMedicament = Medicament(medicament.id_entity, medicament.name, medicament.producer, (medicament.price * 101)/100 , medicament.recipe)
                self.__repository.update(newMedicament)
