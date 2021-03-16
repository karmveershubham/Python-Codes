#function to find Area
def RectArea(Length, Breadth):
    return Length*Breadth

def main():
    #Entering the length
    Length = eval(input('Enter the value of length in meters:'))
    #Entering the Breadth
    Breadth = eval(input('Enter the value of Breadth in meters:'))
    #caliing the function
    Area = RectArea(Length,Breadth)
    print('Area of the rectanle with length',Length, 'and breadth',Breadth, 'is',Area,'metre sq.')

if __name__ == '__main__':
    main()

    

                 
    
    
