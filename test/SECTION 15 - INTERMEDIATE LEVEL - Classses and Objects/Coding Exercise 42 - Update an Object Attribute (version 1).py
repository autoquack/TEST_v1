#Write code on line 10 that will update the serial number of this device to 2019ABC2020, without using a function.
### zadanie:
#class MyRouter(object):
#    def __init__(self, routername, model, serialno, ios):
#        self.routername = routername
#        self.model = model
#        self.serialno = serialno
#        self.ios = ios

#router1 = MyRouter('R1', '2600', '123456', '12.4')



#print(router1.serialno)
###
class MyRouter(object):
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

router1 = MyRouter('R1', '2600', '123456', '12.4')

#setattr(router1, "serialno", "2019ABC2020") # riesenie specialnou funkciou
router1.serialno = "2019ABC2020" # simple riesenie

print(router1.serialno)
