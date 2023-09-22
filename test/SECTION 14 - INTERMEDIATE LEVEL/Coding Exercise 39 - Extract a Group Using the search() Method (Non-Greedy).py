#Consider the following string.
#regex_str = "123.456.789   0 PYTHON 3"
#Write a regular expression pattern in between the parentheses so that regex.group(1) will match and return the '123.456.789' substring (with no Space characters).

###zakladny stav ulohy:
#import re

#regex_str = "123.456.789   0 PYTHON 3"

#regex = re.search(r"()\s{2,}", regex_str)

#print(regex.group(1))
###
import re

regex_str = "123.456.789   0 PYTHON 3"

regex = re.search(r"(.+?)\s{2,}", regex_str)

print(regex.group(1))
