from item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # super function allows for access from the parent class
        super().__init__(name, price, quantity)
        #Assert allows us to validate values being passed in a method or functions

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to 0"

        # assign to self object
        self.broken_phones = broken_phones

