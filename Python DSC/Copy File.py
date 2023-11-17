def Copy_file():
    f1= open("File1.txt","r")#opens the source file.
    f2= open("File2.txt","w")#create the  destination file to perform the operation.
    l=0
    c=0
    for line in f1:
        f2.write(line)
        l+=1
        c+=len(line)
    print("Number of lines in the file: ",l)
    print("Number of characters in the file: ",c)

def main():
    Copy_file()

if __name__=="__main__":
    main()
        
