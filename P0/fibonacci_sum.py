# Program that sums the fibonacci series therms until n (parameter entered by the user)

print('this program sums the fibonacci terms')
print('attention, for a correct result n>0, (the first position is 1)')
print('')
p = int(input('insert the position of the term of fibonacci series (n):'))
ls = [0, 1]


def fibonacci(n):
    for index in range(3, n+1):
        ls.append(ls[index-3]+ls[index-2])
    if p == 1:
        nth_term = ls[0]
    else:
        nth_term = ls[-1]
    return nth_term


def fibonacci_sum(n):
    value = fibonacci(n)
    summat = 0
    if value != 0:
        for i in ls:
            summat += i
    return summat


value2 = fibonacci_sum(p)
print('the value of the sum of the fibonacci terms until the position', p, 'is:', value2)
