#defining function for assigning Grades.
def assign_grade(percentage):
    if percentage>=90:
        print("Congratulations, you got grade = 'A'")
    elif percentage>=70:
        print("you got grade = 'B'")
    elif percentage>=50:
        print("you got grade = 'C'")
    else:
        print("you got grade = 'D'")

def main():
    #entering the marks gained in each subject.
    marks1 = float(input('Enter your marks for 1st subject'))
    marks2 = float(input('Enter your marks for 2nd subject'))
    marks3 = float(input('Enter your marks for 3rd subject'))
    #calculating Total marks.
    total_marks = marks1+marks2+marks3
    print('Your Total Marks are:',total_marks)
    #calculating Percentage
    percentage = (total_marks)/3.0
    print('Your Percentage is:',round(percentage),'%')
    #calling the Function.
    assign_grade(percentage)


if __name__=='__main__':
    main()                   


