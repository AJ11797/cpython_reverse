import assem_gen.nodes.function as ass_function
import assem_gen.nodes.program as ass_program
import assem_gen.nodes.instruction as ass_instruct
import assem_gen.nodes.operand as ass_operand
import parser.nodes


def gen_expression(exp):
    return ass_operand.Imm(exp.value)


def gen_instructions(func_body):
    instructions = []

    if type(func_body) is parser.nodes.statement.ReturnStatement:     
        expression = gen_expression(func_body.expression)
        instructions.append(ass_instruct.Mov(src=expression, dst=ass_operand.Register()))
        instructions.append(ass_instruct.Ret())

    return instructions


def gen_function(func):
    instructions = gen_instructions(func.body)
    return ass_function.Function(name=func.name, instructions=instructions)


def gen_program(AST):
    function = gen_function(AST.function)
    return ass_program.Program(function)


def generate_assembly(AST):
    return gen_program(AST)
