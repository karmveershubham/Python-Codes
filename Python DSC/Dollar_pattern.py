def dollar_pattern(row,column):
    """This is a function to print specific  $ pattern  specified by user."""
    a = 1
    while a<=row:
        if a == 1 or a == row:
            print("$"*column)
        else:
            print("$"+' '*(column-2)+'$')
        a+=1
        
def main():
    y = int(input('Enter the numbers of rows to print $ pattern:'))
    assert y>=1
    z = int(input('Enter the numbers of column to print $ pattern:'))
    assert z>=1
    dollar_pattern(y,z)

if __name__=='__main__':
    main()


for i in range (10):
    print(i)

str="Hello world"
for ch in str:
    print(ch)
l1=[1,2,3,4,5,6,7]
for j in l1:
    print (j)

