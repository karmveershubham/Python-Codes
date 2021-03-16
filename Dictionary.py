def Dict(string):
    vowels='aeiou'
    Dic={}
    for ch in vowels:
        count=string.count(ch)
        Dic[ch]=count
    print('Dictionary with count of each vowels in strings.',Dic)
    
    
def main():
    a=input('Enter the string  to print the dictionary of vowels in it.')
    string=a.lower()
    Dict(string)
    
if __name__=='__main__':
    main()
