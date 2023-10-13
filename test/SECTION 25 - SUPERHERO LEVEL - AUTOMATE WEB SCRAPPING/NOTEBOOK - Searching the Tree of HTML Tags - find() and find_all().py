Important! Please
note
that
your
results, such as the
number
of
h1
tags
on
the
test
web
page, may
differ
from the one in the
course
due
to
changes in the
structure
of
the
website
itself, which
are
not under
my
control.However, the
concepts and principles
stay
the
same.

# Searching the HTML tree
# The find() method - finds the first occurrence of a certain tag
# More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find
result.find("div")

# The find_all() method - finds the all occurrences of a certain tag (and other features, e.g. class name)
# More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
result.find_all("div")
result.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"})

# More info on searching: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree