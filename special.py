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
#\S any non-whitespace char 
for x in re.finditer(r'\S+',' aa\n'):
    print(x)
#\w any alphanumeric char a-z A-Z 0-9 and _ 
for  x in re.finditer(r'\w+','aa9B_  '):
    print(x)
#\W any non-alphanumeric char 
for x in re.finditer(r'\W','aa98_ ') :
    print(x) 
#\b use for end or start of any word 
for x in re.finditer(r'\baa','aakkkk aaw'):
    print(x)  
#\B use for non end or start of any word
for x in re.finditer(r'\Btt','cccc'):
    print(x)



 

 