#function to finding Odd Even numbers.
def even_odd(number):
    if number%2 == 0:
        print(number, "is an Even number")
    else:
        print(number ,"is an Odd number")
    
def main():
    #getting the number to check f it's even or odd
     n = int(input('Enter anumber to check if it is Even or Odd'))
    #Calling the function
     even_odd(n)

if __name__=="__main__":
    main()
