import re


def read_file(filename: str) -> str:
    with open(filename) as file:
        return re.sub("\n", " ", file.read())


def run_lexer(filename: str) -> list:
    program = read_file(filename)

    tokens = []
    while program != "":
        while program[0] == " ":
            program = program.strip()

        if match := re.search("^[a-zA-Z_]\\w*\\b", program):  # Identifier Found
            # if re.search("int\\b")

            tokens.append(match.group())
            program = program[match.span()[1]:]
        elif match := re.search("^[0-9]+\\b", program):  # Constant Found
            tokens.append(match.group())
            program = program[match.span()[1]:]
        elif match := re.search("^\\(", program):  # Open bracket
            tokens.append(match.group())
            program = program[1:]
        elif match := re.search("^\\)", program):  # Close bracket
            tokens.append(match.group())
            program = program[1:]
        elif match := re.search("^{", program):
            tokens.append(match.group())
            program = program[1:]
        elif match := re.search("^}", program):
            tokens.append(match.group())
            program = program[1:]
        elif match := re.search("^;", program):
            tokens.append(match.group())
            program = program[1:]
        else:
            raise Exception("Lexer Error")

    return tokens
