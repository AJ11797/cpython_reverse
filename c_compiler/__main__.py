#!/usr/bin/env python3

import subprocess
import argparse
import sys
import lexer.lexer as lexer
import parser.parser as parser
import assem_gen.assembly_generator as assembly_generator
import emission.emission as emission


def parse_args() -> dict:
    argparser = argparse.ArgumentParser()
    argparser.add_argument('filename')
    argparser.add_argument('--lex', help='flag to stop after lexing',
                           action='store_true')
    argparser.add_argument('--parse', help='flag to stop after parsing',
                           action='store_true')
    argparser.add_argument('--codegen', help='flag to stop after codegen',
                           action='store_true')
    args = argparser.parse_args()

    arguments = {'filename': args.filename[:-2],
                 'lex_flag': args.lex,
                 'parse_flag': args.parse,
                 'codegen_flag': args.codegen}
    return arguments


def preprocess(filename: str):
    """Preprocess a .c file to a .i file"""
    subprocess.run(["gcc", "-E", "-P", f"{filename}.c", "-o", f"{filename}.i"])


def write_assembly(filename: str, assembly: str):
    """Writes the generated assembly code to a file"""
    with open(f"{filename}.s", "w") as file:
        file.write(assembly)


def assemble(filename: str):
    """Calls a linker on the produced assembly file"""
    subprocess.run(["gcc", f"{filename}.s", "-o", f"{filename}"])


if __name__ == "__main__":
    arguments = parse_args()

    preprocess(arguments["filename"])
    tokens = lexer.run_lexer(f"{arguments["filename"]}.i")
    print(tokens)

    if arguments["lex_flag"]:
        sys.exit(0)

    AST = parser.run_parser(tokens)
    print(AST)

    if arguments["parse_flag"]:
        sys.exit(0)

    assembly = assembly_generator.generate_assembly(AST)
    print(assembly)

    if arguments["codegen_flag"]:
        sys.exit(0)

    assembly_code = emission.emit_assembly(assembly)
    print(assembly_code)

    write_assembly(arguments["filename"], assembly_code)
    assemble(arguments["filename"])
