# -- Example for how to import and use in another program --
# 
# from ansi_color import ansi_color
# print(f'{ansi_color('RED')}Lorem ipsum {ansi_color('BLUE')}dolor sit amet{ansi_color('RESET')}')

def ansi_color(color: str):
    color = color.upper()
    ansi_color = {
        'RESET': '\33[0m',
        'BLACK_ON_WHITE': '\33[30;47m',
        'WHITE_ON_BLACK': '\33[37;40m',
        'BLACK': '\33[30m',
        'RED': '\33[31m',
        'GREEN': '\33[32m',
        'YELLOW': '\33[33m',
        'BLUE': '\33[34m',
        'MAGENTA': '\33[35m',
        'CYAN': '\33[36m',
        'WHITE': '\33[37m',
        'GRAY': '\33[40m',
        'BRIGHT_BLACK': '\33[40m',
        'BRIGHT_RED': '\33[41m',
        'BRIGHT_GREEN': '\33[42m',
        'BRIGHT_YELLOW': '\33[43m',
        'BRIGHT_BLUE': '\33[44m',
        'BRIGHT_MAGENTA': '\33[45m',
        'BRIGHT_CYAN': '\33[46m',
        'BRIGHT_WHITE': '\33[47m'
    }
    if color in ansi_color:
        return ansi_color[color]
    else:
        return f'\33[41;34m INVALID COLOR \33[0m'
