import csv

class Item:
    pay_rate = 0.8 # This is a global attribute (the pay rate after 20% discount)
    all =[]
    def __init__(self, name: str, price: float, quantity=0): # will be called autmatically by the instance and will be passed in it as 'self'

        #Assert allows us to validate values being passed in a method or functions
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Price {price} is not greater than or equal to 0"

        # assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self) # self here being the instances that will be created

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment):
         self.__price = self.__price + self.__price * increment

    @property #this decorator will make it a read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) >10:
            raise Exception("Name too long")
        else:
            self.__name = value

    def calculate_total_price(self):   # functions inside a class are called "methods"
        return self.__price * self.quantity
# self refrences the current instance of a class and allows it access to the variables inside of the class
# the fact that we have the __init__ constructor allows us access in different functions to the attricutes already assigned in __init__ through 'self'



    @classmethod
    def instantiate_from_csv(cls): #this wqill only reference the class to instantiate objects
        with open('items.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            items = list(reader)

            for item in items:
                Item(
                    #creating instances/objects from the csv based on whats in the csv file using for loop
                    name = item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity')),
                )

    @staticmethod #statsic methods does not pass the instance/object of a class as an argument
    def is_integer(num):
        # removing the zero decimal place
        if isinstance(num,float):
            # count out the decimal 0
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    def __repr__(self): # used to control how we represent the object
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}','{self.quantity}"