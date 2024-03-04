'''
Leet speak generator. 
Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. 
A própria palavra leet admite muitas variações, como l33t ou 1337. 
O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
Pesquise sobre as principais formas de traduzir as letras. 
Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
'''

from random import choice
from string import ascii_lowercase


def portugues_para_leet(palavra_ptbr: str) -> str:
    '''
    Converter palavra em portugues para leet speak,
    utilizando o discionário leet "https://www.gamehouse.com/blog/leet-speak-cheat-sheet/"
    '''

    palavra_leet: str = ''
    char_map: dict = {
        "a": ["4", "@", "/-\\", "^"],
        "b": ["I3", "8", "13", "|3"],
        "c": ["[", "{", "<", "("],
        "d": [")", "|)", "[)", "|>"],
        "e": ["3", "[-"],
        "f": ["|=", "ph", "|#", "/="],
        "g": ["&", "6", "(_+]", "9", "C-", "gee"],
        "h": ["#", "/-/", "[-]", "]-[", ")-(", "(-)", ":-:", "|-|", "}{"],
        "i": ["1", "[]", "!", "|", "eye", "3y3", "]["],
        "j": [",_|", "_|", "._|", "._]", ",_]", "]"],
        "k": [">|", "|<", "/<", "1<", "|c", "|(", "|{"],
        "l": ["1", "7", "|_", "|"],
        "m": ["/\\/\\", "/V\\", "JVI", "[V]", "[]V[]", "|\\/|", "^^"],
        "n": ["^/", "|\\|", "/\\/", "<\\>", "{\\}", "|V", "/V"],
        "o": ["0", "Q", "()", "oh", "[]"],
        "p": ["|*", "|o", "?", "|^", "[]D"],
        "q": ["(_,)", "()_", "2", "O_"],
        "r": ["12", "|`", "|~", "|?", "/2", "|^", "Iz", "|9"],
        "s": ["$", "5", "z", "ehs", "es"],
        "t": ["7", "+", "-|-", "']['", '"|"', "~|~"],
        "u": ["|_|", "(_)", "V", "L|"],
        "v": ["\\/", "|/", "\\|"],
        "w": ["\\/\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "\\X/"],
        "x": ["><", ">|<", "}{", "ecks"],
        "y": ["j", "`/"],
        "z": ["2", "7_", "-/_", "%", ">_", "~/_", "-|_"],
    }

    for letra in palavra_ptbr:
        if letra.lower() in ascii_lowercase:
            palavra_leet += choice(char_map[letra.lower()])
        else:
            palavra_leet += letra
    return palavra_leet


# ----- Leet speak generator ----- #
print('\n--- L33t SP34K ---')
palavra_br: str = input('Digite uma palavra: ')
print(f'\n{portugues_para_leet(palavra_br)}\n')
