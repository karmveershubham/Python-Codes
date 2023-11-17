def pattern(row):
    for i in range (1, row+1):
        for j in range (1,i+1):
            print(j,end= '')
        print()
def main():
    x= int(input('Enter the number of rows'))
    pattern(x)

if __name__=='__main__':
    main()
    
    
           
