class Statement():
    pass


class ReturnStatement(Statement):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"Return({self.expression})"
