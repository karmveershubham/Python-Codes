def string_set(s1,s2):
    set1=set(s1)
    set2=set(s2)
    print('The set of first string is',set1)
    print('The set of second string is',set2)
    
def Com_char(s1,s2):
    common=set(s1).intersection(set(s2))
    print('The set of common characters is', common)
    
    
def Diff_char(s1,s2):
    difference=set(s1)^set(s2)
    print('The set ofdistinct Character is',difference)
    
def main():
    again='y'
    while again.lower()=='y':
        print("MENU")
        print('1.convert each string into  a seperte list')
        print('2.To display common characters between the sets.')
        print('3.To display Distinct character in the list.')
        choice=int(input('Enter a valid choice'))
        s1=input('Enter the first string:')
        s2=input('Enter the second string:')
        
        if choice == 1:
            string_set(s1,s2)
        elif choice==  2:
            Com_char(s1,s2)
        elif choice == 3:
            Diff_char(s1,s2)
        else:
            print('choose a  valid option.')
        again=input('Do you want to continue.(y/n):')
    print('Bye!')
    
if __name__=='__main__':
   main()            
        
        
            
        
    
