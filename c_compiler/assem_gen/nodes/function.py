class Function():
    def __init__(self, name, instructions: list):
        self.name = name
        self.instructions = instructions

    def __str__(self):
        return f"Func {self.name}({self.instructions})"
