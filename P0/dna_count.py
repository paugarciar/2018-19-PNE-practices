print('exercise4, tools ii')
print('program to count the total number of bases in a DNA sequence and the number of each different base')

dna_seq=input('enter a DNA sequence: ')
print('the length of the sequence is ', len(dna_seq))

A=dna_seq.count('A')
C=dna_seq.count('C')
T=dna_seq.count('T')
G=dna_seq.count('G')
print('A:', A)
print('C:', C)
print('T:', T)
print('G:', G)