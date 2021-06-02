import re

def get_leading_whitespace(string):
    start,end = re.match('^(\s*)',string)
    return string[start:end]
