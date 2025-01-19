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


# ChittagongPizza Class (Adaptee)
class ChittagongPizza:
    def sausage(self):
        print("Ctg pizza")

    def bread(self):
        print("Ctg bread")


# Object Adapter Class for ChittagongPizza to implement Pizza
class ChittagongObjectAdapter(Pizza):
    def __init__(self, adaptee):
        """Initialize with an instance of ChittagongPizza."""
        self.adaptee = adaptee

    def toppings(self):
        # Delegate the call to the adaptee's sausage method
        self.adaptee.sausage()

    def bun(self):
        # Delegate the call to the adaptee's bread method
        self.adaptee.bread()


# Driver Code
if __name__ == "__main__":
    # Using DhakaStylePizza
    dhaka_pizza = DhakaStylePizza()
    dhaka_pizza.toppings()  # Output: Dhaka cheese toppings
    dhaka_pizza.bun()       # Output: Dhaka bread bun

    # Using ChittagongObjectAdapter
    ctg_pizza = ChittagongPizza()  # Original ChittagongPizza object
    pizza_adapter = ChittagongObjectAdapter(ctg_pizza)  # Adapter wraps the object

    pizza_adapter.toppings()  # Output: Ctg pizza
    pizza_adapter.bun()       # Output: Ctg bread
