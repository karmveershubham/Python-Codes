def check_num(list):  #checking if list contain any numeric value.
    for elements in list:
        if not str(elements).isdigit():
            print("\nAll elements are not Numbers.")
            return False

    print("\nAll elements are numbers")
    return True

def count_odd(list):   # counting odd values.
    if check_num(list)==True:
        count=0
        for elements in list:
            if elements%2!=0:
                count+=1
        print("Numbers of odd values in list is:", count)
    else:
        print("List contains non-numeric values so can't count odd number.")

def large_string(list):  #Getting the largest string.
    if check_num(list)==True:
        print("Can't perform this operation on integers.")
             
    else:
        largest=list[0]
        for i in list:
            if len(largest)<len(i):
                largest = i
        print("Largest string in the list is:",largest)

def count_alpha_num(list):  # counting alphanumeric strings in the list.
    num=0
    for items in list:
        if str(items).isdigit()==True:
            num+=1
    print("The number of numeric strings in list are:", num)
    Total_elmnt=len(list)
    alphabets=Total_elmnt-num
    print("the number of alphabetic strings in the list are:",alphabets)
    
def main():
    again='y'
    while again.lower()=='y':
        
        print("\nMENU OF LIST OPERATION\n")
        list=eval(input("Enter the list on which you want to perform operations."))
        
        print("\n1.To check all the elements in a list are numbers or not.")
        print("2.To count numbers of Odd values.")
        print("3.Display of Largest string in the list.")
        print("4.To count of numeric and Alphabetic Strings.")
        choice=int(input("Enter your choice of operation."))
                   
        if choice==1:
            check_num(list)
        elif choice==2:
            count_odd(list)
        elif choice==3:
            large_string(list)
        elif choice==4:
            count_alpha_num(list)
        again=input('\nDo you want to continue.(y/n):')
    print('Bye!')

if __name__=='__main__':
    main()

        
            
   
