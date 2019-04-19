# Program that counts the bases of the gen CPLX2

print('Program to count the different bases of the gen CPLX2')
print()
f = open('CPLX2.txt', 'r')
info = f.read()
info = info.split('\n')
A = 0
C = 0
T = 0
G = 0
for index in info:
    if len(index) != 0 and index[0] != '>':
        A += index.count('A')
        C += index.count('C')
        T += index.count('T')
        G += index.count('G')

print('A:', A)
print('C:', C)
print('T:', T)
print('G:', G)

f.close()
