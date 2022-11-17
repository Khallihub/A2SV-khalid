def Domino(a,b):
    c = a/2
    d = b/2
    if a%2==0:
        return c*b
    elif b%2==0:
        return d*a
    else:
        return a*(b-1)/2 + (a-1)/2
