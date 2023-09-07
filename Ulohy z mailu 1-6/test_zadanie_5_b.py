#import time
#import datetime
#import date

uloha5="""
Uloha5:
- vstupom z klavecnice zadat nejaky datum a nasledne vypocitas kolko rokov, mesiacov, dni, hodin, minut a sekund preslo od daneho datumu (po aktualny datum)
"""
print(uloha5)


from datetime import date, datetime


year = int(input("Enter year: "))
#ValueError(year)
month = int(input("Enter month (1-12): "))
day = int(input("Enter day (1-31): "))
#hours = int(input("Enter hour (0-23): "))
#minutes = int(input("Enter minutes (0-59): "))
#seconds = int(input("Enter seconds (0-59): "))
dateInput = date(year, month, day)
print("Date provided is:", dateInput)

dateToday = date.today()

print("Current date is:", dateToday)

dateDifference = dateToday - dateInput
print("Seconds passed between dates:", dateDifference.total_seconds())
print("Minutes passed between dates:", dateDifference.total_seconds() / 60)
print("Hours passed between dates:", dateDifference.total_seconds() / (60*60))
print("Days passed between dates:", dateDifference.total_seconds() / (60*60*24))
print("Weeks passed between dates:", dateDifference.total_seconds() / (60*60*24*7))
print("Years passed between dates:", dateDifference.total_seconds() / (60*60*24*365))
#print("Days passed between dates:", dateDifference)
#print(dateDifference.total_seconds())
