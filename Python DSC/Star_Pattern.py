def star_pattern(a):
    """This is a function to print specific pattern until to a Row secified by user."""
    rows = 1
    while rows<=a:
        print('*'*rows)
        rows+=1
    
def main():
    z = int(input('Enter the numbers of rows to print * pattern:'))
    assert z>=1
    star_pattern(z)

if __name__=='__main__':
    main()
    
        
