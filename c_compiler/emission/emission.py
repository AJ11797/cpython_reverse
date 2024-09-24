import assem_gen.nodes
import assem_gen.nodes.instruction
import assem_gen.nodes.operand


def emit_operand(operand):
    if type(operand) is assem_gen.nodes.operand.Imm:
        return f"${operand.value}"
    elif type(operand) is assem_gen.nodes.operand.Register:
        return "%eax"


def emit_instructions(instructions):
    code = ""
    for instruction in instructions:
        code += "\t"
        if type(instruction) is assem_gen.nodes.instruction.Mov:
            code += f"movl {emit_operand(instruction.src)},{emit_operand(instruction.dst)}"
        elif type(instruction) is assem_gen.nodes.instruction.Ret:
            code += "ret"
        code += "\n"

    return code


def emit_func(func):
    code = f".globl {func.name}\n"
    code += f"{func.name}:\n"
    code += f"{emit_instructions(func.instructions)}"
    return code


def emit_program(assem_ast):
    code = emit_func(assem_ast.function)
    code += '\n.section .note.GNU-stack,"",@progbits'
    return code


def emit_assembly(assem_ast):
    assembly_code = emit_program(assem_ast) + "\n"

    return assembly_code
