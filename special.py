import re
#\d 0-9 
for x in re.finditer(r'\d+','0123456789') :
    print(x)
#\D any non-digit char
for x in re.finditer(r'\D+','01234aa'):
    print(x)
#\s any whitespace char space , \t,\n
for x in re.finditer(r'\s+','  aa\n'):
    print(x)

 

 