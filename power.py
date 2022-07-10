def power(n,i):
    '''
    求n的i次方
    10**5 = 10*10**4 
    10**4 =10*10**3
    10**1=10
    '''
    if i==1:
        return n
    return n * power(n,i-1)

print(power(8,6))