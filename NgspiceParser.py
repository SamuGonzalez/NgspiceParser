import sys
from antlr4 import *
from gen.NgspiceGrammarLexer import NgspiceGrammarLexer
from gen.NgspiceGrammarParser import NgspiceGrammarParser


def NgspiceParser(argv):
    input_file = FileStream(argv[1])
    lexer = NgspiceGrammarLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = NgspiceGrammarParser(stream)
    tree = parser.code()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    NgspiceParser(sys.argv)
