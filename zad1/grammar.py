import ply.yacc as yacc

from tokenizer import tokens

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = str(p[1]) + ' + ' + str(p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = str(p[1]) +  ' - ' + str(p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES func'
    p[0] = str(p[1]) + ' * ' + str(p[3])

def p_term_div(p):
    'term : term DIVIDE func'
    p[0] = str(p[1]) + ' / ' + str(p[3])

def p_term_func(p):
    'term : func'
    p[0] = p[1]

def p_func_sin(p):
    'func : SIN factor'
    p[0] = 'sin(' + str(p[2]) + ')'

def p_func_cos(p):
    'func : COS factor'
    p[0] = 'cos(' + str(p[2]) + ')'

def p_func_factor(p):
    'func : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = str(p[1])

def p_factor_minus_unary(p):
    'factor : MINUS factor'
    p[0] = '-' + str(p[2])

def p_factor_plus_unary(p):
    'factor : PLUS factor'
    p[0] = '+' + str(p[2])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = '( ' + str(p[2]) + ' )'

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def parse(expression):
    result = parser.parse(expression)
    print(result)
    return result
