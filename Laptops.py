from item import Item

class Laptop(Item):
    def __init__(self, name: str, price: int, quantity = 0, bad_batch = 0):
        super().__init__(name, price, quantity)

        assert bad_batch >= 0, f"Bad Batch {bad_batch} cannot be less than zero"

        self.bad_batch = bad_batch