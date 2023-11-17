#to find area of circle
#assgn a value for the radius 
radius=int(input("enter the radius"))
#compute the area
area=radius*3.14159*radius
#display the results 
print("if the radius is",radius, "Then area is",area, "                                                                                ");

#exercise 1
#first assign value for the width
width=int(input('Enter the width'))
#asign the value for the length
length=int(input('enter the length'))
#then compute the area
area=width*length
#display of the results 
print("if length is", length, "and width is", width,"area is", area,"                                                                     ");


#exercise 2

#conversion of 100 mile into KM
#assign the value of miles
miles=100
#writting conversion formulae:
kilometers=miles*1.609
#display of results
print("the value of", miles, "miles in kilometers is", kilometers, "KM")


def RectArea(length,breadth):
    return length*breadth
def CircleArea(radius):
    return 22/7*radius*radius

def main():
    length = eval(input('Enter the length:'))
    breadth = eval(input('Enter the breadth:'))
    area = RectArea(length,breadth)
    print(area)
    radius = eval(input('Enter the radius:'))
    areaC = CircleArea(radius)
    print(areaC)

if __name__ =='__main__':
    main()


