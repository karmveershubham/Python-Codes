def seperate(Tup):
    print('The sepertaed tuples are:')
    for i in range(0,len(Tup)//2):
        print(Tup[i],end='')
    print()
    for j in range(len(Tup)//2,len(Tup)):
        print(Tup[j],end='')

def even(Tup):
    list=[]
    for i in range(0,len(Tup)):
        if Tup[i]%2==0:
            list.append(Tup[i])
    Tup1=tuple(list)
    print('The Even Tuples are:', Tup1)

def conc(Tup):
    Tup1=eval(input('Enter the tuple you want to concatenate'))
    print(Tup+Tup1)

def max_min(Tup):
    print('The max value in the given tuple is:',max(Tup))
    print('The min value in the given tuple is:', min(Tup))
    
    
    
def main():
    again='y'
    while again.lower()=='y':
        print("MENU")
        print('1.To print the tuples in two line by separating into middle.')
        print('2.To print the tuples with even numbers.')
        print('3.To concatenate a given tuple.')
        print('4.To return the minimum and maximum value from tuple.')
        choice=int(input('Enter a valid choice'))
        Tup=eval(input('Enter the Tuple on which you perform these operation.')) 
        
        if choice == 1:
            seperate(Tup)
        elif choice==  2:
            even(Tup)
        elif choice == 3:
            conc(Tup)
        elif choice== 4:
            max_min(Tup)
            
        else:
            print('choose a  valid option.')
        again=input('\nDo you want to continue.(y/n):')
    print('Bye!')
    
if __name__=='__main__':
   main()            
