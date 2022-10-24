from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n, base):
    while n > 0 :
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertstring[n %base])
        n = n // base
        res = ""
        while not rStack.isEmpty():
            res = res + str(rStack.pop())
        return res

print(toStr(769,16))