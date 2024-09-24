import parser.nodes.identifier as node_identifier
import parser.nodes.statement as node_statement
import parser.nodes.expression as node_expression
import parser.nodes.function as node_function
import parser.nodes.program as node_program


def expect(expected, tokens):
    if tokens[0] != expected:
        raise Exception(f"Token error - got {tokens[0]}, expected {expected}")
    del tokens[0]


def parse_identifier(tokens):
    identifier_name = tokens[0]
    del tokens[0]
    return node_identifier.Identifier(identifier_name)


def parse_exp(tokens):
    expression_value = tokens[0]
    del tokens[0]
    return node_expression.Constant(expression_value)


def parse_statement(tokens):
    expect("return", tokens)
    return_value = parse_exp(tokens)
    expect(";", tokens)
    return node_statement.ReturnStatement(return_value)


def parse_function(tokens):
    expect("int", tokens)
    id = parse_identifier(tokens)
    expect("(", tokens)
    expect("void", tokens)
    expect(")", tokens)
    expect("{", tokens)
    body = parse_statement(tokens)
    expect("}", tokens)
    return node_function.Function(id, body)


def parse_program(tokens):
    function = parse_function(tokens)
    return node_program.Program(function)


def run_parser(tokens: list):
    AST = parse_program(tokens)
    if tokens != []:
        raise Exception("Invalid identifier after function")
    return AST
