from assem_gen.nodes.operand import Operand


class Instruction():
    pass


class Mov(Instruction):
    def __init__(self, src: Operand, dst: Operand):
        self.src = src
        self.dst = dst

    def __repr__(self):
        return f"Mov({self.src}->{self.dst})"


class Ret(Instruction):
    def __repr__(self):
        return "Ret"
