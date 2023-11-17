def Com_char(a,b):
    
    x = a.lower()
    y = b.lower()


    character=0
    for  char1 in  x:
        for char2 in y:  
            if char1==char2:
                character += 1
    print("The number of common character is:",character)


def main():
    again='y'
    while again.lower()=='y':
        a= input('Enter the 1st word:')
        b= input('Enter the word to find common character:')
        Com_char(a,b)
        again=input('\nDo you want to print and check another value.(y/n)')
    print('Bye!')

if __name__=='__main__':
    main()
