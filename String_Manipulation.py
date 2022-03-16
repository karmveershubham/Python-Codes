def strng_tasks(choice,string):
    if choice==1:
        str1=input('Enter string whose position you would like to find.')
        print('\nThe position of ',str1,'is:',string.rfind(str1))
        
    elif choice==2:
        str1=input("Enter the substring you want to replace:-")
        str2=input("Enter the substring you want to replace with :-")
        string=string.replace(str1,str2)
        print('\nThe new string with replacement is:', string)
        
    elif choice==3:
        delimiter=input('Enter the delimiter on which basis the sting is separated.')
        string = string.split(delimiter)
        print('\nStrings seperated by',delimiter,'is:',string)

    elif choice==4:
        string = string.title()
        print('\nString in title form is:',string)

    elif choice==5:
        string =string.swapcase()
        print('\nString with swapcase is:',string)
        
def main():
    print('MENU:-')
    print("1.Look for a substring in the given string and returns its position.")
    print("2.Replace substring'good' with 'best'  in given string.")
    print("3.Find all the  substring  in the string which are separated by delimiter:")
    print("4.Convert the given text into title form.")
    print("5.Convert lowercase  to uppercase  and uppercase to lowercase in the given string.")
    print("6. Exit")

    choice=int(input('Enter the choice'))
    assert choice>0 and choice<=6
    while choice!=6:
        string=input('Enter the string you want to Edit.') 
        st=strng_tasks(choice,string)
        print('')
        choice=int(input('Enter the choice again.'))
        assert choice>0 and choice<=6
    else:
        print("Bye!")
        
if __name__=='__main__':
    main()
    
