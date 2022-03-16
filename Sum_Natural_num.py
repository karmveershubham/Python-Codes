def count_func(a):
    """This is the function to count 1st n natural numbers from 1"""
    count = 1
    while count<= a:
        print(count)
        count+=1
        
def sum_func(a):
     """This is the function to count sum of 1st n natural numbers from 1"""
     count = 1
     sum = 0
     while count<= a:
         sum = sum+count
         count += 1
     print('Sum of all the 1st n Natural Numbers:',sum)

def sum_func1(a):
     """This is the function to count sum of 1st n natural numbers from 1"""
     count = 1
     sum = 0
     while count<= a:
         sum = sum+count
         count += 1
     return (sum)
     
def main():
    z = int(input('Enter the nth natural number:'))
    #assert z >= 1
    count_func(z)
    sum_func(z)
    s=sum_func1(z)
    print('Sum of all the 1st n Natural Numbers:',s)

if __name__=='__main__':
    main()
