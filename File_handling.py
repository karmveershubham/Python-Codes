def writeData():
    file = open('file1.txt','w') 
    file.write("Dyal Singh College owes its origin to the extreme generosity and foresight of Sardar Dyal Singh Majithia.\n") 
    file.write("He was the founder of ‘The Tribune’ and ‘Punjab National Bank’.\n")
    file.write("He willed his vast wealth in 1895 for the setting up of an Education Trust for a truly secular college.\n")
    file.write("Consequently, Dyal Singh College was established at Lahore in 1910.\n")
    file.write("After the Partition of India, Dyal Singh College was established in Karnal and in Delhi.\n")
    file.write("It started functioning in the capital as a constituent College of the University of Delhi in 1959.\n")
    file.write("It was taken over by the University of Delhi as a University maintained institution in 1978.\n")
    file.close() 

def writeAlternate():
    file = open('file2.txt','w') 
    file1 = open('file1.txt','r') 
    for i in range(7):
        s=file1.readline()
        if i%2==0:
            file.write(s)
    file.close()
    file1.close()

def countLetters():
    file=open('file2.txt','r')
    l=list("shubham")
    l=set(l)
    dic={}
    s=file.read()
    for i in l:
        dic[i]=s.count(i)    
    file.close()
    print(dic)

def main():
   writeData()
   writeAlternate()
   countLetters() 

main()
