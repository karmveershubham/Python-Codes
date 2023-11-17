def dollar_pattern(row,column):
    """This is a function to print specific  $ pattern  specified by user."""
    a = 1
    print('$'*column)
    while a<=row-2:
        b = 1
        st=""
        while b<=column-2:
            st+=' '
            b+=1
        a+=1

        print('$'+st+'$')
    print('$'*column)
            
def main():
    y = int(input('Enter the numbers of rows to print $ pattern:'))
    assert y>=1
    z = int(input('Enter the numbers of column to print $ pattern:'))
    assert z>=1
    dollar_pattern(y,z)
    print('Bye!')

if __name__=='__main__':
    main()
