print('program to calculate a term of fibonacci series')

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
value=fibonacci(p)
print('its corresponding value is', value)
