import re

my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5'


a = re.match(r"255", my_regex_str)
type(a)

print("test a", a)
#######################

b = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
b.group(0)

print("test b", b)
print("test b2", b.group(0))
######################

c = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
c.group(1)

print("test c", c)
print("test c2", c.group(1))