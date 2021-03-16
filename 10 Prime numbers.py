def list_prime(n):#function to print the list of prime numbers in given number.
    print('The list of prime numbers in range 1 to', n,'is:')

    for a in range(2,n+1):
        prime = True
        for i in range (2,a):
            if a%i==0:
                prime=False
        if prime:
            print(a,end=' ')


def check_prime(n):#function to check whether the number is prime or not.
    
    if n>1:
        for i in range (2,n):
            if (n%i)==0:
                print(n,'is not a prime number')
                break
        else:
            print(n,"is a prime number")
    else:
        print(n, 'is not a prime number.')
def main():
    again='y'
    while again.lower()=='y':
        
        a= int(input('Enter the number to determine it is prime or not.'))
        check_prime(a)
        list_prime(a)
        again=input('\nDo you want to print and check another value.(y/n)')
    print('Bye!')
           

if __name__=='__main__':
    main()
