# Program that opens the CPLX2 gen and prints all the information contained in it

print('Program to print the information of the gen CPLX2')
print()
f = open('CPLX2.txt', 'r')
info = f.read()
print(info)
f.close()
