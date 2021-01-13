import re

def finditer() :
    for match in re.compile(r'aa').finditer("aaaaccccaaacccaacccaccc") :
        print(match)
    #match.group() match.start(),match.end(),match.span()
    for match in re.finditer(r'aa',"aaacccaaccaacc") :
        print(match)

def findall():
    for match in re.findall(r'aa',"aaacccacccaacccaccc"):
        print(match)
    for match in re.compile(r'aa').findall('aaacccaaccaacc'):
        print(match)

def match() :
    print(re.match(r'aaa','aabbbbb'))
    print(re.compile(r'aa').match('aabbbbbbbb'))

