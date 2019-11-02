__author__ = 'ygzhang'

def bounds_of_rotations(x, c):
        n = len(x)
        Sum = []
        m = 0
        for m in range(n):
                S = 0.0
                i = 0
                for i in range(n):
                        if i+m < n:
                                S = S+x[i+m]*c**i
                        else:
                                S = S+x[i+m-n]*c**i
                        i =+ 1
                Sum.append(S)
                m =+ 1
        Max = max(Sum)
        Min = min(Sum)
        print((Min, Max))
