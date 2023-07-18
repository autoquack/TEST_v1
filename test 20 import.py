#import colorama

#print(colorama.Fore.BLACK + colorama.Back.MAGENTA + "some text")

from colorama import Fore, Back

print(Fore.BLACK + Back.MAGENTA + "another text")


import datetime


from suntime import Sun, SunTimeException

lattitude = 55.55
longitude = 55.55

sun = SUN(lattitude,longitude)

today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
print ("today at something somewhere sun raised at {} and get down at {} UTC".format(today_sr.strftime('%H:%M'),today_ss.strftime('%H:%M')))