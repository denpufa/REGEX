import re
# . ^ $ * + ? { } [ ] \ | ( )

s = ' abc\n'
# . any caracter except new line caracter
for x in re.finditer(r'.',s) :
    print(x)
# ^ start with "^comeco"
for x in re.finditer(r'^ a',s) :
    print(x)

# $ ends with "fim$"
# * zero or more occurrences "a*"
# + one or more occurrences "a+"
# { } Exactly the specified number of occurrences "al{2}"
# [] a set of caracteres "[a-m]"
# \ special sequence or caracter "\d"
# | Either or "a|b"
# () capture and group 

