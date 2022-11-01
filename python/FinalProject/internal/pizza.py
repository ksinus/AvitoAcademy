class Pizza:
    """Base pizza class"""

    def __init__(self,
                 ingredients: dict,
                 size: str = None,
                 name: str = None) -> None:
        self.name_ = name
        self.size_ = size
        self.ingredients_ = ingredients

    def dict(self) -> dict:
        return self.ingredients_

    def __eq__(self, other) -> bool:
        return self.ingredients_ == other.ingredients_ and \
               self.size_ == other.size_


class Margherita(Pizza):
    """Margherita pizza class"""

    def __init__(self, size: str = None) -> None:
        self.name_ = "Margherita🧀"
        self.size_ = size
        self.ingredients_ = {"tomato sauce": 75,
                             "mozzarella": 8,
                             "tomatoes": 10}
        super().__init__(self.ingredients_, self.size_, self.name_)


class Pepperoni(Pizza):
    """Pepperoni pizza class"""

    def __init__(self, size: str = None) -> None:
        self.name_ = "Pepperoni🍕"
        self.size_ = size
        self.ingredients_ = {"tomato sauce": 75,
                             "mozzarella": 8,
                             "pepperoni": 10}
        super().__init__(self.ingredients_, self.size_, self.name_)


class Hawaiian(Pizza):
    """Hawaiian pizza class"""

    def __init__(self, size: str = None) -> None:
        self.name_ = "Hawaiian🍍"
        self.size_ = size
        self.ingredients_ = {"tomato sauce": 75,
                             "mozzarella": 8,
                             "pineapples": 2,
                             "chicken": 1}
        super().__init__(self.ingredients_, self.size_, self.name_)
