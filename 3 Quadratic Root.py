import math

def Quad_eqn(a,b,c):
    
    D = (b**2)-(4*a*c)
    print('Descriminant of Quadratic equation is',round(D,2))
    
    
    if D<0:
        sqrt_val=(math.sqrt(-D))
        x1 = round(-b/(2*a),2)
        x2 = round(-b/(2*a),2)
        print('Roots of the Quad. equation are imaginary.\nx1=',x1,'+',round(sqrt_val/(2*a),2),'*i')
        print('x2=',x2,'-',round(sqrt_val/(2*a),2),'*i')
        print()
        
    elif D == 0:
        x1 =round(-b/(2*a),2)
        x2 = round(-b/(2*a),2)
        print('Roots of the Quad. equation are equal.\nx1=',x1)
        print('x2=',x2)
        print()

    else :
        sqrt_val1=(math.sqrt(D))
        x1 =round((-b + round(sqrt_val1,2))/(2*a),2)
        x2 =round((-b - round(sqrt_val1,2))/(2*a),2)
        print('Roots of the Quad. equation are equal.\nx1=',x1)
        print('x2=',x2)
        print()
        
def main():
    again = 'y'
    while again.lower()=='y':
        print('For the Quadratic equatin in the form of ax^2+bx+c.')
        a=eval(input('Enter the value of a:'))
        assert a!=0
        b=eval(input('Enter the value of b:'))
        c=eval(input('Enter the value of c:'))
        Quad_eqn(a,b,c)
        print()
        again=input('do yo want to find Roots for another Quadratic Equation.(y/n):')
        print()
    print('Bye!!')
    
        
if __name__=='__main__':
    main()            
        

        
    
