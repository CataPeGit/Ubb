def min(a):
    minim = 99999999999
    for i in a:
        if minim > a[i]:
            minim = a[i]
    return minim

def maxi(a):
    maxi = -9999999999
    for i in a:
        if maxi < a[i]:
            maxi = a[i]
    return maxi

def fib(a):
    if a < 0:
        print('wrong input')
        
    elif a == 0:
        return 0
    elif a == 1 or a == 2:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)

def fun(n):
    i = 0
    s = 0
    while i <= n:
        i += 1
        aux = i
        while aux > 0:
            s = s + i
            aux -= 1
    return s


def function(l):
    s = 0 
    num = 1 # we start from 0
    k = 0
    while l > 0: # we will go trough all the items in the sequence (lenght = l)
        l -= 1
        s += num 
        k += 1 
        if k == num: # we check if we added variable 'num' k times
            num += 1 
            k = 0
    return s

def s(a,b):
    print(a,b)
s(a="mar",23)
