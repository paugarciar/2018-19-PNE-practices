print('this program sums the fibonacci terms')
print('attention, for a correct result n>0, (the first position is 1)')
print('')
p=int(input('insert the position of the term of fibonacci series (n):'))
l=[0,1]

def fibonacci(n):
    for index in range(3,n+1):
        sum=l[index-3]+l[index-2]
        l.append(sum)
    if p==1:
        nth_term=l[0]
    else:
        nth_term= l[-1]
    return nth_term


def fibonacci_sum(n):
    value=fibonacci(n)
    sumatory=0
    if value!=0:
        for i in l:
            sumatory += i
    return sumatory


value2=fibonacci_sum(p)
print('the value of the sum of the fibonacci terms until the position', p, 'is:', value2)
