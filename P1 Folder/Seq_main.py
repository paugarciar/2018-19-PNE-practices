# Program to calculate the length, number and percentage of bases of different DNA strings


# Creation of seq class
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases  # self.strbases now represents my initial string

    def len(self):
        return len(self.strbases)  # returns the length of our string(self.strbases)

    def complement(self):
        comp_str = ""  # this empty string will receive the complementary bases
        pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for base in self.strbases:
            comp_str += pattern[base]  # complementary bases are searched in the dictionary
        return comp_str

    def reverse(self):
        rev_str = self.strbases[::-1]  # inverting the order of the bases
        return rev_str

    def count(self, base):
        result = self.strbases.count(base)  # counting the base that we will introduce
        return result

    def perc(self, base):
        tl = len(self.strbases)
        n = self.strbases.count(base)
        if tl > 0:
            perc = round(100.0 * n / tl, 1)  # percentage with one decimal of precision

        else:
            perc = 0  # if there is an empty string
        return perc


# main function
print("Practice 1")

# creation of objects of the class Seq
s1 = Seq("ATAG")
s2 = Seq("CC")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())

# printing the results using loops
s = [s1, s2, s3, s4]  # list with all sequences
bases = "ACTG"  # string to iterate over the bases
n_bases = {}  # dictionary to save number of bases
percentage = {}  # dictionary for percentages


for sequence in s:
    if sequence == s1:
        name = "\nSEQUENCE 1:"  # name is different for each one
    elif sequence == s2:
        name = "\nSEQUENCE 2:"
    elif sequence == s3:
        name = "\nSEQUENCE 3:"
    else:
        name = "\nSEQUENCE 4:"
    print(name, sequence.strbases)  # accessing to the string in order to print it
    print(" Length:", sequence.len())  # calling attribute length

    for i in bases:
        n_bases[i] = sequence.count(i)  # adding in their corresponding dictionary the information
        percentage[i] = str(sequence.perc(i))+"%"  # percentage symbol string need another string to be added
    print(" Bases count: ", n_bases)
    print(" Bases percentage: ", percentage)  # printing finally the dictionaries
