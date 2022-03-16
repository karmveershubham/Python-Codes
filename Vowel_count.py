'''Vowel count in a file using file handling in python.'''

def f_hand(file):
    f=open(file,'r')
    str=f.read()
    print('The file contains following data:\n',str)
    f.close()
    Dict(str)

def Dict(str):
    vowels='aeiou'
    Dic={}
    for ch in vowels:
        count=str.count(ch)
        Dic[ch]=count
    print('Dictionary with count of each vowels in strings.',Dic)
    


def main():
    file=str(input('Enter the File name.'))
    f_hand(file)

if __name__=='__main__':
    main()
    
    
