#Write a function on line 10, in between the parentheses of the print() function, that checks if portsno is an attribute of router1 or not. Of course, this is False.
### zadanie:
#class MyRouter(object):
#    def __init__(self, routername, model, serialno, ios):
#        self.routername = routername
#        self.model = model
#        self.serialno = serialno
#        self.ios = ios

#router1 = MyRouter('R1', '2600', '123456', '12.4')

#print()
###
class MyRouter(object):
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

router1 = MyRouter('R1', '2600', '123456', '12.4')

print(hasattr(router1, "portsno"))