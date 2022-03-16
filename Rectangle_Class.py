"""OOP in python creating rectangl class and calculating it's perimeter and area."""

class rectangle:  
    def __init__(self,length,breadth):#constructor
        self.breadth=breadth
        self.length=length
        
    def area(self):
        return self.breadth*self.length
    
    def perimeter(self):
        return 2*(self.breadth+self.length)
    
    def __del__(self): #destructor
        print('Deleted!!')
        
def main():
    a= int (input('Enter the length of rectangular Playground..'))
    b=int(input('Enter the bradth of the rectangular Palyground.'))
    obj = rectangle(a,b)
    print('Area of  Rectangular Playground:',obj.area(),'m sq.')
    print('Perimeter of Rectangular Playground:',obj.perimeter()'m sq.')

if __name__=='__main__':
    main()
