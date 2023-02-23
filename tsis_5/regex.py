import re
txt = open('receipt.txt')

#--------------------------------- 1
def matches_ab_b(txt):
    pattern = "^a(*b)&"
    x = re.findall(pattern, txt)
    return x
#--------------------------------- 2
def matches_abb_or_abbb(txt):
    pattern = "ab{2, 3}"
    x = re.findall(pattern, txt)
    return x
#--------------------------------- 3
def lowletters_joined_with_underscore(txt):
    pattern = "^[a-z]+_[a-z]+$"
    x = re.findall(pattern, txt)
    return x
#--------------------------------- 4
def upper_with_lows(txt):
    pattern = "[A-Z]+[a-z]+&)"
    x = re.findall(pattern, txt)
    return x
#--------------------------------- 5
def a_smth_b(txt):
    pattern = "^a.*?b&"
    x = re.findall(pattern, txt)
    return x
#--------------------------------- 6
def a_smth_b(txt):
    x = re.sub("[ .,]" ,":", txt)
    return x
#--------------------------------- 7
def snake_to_camel(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))
#--------------------------------- 8
def split_by_upper(txt):
    return re.findall("[A-Z][^A-Z]*", txt)
#--------------------------------- 9
def space_between_capital(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
#--------------------------------- 10
def camel_to_snake(txt):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',re.sub('([A-Z]+)', r' \1',txt.replace('-', ' '))).split()).lower()