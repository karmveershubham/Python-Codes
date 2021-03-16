#function is for checking if a person is eligible to Caste Vote or not
def CasteVote(Age_of_Person):
    if Age_of_Person >= 18:
        print('Your age is', Age_of_Person,'so You are Eligible to Caste Your Vote, Thanks!')
    else:
        print('Sorry,Your Age is',Age_of_Person,'so You are too Young to Caste Vote.')
        
def main():
    Age = int(input('Enter Your Age to check Your Eligibility to Caste Your Vote'))
    CasteVote(Age)
              
if  __name__=='__main__':
    main()
