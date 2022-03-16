#Getting cube of key values in a dictionary.

def Dict(a,b):
    Dic=dict()
    for i in range (a,b+1):
        Dic[i]=i**3
    print('The Dictionary with cube of keyvalues:',Dic)
    
def main():
    print('To get the cube of keys in dictionary.')
    a=1
    b=int(input('Enter the Range till you want to print dictionary.'))
    Dict(a,b)
    
if __name__=='__main__':
    main()
