# Write the missing line of code so that, when called, the function will return 1000 as the final result, not an UnboundLocalError exception.

var1 = 100

def var1_func():
    global var1 #dopisane global var1
    print(var1 * 10)
    var1 = 200

var1_func()