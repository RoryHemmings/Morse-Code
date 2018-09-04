import sys
import os
import datetime

helpMenu = "\n\nFLAGS:\n\t-s <PATH> - saves to Path\n\t-m <MESSAGE> - uses command line version with message\n\t-r - reverses input\n\t-h - displays this message\n\n"

_SAVE = False
_PATH = ""

_CLV = False
_MESSAGE = ""

_REVERSE = False

DOT = "0"
DASH = "1"

chart = {
    'a': DOT + DASH,
    'b': DASH + DOT + DOT + DOT,
    'c': DASH + DOT + DASH + DOT,
    'd': DASH + DOT + DOT,
    'e': DOT,
    'f': DOT + DOT + DASH + DOT,
    'g': DASH + DASH + DOT,
    'h': DOT + DOT + DOT + DOT,
    'i': DOT + DOT,
    'j': DOT + DASH + DASH + DASH,
    'k': DASH + DOT + DASH,
    'l': DOT + DASH + DOT + DOT,
    'm': DASH + DASH,
    'n': DASH + DOT,
    'o': DASH + DASH + DASH,
    'p': DOT + DASH + DASH + DOT,
    'q': DASH + DASH + DOT + DASH,
    'r': DOT + DASH + DOT,
    's': DOT + DOT + DOT,
    't': DASH,
    'u': DOT + DOT + DASH,
    'v': DOT + DOT + DOT + DASH,
    'w': DOT + DASH + DASH,
    'x': DASH + DOT + DOT + DASH,
    'y': DASH + DOT + DASH + DASH,
    'z': DASH + DASH + DOT + DOT,
    ' ': '2'
}

backwards = {chart[k]: k for k in chart}


def convert(message):
    words = []
    for s in message:
        if s == ' ':
            words.append('2')
        else:
            words.append(chart[s.lower()])

    words = refine(words)
    return words


def reverse(message):
    words = ''
    temp = ''
    for s in message:
        if not s == ' ':
            temp += s
        elif s == ' ':
            if len(temp) > 0:
                words += backwards[encode(temp)]
                temp = ''
        elif s == '/':
            words += ' '

    words += backwards[encode(temp)]
    return words


def encode(let):
    ret = ''
    for s in let:
        if s == '.':
            ret += DOT
        elif s == '-':
            ret += DASH
        else:
            ret += '2'

    return ret


def refine(s):
    ret = ""
    for letter in s:
        for n in letter:
            if n == DOT:
                ret += '.'
            elif n == DASH:
                ret += '-'
            else:
                ret += ' / '
        ret += ' '
    return ret


def save(s):
    global _PATH
    if not '.' in _PATH:
        filename = datetime.time()
    else:
        filename = "File"
    f = open(_PATH, 'w')
    f.write(s)
    f.close()
    print('{} succesfully saved'.format(filename))
    

def checkArgs(args):
    global _SAVE
    global _PATH
    global _CLV
    global _MESSAGE
    global _REVERSE
    for i in range(len(args)):
        if args[i] == '-h':
            print(helpMenu)
            exit()

        if args[i] == '-m':
            _CLV = True
            i += 1
            _MESSAGE = args[i]

        if args[i] == '-r':
            _REVERSE = True

        if args[i] == '-s':
            _SAVE = True
            i += 1
            if i >= len(args) or args[i][0] == '-':
                _PATH = os.getcwd()
            else:
                _PATH = args[i]


def main(args):
    global _MESSAGE
    global _SAVE
    global _CLV
    global _REVERSE
    checkArgs(args)
    if not _CLV:
        message = input("Enter Message: ")
        message = convert(message) if not _REVERSE else reverse(message)
        if _SAVE and not _REVERSE:
            save(message)
        else:
            print(message)

    else:
        message = _MESSAGE
        message = message = convert(message) if not _REVERSE else reverse(message)
        if _SAVE and not _REVERSE:
            save(message)
        else:
            print(message)


if __name__ == '__main__':
    main(sys.argv)
    #print(reverse('.... ..  /  .-. --- .-. -.-- .... ..  /  .-. --- .-. -.--'))
