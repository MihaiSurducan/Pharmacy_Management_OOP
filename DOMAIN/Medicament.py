from DOMAIN.Entity import Entity


class Medicament(Entity):

    def __init__(self, id_medicament, name, producer, price, recipe):
        """
         Creates a medicament
            :param id_medicament: int, the medicament id.
            :param name: str, the name of the medicament.
            :param producer: str, producer of the medicament
            :param price: float
            :param recipe: str, bool
        """
        super(Medicament, self).__init__(id_medicament)
        self.__name = name
        self.__producer = producer
        self.__price = price
        self.__recipe = recipe

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def producer(self):
        return self.__producer

    @producer.setter
    def producer(self, newProducer):
        self.__producer = newProducer

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, newPrice):
        self.__price = newPrice

    @property
    def recipe(self):
        return self.__recipe

    @recipe.setter
    def recipe(self, newRecipe):
        self.__recipe = newRecipe

    def __str__(self):
        return "Medicament {}, {}, {}, {}, {}".format(self.id_entity,
                                                      self.name,
                                                      self.producer,
                                                      self.price,
                                                      self.recipe
                                                      )

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity
