'''OOP in python creating class student getting their marks and printing their average scores.'''

class Students:
    MaxAvg=0
    def __init__(self,name,m1=0,m2=0,m3=0):
        self.name=name
        self.score1=m1
        self.score2=m2
        self.score3=m3
    
        if ((m1+m2+m3)/3)>Students.MaxAvg:
            Students.MaxAvg=round((m1+m2+m3)/3,2)
    
    def Display_Avg(self):
        return round((self.score1+self.score2+self.score3)/3 ,2)
        
    def Display_Maxavg(self):
        return Students.MaxAvg
    
    def __del__(self): #destructor
        print('Deleted!! by Destructor!!')
    
def main():
    students=int(input('Enter the number of students:'))
    for i in range (students):
        name=input('Enter the name of student:')
        score=eval(input('Enter the score  of 3 subjects in a list.'))
        S1=Students(name,score[0],score[1],score[2])
        print('Avrage marks of',name,'is:',S1.Display_Avg())
        print('')
    print('Maximum Average score of the class is:',S1.Display_Maxavg())
if __name__=='__main__':
    main()  
