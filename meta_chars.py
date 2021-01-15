import re
# . ^ $ * + ? { } [ ] \ | ( )
s = ' abc'
# . any caracter except new line caracter
for x in re.finditer(r'.',s) :
    print(x)
# ^ start with "^comeco"
for x in re.finditer(r'^ a',s) :
    print(x)
# $ ends with "fim$"
for x in re.finditer(r'c$',s) :
    print(x)
# * zero or more occurrences "a*"
for x in re.finditer(r'd*',s) :
    print(x)
# + one or more occurrences "a+"
for x in re.finditer(r'a+b+c+',s) :
    print(x)
# { } Exactly the specified number of occurrences "al{2}"
for x in re.finditer(r'.{4}',s) :
    print(x)
# [] a set of caracteres "[a-m]" "[a-zA-c0-7]"
for x in re.finditer(r'[a-c]',s) :
    print(x)
# \ special sequence or caracter "\d"
for x in re.finditer(r'\.','.aa') :
    print(x) 
    # in special.py
# | Either or "a|b"
for x in re.finditer(r'a|b',s) :
    print(x)
# () capture and group 
for x in re.finditer(r'(a)',s) :
    print(x)


