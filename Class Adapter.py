from abc import ABC, abstractmethod

# Interface (Abstract Base Class) for Pizza
class Pizza(ABC):
    @abstractmethod
    def toppings(self):
        pass

    @abstractmethod
    def bun(self):
        pass


# DhakaStylePizza Class implementing Pizza
class DhakaStylePizza(Pizza):
    def toppings(self):
        print("Dhaka cheese toppings")

    def bun(self):
        print("Dhaka bread bun")


# ChittagongPizza Class (with different methods)
class ChittagongPizza:
    def sausage(self):
        print("Ctg pizza")

    def bread(self):
        print("Ctg bread")


# Adapter Class for ChittagongPizza to implement Pizza
class ChittagongAdapter(ChittagongPizza, Pizza):
    def toppings(self):
        self.sausage()  # Adapts `sausage` to `toppings`

    def bun(self):
        self.bread()  # Adapts `bread` to `bun`


# Driver Code
if __name__ == "__main__":
    # DhakaStylePizza usage
    dhaka_pizza = DhakaStylePizza()
    dhaka_pizza.toppings()  # Output: Dhaka cheese toppings
    dhaka_pizza.bun()       # Output: Dhaka bread bun

    # ChittagongClassAdapter usage
    ctg_pizza = ChittagongAdapter()
    ctg_pizza.toppings()  # Output: Ctg pizza
    ctg_pizza.bun()       # Output: Ctg bread

