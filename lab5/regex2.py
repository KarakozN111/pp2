#with row txt

import re
txt = open('row.txt')
#ex 1
def match_pattern(txt):
    patt = "^a(*b)$"
    res = re.findall(patt, txt)
    return res
#ex2
def match_pattern(txt):
    patt = "ab{2, 3}"
    res = re.findall(patt, txt)
    return res
#ex3
def sequences(txt):
    patt = "^[a-z]+_[a-z]+$"
    res = re.findall(patt, txt)
    return res
#ex4
def match_pattern(txt):
    patt = "^[A-Z][a-z]+&"
    res = re.findall(patt, txt)
    return res
#ex5
def match_pattern(txt):
    patt = "^a.*?b&"
    res = re.findall(patt, txt)
    return res
#ex6
def colon(txt):
    x = re.sub("[ .,]" ,":", txt)
    return x
#ex 7
def snake_to_camel(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))
#ex8
def split_by_upper(txt):
    return re.findall("[A-Z][^A-Z]*", txt)
#ex9
def space_between_capital(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
#ex10
def camel_to_snake(txt):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',re.sub('([A-Z]+)', r' \1',txt.replace('-', ' '))).split()).lower()