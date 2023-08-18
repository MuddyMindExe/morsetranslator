# Task of the module
Translates Latin and Cyrillic text into Morse code and vice versa.
If you try to tanslate from morse code to text you will always get you text in upper case, beacuse morse code does not have the different codes for lower and upper case letters.
If you want to translate only numbers or special symbols you may use all this functions, because dictionaries, that contain all the letters have all the special symbols.
# Functions
```py
def ltext(text):
#This function translates Latin text into a morse code
```
```py
def ktext(text):
#This function translates Cyrillic text into a morse code
```
```py
def lcode(text):
#This function translates morse code into a Latin text
```
```py
def kcode(text):
#This function translates morse code into a Cyrillic text
```
### Examples
**ltext**
```py
def ltext(text):
    return ' '.join([engdict[l] for l in text.upper() if l in engdict])
txt = 'Try to convert'
print(ltext(txt))
```
Result:
```py
- .-. -.--  - ---  -.-. --- -. ...- . .-. -
```
**ktext**
```py
def ktext(text):
    return ' '.join([rusdict[l] for l in text.upper() if l in rusdict])
txt = 'Попытка перевода'
print(ktext(txt))
```
Result:
```py
.--. --- .--. -.-- - -.- .-  .--. . .-. . .-- --- -.. .-
```
**lmorse**
```py
def lmorse(text):
    res = []
    for l in text.split(' '):
            for key, value in engdict.items():
                if value == l:
                    res.append(key)
    return ''.join(res).strip()
txt = ''
print(ktext(txt))
```
Result:
```py
TRY TO CONVERT
```
**kmorse**
```py
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
txt = '.--. --- .--. -.-- - -.- .-  .--. . .-. . .-- --- -.. .-'
print(kmorse(txt))
```
Result:
```py
ПОПЫТКА ПЕРЕВОДА
```
