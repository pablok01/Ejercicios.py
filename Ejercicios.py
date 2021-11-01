import ply.lex as lex
import sys
from ply.lex import Lexer
reserved={
    'print':'PRINT',
}



tokens = list(reserved.values()) +[
    #Expresiones aritmeticas
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'MODULO',
    #OPERADORES CONDICIONALES
    'MAYOR',
    'MENOR',
    'IGUAL',
    'MAYOROIGUAL',
    'MENOROIGUAL',
    'DIFERENTE',
    #variables validas
    'VARIABLE',
    #enteros y decimales
    'NUMEROS',
    #cadenas de caracteres
    'CADENAS',
    'comentarios',
    'ID'
]
def t_VARIABLE(t):
    r'[a-zA-Z]([\w])*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        return t
def t_NUMEROS(t):
    r'\d+\.?\d*'
    t.value = float(t.value)
    return t
def t_ID(t):
    r'[a-zA-Z_][\w]*'
    if t.value in reserved:
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        t_error(t)
#expresiones aritmeticas
t_SUMA=r'\+'
t_RESTA=r'\-'
t_MULTIPLICACION=r'\*'
t_DIVISION=r'/'
t_MODULO=r'\%'
#operadores condicionales
t_MAYOR=r'>'
t_MENOR=r'<'
t_IGUAL='='
def t_MAYOROIGUAL(t):
    r'>='
    return t
def t_MENOROIGUAL(t):
    r'<='
    return t
def t_DIFERENTE(t):
    r'!>'
    return t

def t_CADENAS(t):
    r'\"(.)*?\"'
    return t
def t_comentarios(t):
    r'\#(.)*?\n+'
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'
#error, prueba y lectura
def t_error(t):
    print("Lexical error: " + str(t.value))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    i = 1  # Representa la línea
    while True:
        tok = lexer.token()
        if not tok:
            break
        import texttable

        tableObj = texttable.Texttable()

        tableObj.set_cols_align(["l", "r", "c", "v"])

        #tableObj.set_cols_dtype(["a", "i", "t", "g"])

        tableObj.set_cols_valign(["t", "m", "b", "r"])

        tableObj.add_rows([
            ["LINEA DE CODIGO","LINEA","TOKEN","PARTE DE CODIGO"],
            [str(i),str(tok.lineno),str(tok.type),str(tok.value)]

        ])

        print(tableObj.draw())
        #print("\t" + str(i) + " - " + "Line: " + str(tok.lineno) + "\t" + str(tok.type) + "\t-->  " + str(tok.value))
        i += 1
    # print(tok)


lexer: Lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'prueba.txt'
    f = open(fin, 'r')
    data = f.read()
    # print (data)
    # lexer.input(data)
    test(data, lexer)
# input()