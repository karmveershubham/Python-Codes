import math

def quadritic(a,b,c):
    
    """to calculate the roots of the quadritic equation using sridhracharya's formula and to print the results."""

    disc= (math.pow(b,2)-4*a*c)
    #if discriminant of equation is zero than we get a negative no. in underoot hence there will be no real roots.
    if disc<0:
        x1=(-b)/(2*a)
        x2=(-b)/(2*a)
        print("roots of the given quadritic equation are imaginary") 
        print('x1= ',x1,'+', 'i'*(math.sqrt(-1*disc)))
        print('x1= ',x1,'+', 'i'*(math.sqrt(-1*disc))) 

    elif disc == 0:
        x1=(-b+math.sqrt(disc))/(2*a)
        x2=(-b-math.sqrt(disc))/(2*a)

        print("roots of the given quadritic equation are equal")
        print('x1= ',x1)
        print ('x2= ',x2)
    else:
        x1=(-b+math.sqrt(disc))/(2*a)
        x2=(-b-math.sqrt(disc))/(2*a)

        print("roots of the given quadritic equation are")
        print('x1= ',x1)
        print ('x2= ',x2) 
            
              
def main():
    """to take the desired quadritic equation from the user as input by giving some necessary instructions."""

    print("if  the general quadrtic equation is written in the form")
    print("(a)x^2+(b)x+c ,where a can not be 0")
    print("then with respect to above")
    print()
    cont='y'
    #to continue till the user want.
    while cont.lower()=='y':
        a=float(input("enter the value of  the coefficiant of x^2 as a= "))
        b=float(input("enter the value of the coefficiant of x as b= "))
        c=float(input("enter the value of a constant as c= "))
        print()

    #to represent the equation entered by the user.
        print("the equation entered by you is = ",'(',a,')x^2+(',b,')x+',c)
        ans=input("enter 'y' if the equation is correct else enter 'n' ")
        print()

    #if a=0 then it will not be an quadritic equation .
        assert a!=0

        if ans.lower()=='y':
            print()
            quadritic(a,b,c)
        else:
            print('please again enter the equation according to the instructions. ')
            print()
            main()
        count=input('you want to continue for other equation(y/n).')
        print()
    print('bye!')

if __name__=='__main__':
    main()
        
