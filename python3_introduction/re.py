import re

result = re.match('You', 'Young Frankenstein')

youpattern = re.compile('You')

result = youpattern.match('Young Frankenstein')