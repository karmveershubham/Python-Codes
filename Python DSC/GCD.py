def GCD(a,b):#function to findgcd of two given numbers.
    if a>b:
        smaller = a
    else:
        smaller = b

    for i in range (1,smaller+1):
        if ((a%i ==0) and (b%i== 0)):
            gcd = i
            
    print('GCD of ', a, 'and', b, 'is:' ,gcd)
        
def main():
    again='y'
    while again.lower()=='y':
        a=int(input('Enter the 1st value.'))
        b=int(input('Enter the 2nd value.'))
        GCD(a,b)
        again=input('Do you want to compute another Data:(y/n)')
    print('Bye!')
        
if __name__=='__main__':
    main()
        
