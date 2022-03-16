def LCM(a,b):#function to find LCM of two integers.
    if a>b:
        greater = a
    else:
        greater = b

    while (True):
        if ((greater%a==0)and (greater %b== 0)):

            lcm= greater
            break
        greater+=1
        
            

    print('LCM of',a,'and',b,'is:',lcm)

def main():
    again='y'
    while again.lower()=='y':
        a=int(input('Enter the 1st value.'))
        b=int(input('Enter the 2nd value.'))
        LCM(a,b)
        again=input('Do you want to compute another Data:(y/n)')
    print('Bye!')
        
if __name__=='__main__':
    main()
        
