import re
#* 0 or more
for x in re.finditer(r'n*','nn'):
    print(x)
#+ 1 or more
for x in re.finditer(r'n+','nn'):
    print(x)
#? 0 or 1 
for x in re.finditer(r'n?b','b'):
    print(x)
#{} exact number {4}
for x in re.finditer(r'r{3}','rrr'):
    print(x)
#{2,4} range of numbers
for x in re.finditer(r'r{2,4}','rr'):
    print(x)



