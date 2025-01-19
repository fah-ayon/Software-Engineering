class MagicalCake:
    # Singleton instance
    _instance = None

    def __new__(cls):
        """Override __new__ to ensure only one instance is created."""
        if cls._instance is None:
            print("Preparing the magical cake for the first time!")
            cls._instance = super(MagicalCake, cls).__new__(cls)
        return cls._instance


# Driver Code
if __name__ == "__main__":
    # Multiple calls to create a magical cake
    cake1 = MagicalCake()
    cake2 = MagicalCake()
    cake4 = MagicalCake()
    cake6 = MagicalCake()

    # Printing the memory addresses of each instance
    print(cake1)
    print(cake2)
    print(cake4)
    print(cake6)
