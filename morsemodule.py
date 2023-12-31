engdict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..','0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "\\": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}
rusdict = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
    'Е': '.', 'Ё': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
    'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
    'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
    'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
    'Ю': '..--', 'Я': '.-.-',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "\\": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}
def ltext(text):
    return ' '.join([engdict[l] for l in text.upper() if l in engdict])
def ktext(text):
    return ' '.join([rusdict[l] for l in text.upper() if l in rusdict])
def lmorse(text):
    res = []
    for l in text.split(' '):
            for key, value in engdict.items():
                if value == l:
                    res.append(key)
    return ''.join(res).strip()
def kmorse(text):
    res = []
    for l in text.split(' '):
            for key, value in rusdict.items():
                if value == l:
                    if key != 'Ё':
                        res.append(key)
                    else:
                        pass
    return ''.join(res).strip()
