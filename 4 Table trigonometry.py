import math

def sines():
    print("Tables of sines")
    for x in range (0, 360, 45):
        a=format(math.sin(math.radians(x)),".2f")
        print('sin',x,'=',a,end=', ')


def cosines():
    print("\nTables of Cosines")
    for x in range (0, 360, 45):
        b=format(math.cos(math.radians(x)),".2f")
        print('cos',x,'=',b,end=', ')

def tan():
    print("\nTables of tan")
    for x in range (0, 360, 45):
        c=format(math.tan(math.radians(x)),".2f")
        print('tan',x,'=',c,end=', ')

        

def main():
    sines()
    cosines()
    tan()
    print()

if __name__=='__main__':
    main()
    
