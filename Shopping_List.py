class ShoppingListKM:
# Initializer
    def __init__(self, name, amount):
        self.__name = name
        self.__amount = amount
        self.__price = self.__PriceListKM()
        self.__calcuprice = self.CostCalculateKM()


# List
    def __PriceListKM(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__name == "Moose Cheese":
            self.__price = 487.20
        elif self.__name == "White Truffles":
            self.__price = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__price = 270.81
        else:
            self.__price = 0.00

        return self.__price

# Calculation
    def CostCalculateKM(self):
        self.__calcuprice = self.__amount * self.__price
        return self.__calcuprice

# Accessor
    def getNameKM(self):
        return self.__name

    def getAmountKM(self):
        return self.__amount

    def getPriceKM(self):
        return self.__price

    def getCalcupriceKM(self):
        return self.__calcuprice