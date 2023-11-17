def Rect_Area(len,breadth):#calculate the area of rectangle and square both.
    area=len*breadth
    print('Area of selected shape',area,'sq. unit')

def Area_circle(rad):#calculate the area of circle.
    area = 3.14*rad*rad
    print('Area of circle with radius',rad, 'is',round(area,2),'sq. unit')

def area_Triangle(base,height):#calculate the area of  triangle.
    area = (1/2)*base*height
    print('Area of Triangle',area,'sq. unit')
    
    
def main():
    print('MENU!\nwelcome! select the option to which area you want to calculate.')
    print('1.calculate the area of RECTANGLE.')
    print('2.calculate the area of SQUARE.')
    print('3.calculte the area of CIRCLE.')
    print('4.calculate the area of TRIANGLE.')
    n='y'
    while n.lower()=='y':
        a=int(input('select option:'))
        assert a>=1 and a<=4
    
        if a==1:
            len=int(input('Enter the length:'))
            breadth = int(input('Enter the breadth:'))
            Rect_Area(len,breadth)
            print()
        elif a==2:
            side=int(input('Enter the length of side:'))
            Rect_Area(side,side)
            print()
        elif a==3:
            rad=int(input('Enter the radius:'))
            Area_circle(rad)
            print()
        else:
            base=int(input('Enter the length of base:'))
            height= int(input('Enter the height:'))
            area_Triangle(base,height)
            print()

        n=input('Do you want to continue?(y/n):')
        print()
    print('BYE!')
        

if __name__=='__main__':
    main()
        
    
    
