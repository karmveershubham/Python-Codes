def prime(num):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                print(num,'is not a prime number')
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,'is anot a prime number')

    print('All the prime number s in given range are:')

    for i in range (2,num):
        if i>1:
            for j in range (2,i):
                if i%j==0:
                    break
            else:
                print(i)
def main():
    num = int(input('5enter a number'))
    prime (num)

if __name__=='__main__':
    main()
