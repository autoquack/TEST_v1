#Consider the following string.

#regex_str = "123.456.789   0 PYTHON 3"

#Use a regular expressions specific method to replace any word-character ( a-z, A-Z, 0-9, _ ) with the percent sign ( % ) throughout the entire string. Note that whitespaces should not be modified in any way.
### zadanie ulohy:
#import re

#regex_str = "123.456.789   0 PYTHON 3"

#regex =

#print(regex)
###

import re

regex_str = "123.456.789   0 PYTHON 3"

#regex = re.sub("[a-zA-Z]" + "[0-9]", "%", regex_str)
regex = re.sub("\w", "%", regex_str)

print(regex)