# Printing the number of fibonacci series located in the position n

print('program to calculate a term of fibonacci series')
print('attention, for a correct result n>0, (the first position is 1)')
print('')
p = int(input('insert the position of the term of fibonacci series (n):'))
ls = [0, 1]


def fibonacci(n):
    for index in range(3, n+1):
        ls.append(ls[index-3]+ls[index-2])  # we add to the list a number that is the sum of the two last

    if p == 1:
        nth_term = ls[0]  # the number in the first position is 0

    else:
        nth_term = ls[-1]

    return nth_term


value = fibonacci(p)
print('its corresponding value is', value)
