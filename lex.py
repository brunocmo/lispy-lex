import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    tokens = {
        'QUOTE': r'\'',
        'STRING': r'\".*\"',
        'LPAR': r'\(',
        'RPAR': r'\)',
        'NUMBER': r'[+|-]?\d+(?:\.\d+)?',
        'NAME': r'([a-zA-Z_%\+\-]|\.\.\.)[a-zA-Z_0-9\-\>\?\!]*',
        'CHAR': r'#\\[a-zA-Z]*',
        'BOOL':  r'#[t|f]',
    }

    token = ''
    
    code = re.sub(r';;.*', "", code)

    for key, value in tokens.items():   

        if re.match('n+', key):
            token += f'(?:{value})|'
        else:
            token += f'(?P<{key}>{value})|'

    token = re.compile(token)

    lexfinal = [ ]

    for each in token.finditer(code):

        if each.lastgroup != None:
            lexfinal.append(Token(each.lastgroup, each.group()))

    return lexfinal