def sum_func(a):
     """This is the function to count sum of 1st n natural numbers from 1"""
     count = 1
     sum = 0
     while count<= a:
         sum = sum+count
         count += 1
     print('Sum of all the 1st n Natural Numbers:',sum)

def main():
    z = int(input('Enter the nth natural number:'))
    assert z >= 1
    sum_func(z)
    return (sum)

if __name__=='__main__':
    main()
