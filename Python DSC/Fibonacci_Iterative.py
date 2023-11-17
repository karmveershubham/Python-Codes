def Fibonacci(n):#To find value of Fibonacci series.
    a=0
    b=1
    if  n<=0:
        print('Incorrect option')

    elif n==1:
        return a

    #elif n==2:
        #return b
    else:
        for i in range (2,n):
            c=a+b
            a=b
            b=c
        return b
def main():
    again='y'
    while again.lower()=='y':
        a= int(input('To get the nth term of febonacci seies. \nEnter the value of n:'))
        print ('The ', a, 'th term of fibonacci series is:',Fibonacci(a))
        again=input('\nDo you want to print and check another value.(y/n)')
    print('Bye!')
           
if __name__=='__main__':
    main()
           
           
