def selection_sort (lst):
    for i in range (0,len(lst)):
        min_index = i
        for j in range (i,len(lst)):
            if lst[j]<lst[min_index]:
                min_index=j
        if min_index!=i:
            lst[min_index],lst[i]=lst[i],lst[min_index]
            
def insertion_sort(lst):
    for i in range (1,len(lst)):
        temp= lst[i]
        j=i-1
        while j>=0 and lst[j] > temp:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]= temp
    print()

def main():
    again='y'
    while again.lower()=='y':
        print("MENU")
        print('1.To perform selection sort.')
        print('2.To perform insertion sort.')
        choice=int(input('Enter the option to perform sorting of list.'))
        lst= eval(input('Enter a list to sort.'))

        if choice == 1:
            selection_sort(lst)
        elif choice==  2:
            insertion_sort(lst)
        else:
            print('choose a  valid option.')
        print('The sorted list is:',lst)
        again=input('\nDo you want to continue.(y/n):')
    print('Bye!')
    
if __name__=='__main__':
   main()
