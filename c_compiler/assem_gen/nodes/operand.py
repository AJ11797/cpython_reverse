class Operand():
    pass


class Imm(Operand):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Imm({self.value})"


class Register(Operand):
    def __repr__(self):
        return "Register"
