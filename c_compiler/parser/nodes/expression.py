import sys


class Expression():
    pass


class Constant(Expression):
    def __init__(self, value):
        try:
            self.value = int(value)
        except ValueError:
            print("Constant must be a number")
            sys.exit(1)

    def __str__(self):
        return f"Constant({self.value})"
