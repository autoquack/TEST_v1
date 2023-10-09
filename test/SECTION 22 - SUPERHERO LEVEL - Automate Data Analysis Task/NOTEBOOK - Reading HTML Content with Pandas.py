Reading HTML Content from URLs and HTML Files with Pandas



#Installing the lxml module, which is necessary for reading HTML content with Pandas; otherwise, Python throws an ImportError exception

pip install lxml
import lxml


#Reading HTML content from an URL

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
d = pandas.read_html(url)


#If there are multiple tables on the page, you can select which one to load/read by using indexes

d = pandas.read_html(url)[0]
d = pandas.read_html(url)[1]


#Reading HTML content from an .html file stored locally

d = pandas.read_html("D:\\sample_data\\Python (programming language) - Wikipedia.html")



More information:

https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#html