__author__ = 'springfield'
maxpalin=0

def turn_arrow(x):
    return int(str(x)[::-1])


for x1 in range(100,1000):
    for x2 in range(100,1000):
        x3=x1*x2
        if turn_arrow(x3)==x3 and x3>maxpalin:
            maxpalin= x3
print maxpalin