def func(a):
    """This is the function to count n natural numbers from 1"""
    count = 1
    while count<= a:
        print(count)
        count+=1
def main():
    z = int(input('Enter the nth natural number:'))
    func(z)

if __name__=='__main__':
    main()
    
    
