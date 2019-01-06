import abc

class AbstractFactory(metaclass=abc.ABCMeta):
    """The factory (abstract) from which concrete factory inherits. Closer to a java-interface thing"""
    

    def get_factory(wantSoup=True):
        """selects the right concrete factory. Could obviously be more complex selection process"""
        if wantSoup:
            return ConcreteSoupFactory()
        else:
            return ConcreteSandwichFactory()

class ConcreteSoupFactory(AbstractFactory):
    """2 for 1: this also demonstrate the proper use of getters/setters in python (@properies instead of get() set()"""
    def __init__(self):
        self.ingredients = None
        self.stock = 'chicken'
        self.vedgies = 'mushrooms'

    ### Accessors functions ###
    @property
    def ingredients(self):
        return self.__ingredients       # __ before attr name

    @property
    def stock(self):
        return self.__stock

    @property
    def vedgies(self):
        return self.__vedgies

    @stock.setter
    def stock(self, v):
        if v in self.ingredients['stock']:
            self.__stock = v
        else:
            self.__stock = None

    @vedgies.setter
    def vedgies(self, v):
        if v in self.ingredients['vedgies']:
            self.__vedgies = v
        else:
            self.__vedgies = None

    @ingredients.setter
    def ingredients(self,v):    # __ before the attr. name
        self.__ingredients = {'stock': ['chicken', 'beef', 'vedgetables'], 'vedgies': ['carrot','brocoli', 'mushrooms']}

    def __repr__(self):
        return "This is a soup with " + str(self.stock) + " stock and " + str(self.vedgies)


class ConcreteSandwichFactory(AbstractFactory):
    def __init__(self):
        self.ingredients = {'breadType': ['white', 'whole wheat', '7 grains'],
                            'condiment': ['ketchup','mustard', 'sraricha'],
                            'stuffing': ['tomatoes', 'ham']}
        self.breadType = "7 grains"
        self.condiment = "mustard"
        self.stuffing = "ham"

    def __repr__(self):
        return "This is a sandwich with " + str(self.breadType) + " bread, " + str(self.condiment) + " and " + str(self.stuffing)


factoSoup = AbstractFactory.get_factory()
factoSoup.stock = 'beef'
factoSand = AbstractFactory.get_factory(wantSoup=False)
factoSand
print(factoSoup)
print(factoSand)