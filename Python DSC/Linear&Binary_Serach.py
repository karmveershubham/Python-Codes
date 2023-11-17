def lin_search(list,srch_val):#To search a specific element in the list specified by the user.
    for i in range (0,len(list)+1):
        if srch_val==list[i]:
            return i
    return None
        
    
def bin_search(list,srch_val):#To search a specific element in the list specified by the user.

    first_val=0
    end_val=len(list)-1
    mid_val=0
    while first_val<=end_val:
        mid_val=((first_val+end_val)//2)
        
        if list[mid_val]<(srch_val):
            first_val = mid_val+1
            
        elif list[mid_val]>(srch_val):
            end_val=mid_val-1
        else:
            return mid_val
    return None    
        
def main():
    print("MENU for searching of lists:")
    print("1.Linear search")
    print("2.Binary serach")

    again='y'
    
    while again.lower()=='y':
        choice=input('\nEnter a choice for performing search operation.')
        if choice=='1':
            list=eval(input('\nEnter a list:'))
            srch_val=eval(input("Enter a value to search in the list."))
            srch_reslt1=lin_search(list,srch_val)
            print(srch_val,'found at index',srch_reslt1)

        
        elif choice =='2':
            list=eval(input('Enter a sorted list:'))
            for i in range (1,len(list)+1):
                if list[i]<list[i-1]:
                    print('The list is not sorted')
                else:
                    srch_val=eval(input("Enter a value to search in the list."))
                    srch_reslt2= bin_search(list,srch_val)
                    print(srch_val,'found at index',srch_reslt2)
                break   

        else:
            print('Enter a valid choice')
            
        again=input('\nDo you want to continue(y/n):')
    print('Bye')

    
if __name__=='__main__':
    main()
