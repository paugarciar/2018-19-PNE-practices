print('program to sum the n first integers')

def sum_of_integers(s)
    k=0
    for i in range(s):
        k=i+1+k
    return k


int=int(input('please insert an integer number: '))
print(sum_of_integers(int))

"""Correction
def sumn(n):
    total=0
    for i in range(n):
        total=total+i+1
    return total
num=int(input('number: ')
total_sum=sumn(num)
print('the total sum is {}.format(num)')"""
