def Factorial(n):#using REcursion Finding the Factorial of a Number.
    if n==1:
        return n
    else:
        return n*Factorial(n-1)
from datetime import date
today = date.today()
print("Today's date is:", today)
def main():
    again='y'
    while again.lower()=='y':
        a=int(input('Enter the number whose Factorial is to be calculated.'))
        print('The Value of',a,'! =',Factorial(a))
        again=input('\nDo you want to print and check another value.(y/n)')
    print('Bye!')

if __name__=='__main__':
    main()
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime('%A'))
