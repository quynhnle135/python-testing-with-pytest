class Order:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity
        self.__filled = False

    def fill(self, warehouse):
        has_inventry = warehouse.has_inventory(self.__product, self.__quantity)
        if has_inventry:
            warehouse.remove(self.__product, self.__quantity)
            self.__filled = True

    def is_filled(self):
        return self.__filled