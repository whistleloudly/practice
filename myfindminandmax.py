def findminandmax(L):
    s = len(L)
    if s != 0:
        Min = L[0]
        Max = L[0]
        for i in L:
            if i <= Min:
                Min = i
            if i >= Max:
                Max = i
            return (Min,Max)
    else:
        return (None,None)
