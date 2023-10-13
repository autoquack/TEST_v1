# Extracting webpage elements by tag

# Extracting the head - creates a Tag object
# Will return only the first tag by that name
head = result.head
>> > type(head)
<

class 'bs4.element.Tag'>

# Extracting h2 heading - creates a Tag object
# Will return only the first tag by that name


h2 = result.h2
>> > type(h2)
<

class 'bs4.element.Tag'>

# Extracting the title - creates a Tag object
# Will return only the first tag by that name


title = result.title
>> > type(title)
<

class 'bs4.element.Tag'>

# Accessing the name of a tag

>> > head.name
'head'
>> > h2.name
'h2'
>> > title.name
'title'

# Setting a new name for a tag
>> > title.name = "mytitle"
>> > title
< mytitle > Top
items < / mytitle >
# This change is reflected in the BeautifulSoup object itself

# A tag may have any number of attributes. Example:
# <header role="banner" class="navbar navbar-fixed-top navbar-static">
# The header tag has two attributes:
# attribute: role, value: "banner"
# attribute: class, value: "navbar navbar-fixed-top navbar-static"

# Using the attrs object attribute you can view the tag's own attributes
# as a dictionary with the attribute name as the key and attribute value(s) as the value
# Here, the 'role' attribute is a single-valued attribute
# and the 'class' attribute is a multi-valued attribute
# Note: for multi-valued attributes you get a list of the attribute's values as the dictionary value
>> > header = result.header
>> > print(header.prettify())  # pretty printing HTML code
>> > header.attrs
{'role': 'banner', 'class': ['navbar', 'navbar-fixed-top', 'navbar-static']}

# Accessing the value of a tag's attribute (as with any other dictionary)
>> > header['role']
'banner'
>> > header['class']
['navbar', 'navbar-fixed-top', 'navbar-static']

# or, using the get() method:
>> > header.get('role')
'banner'
>> > header.get('class')
['navbar', 'navbar-fixed-top', 'navbar-static']

# Modifying a tag's attribute value
>> > header['role'] = "something"
>> > header.attrs
{'role': 'something', 'class': ['navbar', 'navbar-fixed-top', 'navbar-static']}

# Adding a new tag attribute
>> > header['new'] = "python"
>> > header.attrs
{'role': 'something', 'class': ['navbar', 'navbar-fixed-top', 'navbar-static'], 'new': 'python'}

# Removing a tag attribute
>> > del header['new']
>> > header.attrs
{'role': 'something', 'class': ['navbar', 'navbar-fixed-top', 'navbar-static']}

# Extracting the string from a tag
>> > h2 = result.h2
>> > h2
< h2 > Top
items
being
scraped
right
now < / h2 >
>> > h2.string
'Top items being scraped right now'
>> > type(h2.string)
<

class 'bs4.element.NavigableString'>
# this is called a NavigableString
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigablestring

# Zooming in to a certain area of the HTML tree
# Using a tag name as an attribute will give you only the first tag by that name
# More info: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree


result.header.div
result.header.div.div.a
result.header.div.div.a.button