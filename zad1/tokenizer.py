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
   'MODULO',
   'FACTORIAL',
   'SQRT',
)

# Regular expression rules for simple tokens
t_PLUS    = r'dodaj|dodać|plus|\+'
t_MINUS   = r'odejmij|odjąć|minus|\-'
t_TIMES   = r'razy|pomnóż\sprzez|x|pomnożone\sprzez'
t_DIVIDE  = r'podzielić\sprzez|/|podzielone\sprzez|dzielone\sprzez|slash|podzielone\sna'
t_LPAREN  = r'otwórz\snawias|nawias'
t_RPAREN  = r'zamknij\snawias'
t_SIN     = r'sinus'
t_COS     = r'cosinus'
t_RAISE_TO_POWER = r'do\spotęgi|potęga'
t_MODULO = r'modulo'
t_NUMBER = r'(\d+(\.\d+)?)|e|pi'
t_FACTORIAL = r'silnia'
t_SQRT = r'pierwiastek\sz|pierwiastek'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
