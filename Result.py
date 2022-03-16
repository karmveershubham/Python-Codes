'''Result.py is program that take input from user and show them their average marks.'''

def avgMarks(marks_list,Passmarks):# Function to find The average Percentage of Marks.
    
    for marks in marks_list:
        assert marks <= 100 #Asserting max marks should not Exceed 100.
        if marks < Passmarks:
            print('Essential Repeat')#Essential repeat if marks is less than Passing marks.
            return
    else:
        average=round(sum(marks_list)/3 , 2)#to find the average.
        print('\nThe Average Percentage of the Total marks is:',average,'%')
    

def main():
    Again ='y'
    print('\nAttention!\nEnter the marks in Given Format:[Marks_S1,Marks_S3,Marks_S3]')
    while Again.lower()=='y':
        marks_list=eval(input('\nEnter your marks in the three subjects in a list:'))
        if type(marks_list)!=list:  #Returning to main if input is not a list.
            print('Enter in valid Format suggested Above.')
            return main()
        Passmarks=int(input('\nEnter the passing marks for Subject:'))
        avgMarks(marks_list,Passmarks)
        Again=input('\nDo yow want to continue for another Data.(y/n):')
    print('Bye!')
    
if __name__=='__main__':
    main()
    

