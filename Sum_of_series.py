import math

def sum_of_series(n):
    # A Simple Function to return value of 1/0!-1/1! + 1/2! - .. ... 1/n! 
    print('The value of 1/0!-1/1! + 1/2! - .. ... 1/n! where n=',n,)
    a=1
    for i in range (1,n+1):      
        
        if i%2==0:
            i=math.factorial(i)
            x=1/i
            a=a+x
        
        elif i%2!=0:
            i=math.factorial(i) 
            z=-1/i
            a=a+z
    print('Sum of sries is:', a)
    
def main():
    n=int(input('Enter the nth number for the series.'))
    assert n>=0
    sum_of_series(n)

if __name__=='__main__':
    main()
