import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'SIN',
   'COS',
   'RAISE_TO_POWER',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+|dodaj|dodać|plus'
t_MINUS   = r'-|odejmij|odjąć|minus'
t_TIMES   = r'x|\*|razy|pomnóż\sprzez'
t_DIVIDE  = r'/|podzielić\sprzez|podzielone\sprzez'
t_LPAREN  = r'otwórz\snawias'
t_RPAREN  = r'zamknij\snawias'
t_SIN     = r'sinus'
t_COS     = r'cosinus'
t_RAISE_TO_POWER = r'do\spotęgi'
t_NUMBER = r'(\d+(\.\d+)?)|e|pi'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
