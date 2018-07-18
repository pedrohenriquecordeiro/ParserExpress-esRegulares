from parsing.Interpreter import Interpreter
from machina.machina5 import machina5
from machina.machina3 import machina3
from machina.machina1 import machina1
from parse_json.Translator import translator
from AF.afnLambda import afnL
from AF.afd import afd

def main():

    er = input("Digite a ER ->")
    er = er.strip()
    er = er.lower()

    interpreter = Interpreter(er)
    interpreter.build()

    print(translator(er))

    #print(afn(er))
    #print(translator(er))

if (__name__ == "__main__"):
    # se eu sou o principal eu run
    # se eu for chamado por um outro arquivo eu não sou principal entao eu nao dou run
    main()