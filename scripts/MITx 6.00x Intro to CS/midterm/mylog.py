def myLog(x,b):
    if b>x:
        return 0
    else:
        exponent = 2
        while  b ** exponent <= x:
            exponent += 1
        if b ** exponent == x:
            return exponent
        else:
            return exponent -1

print(myLog(1,16))
