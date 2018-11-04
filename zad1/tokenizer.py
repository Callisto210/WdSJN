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
)

# Regular expression rules for simple tokens
t_PLUS    = r'dodaj|dodać|plus'
t_MINUS   = r'odejmij|odjąć|minus'
t_TIMES   = r'razy|pomnóż\sprzez'
t_DIVIDE  = r'podzielić\sprzez'
t_LPAREN  = r'otwórz\snawias'
t_RPAREN  = r'zamknij\snawias'
t_SIN     = r'sinus'
t_COS     = r'cosinus'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
##
##^^^^Tutaj trzeba będzie zrobic rozpoznawanie liczb
##

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

##Q&D aka Quick and Dirty test
#data = '''3 dodać 5 podzielić przez otwórz nawias 4 razy 3 zamknij nawias pomnóż przez 9 minus 8'''
#lexer.input(data)

#while True:
#    tok = lexer.token()
#    if not tok:
#        break
#    print(tok)
