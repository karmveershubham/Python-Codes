def reverse(a):
    x=int(a[-1::-1])
    print('the reverse of number',a,'is',x)
def main():
    again='y'
    while again.lower()=='y':
        a=int(input('Enter the number to reverse:'))
        assert a>=0
        b = str(a)
        reverse(b)
        again=input('Do you want to reverse another number.(y/n)')
    print('Bye!')

if __name__=='__main__':
    main()
    
    
