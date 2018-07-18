from parsing.Token import Token
from parsing.TypeToken import TypeToken


class Interpreter:

    def __init__(self, text):
        self.text = text
        self.pointer = 0
        self.current_token = None
        #objeto que materializa os tipos de token suportados
        self.type_token = TypeToken()

    def get_current_token(self):
        if self.pointer > len(self.text) - 1:
            return Token(self.type_token.EOF, None)
        else:
            current_char = self.text[self.pointer]
            if current_char.isdigit() or current_char.isalpha():
                token = Token(self.type_token.VAR, current_char)
                return token
            elif current_char == '+':
                token = Token(self.type_token.PLUS, current_char)
                return token
            elif current_char == '(':
                token = Token(self.type_token.O_PAR, current_char)
                return token
            elif current_char == ')':
                token = Token(self.type_token.C_PAR, current_char)
                return token
            elif current_char == '*':
                token = Token(self.type_token.FECHO, current_char)
                return token
            else:
                self.error()

    def eat(self, token_type):
        for tp in token_type:
            if tp == self.get_current_token().type:
                self.pointer += 1
                return True
        return False

    def symbol(self):
        log = self.eat([self.type_token.VAR])
        if not log:
            self.error('symbol')

    def factor(self):
        temp = self.get_current_token().type
        if temp == self.type_token.VAR:
            self.symbol()
            if self.get_current_token().type == self.type_token.FECHO:
                self.eat([self.type_token.FECHO])

        elif temp == self.type_token.O_PAR:
            ax = self.eat([self.type_token.O_PAR])
            self.expr()
            ay = self.eat([self.type_token.C_PAR])
            if not (ax and ay) : self.error()
            if self.get_current_token().type == self.type_token.FECHO:
                self.eat([self.type_token.FECHO])
        else:
            self.error('factor')


    def term(self):
        self.factor()
        temp = self.get_current_token().type
        while( (temp == self.type_token.VAR) or
               (temp == self.type_token.O_PAR) ):
            self.factor()
            temp = self.get_current_token().type


    def expr(self):
        self.term()
        while self.eat([self.type_token.PLUS]):
            self.term()

    def build(self):
        self.expr()
        if not (self.pointer > len(self.text) - 1):
            self.error('build')

    def error(self,str):
        raise Exception('Error parsing in {a} at part of {b}'.format(a = self.get_current_token() , b = str) )