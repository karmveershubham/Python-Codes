def half_tup(t1):
    print('The output is:')
    for i in range(0,len(t1)//2):
        print(t1[i],end='')
    print()
    for j in range(len(t1)//2,len(t1)):
        print(t1[j],end='')


def even_tup(t1):
    list1=[]
    for i in range(0,len(t1)):
        if t1[i]%2==0:
            list1.append(t1[i])
    t2=tuple(list1)
    return t2


def conc(t1,t2):
    t1_new=t1+t2
    return t1_new


def min_max(t1):
    print('The minimum value in the above tuple is',min(t1))
    print('The maximum value in the above tuple is',max(t1))



def main():
    t1=(1,2,5,7,9,2,4,6,8,10)
    t_2=(11,13,15)
    half_tup(t1)
    print('\nThe even elements containing tuple is',even_tup(t1))
    print('nThe tuple to be concatenated with former tuple is:',t_2)
    print('The concatenated tuple is:',conc(t1,t_2))
    min_max(t1)

if __name__=='__main__':
    main()
