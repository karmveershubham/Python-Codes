def primes(T1):#Function to find cubes of  prime numbers from the given tuple and to print them in dictionary '''
    T2=[]
    for num in T1:#To check the prime numbers and get their values simaltaneously.
        prime = True
        if num==1:
            prime=False
        for i in range (2,num):
            if num%i==0 :
                prime=False
           
        if prime: #Appending the values in the list
            T2.append(num)
    print('The list of Prime Numbers is:',T2)
    PrimeCubes={ num:num**3 for num in T2 }
    print('The Cubes of Primes:',PrimeCubes)#printing the cubes of prime from  PrimeCube Dictionary.
        
def main():
    Again ='y'
    while Again.lower()=='y':
        T1= eval(input('Enter a Tuple of natural numbers.'))
        primes(T1)
        Again=input('\nDo yow want to continue for another Data.(y/n):')
    print('Bye!')
    
   

if __name__=='__main__':
    main()
