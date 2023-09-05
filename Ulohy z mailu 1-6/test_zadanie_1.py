uloha1 = """
Uloha1:
- generovanie random cisla (integer, float), random textoveho retazca, random stringu(ktory bude obsahovat aj specialne znaky)
   > na tuto ulohu si najdi kniznicu na nete a nauc sa ju pouzivat
- vygenerovanie/vypisanie aktualneho datumu a casu 
"""
print(uloha1)
import secrets
import string
import random
import datetime
# cisla v1
r_number = random.randint(0, 10)
print(r_number)
# cisla v2
r_number2 = "".join(secrets.choice(string.digits) for a in range(1))
print(r_number2)
# pismmena v1
r_text_length = random.randint(1, 10)
r_text = "".join(secrets.choice(string.ascii_letters) for b in range(r_text_length))
print(r_text)
# pismena v2
r_text2 = "".join(secrets.choice(string.ascii_letters) for c in range(0, 10))
print(r_text2)
# vsetko dokopy
r_string = "".join(secrets.choice(string.digits + string.ascii_letters + string.punctuation) for d in range(0, 10))
print(r_string)
# cas
#time = time.localtime()
#c_time = time.strftime("%H:%M:%S", t)
#time = time.localtime()
#c_time = time.tm_sec
#print(c_time)
time = datetime.datetime.now()
print(time)

