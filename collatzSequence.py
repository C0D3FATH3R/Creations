# Developed By C0D3FATH3R
def collatz(number) : # With print statement
    if number % 2 == 0 : # For Even Numbers
        i = number // 2
        print (i)
        return i
    elif number % 2 == 1 : # For Odd Numbers
        i = (number*3)+1
        print (i)
        return i

def collatzf(number) : #Without print statement
    if number % 2 == 0 : # For Even Numbers
        i = number // 2
        return i
    elif number % 2 == 1 : # For Odd Numbers
        i = (number*3)+1
        return i

def doit (i):
    while True :
        if collatzf(i) == 1 :
            print(collatzf(i))
            break
        else :
            n = collatz(i)
            return doit(n)
            print (n)
try :
    doit(int(input()))
except ValueError :
    print("Invalid argument : No strings")
