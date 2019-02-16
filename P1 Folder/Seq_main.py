# Creation of seq class
class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        comp_str = ""
        pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for base in self.strbases:
            comp_str += pattern[base]
        return comp_str

    def reverse(self):
        rev_str = self.strbases[::-1]
        return rev_str

    def count(self, base):
        result = self.strbases.count(base)
        return result

    def perc(self, base):
        tl = len(self.strbases)
        n = self.strbases.count(base)
        if tl > 0:
            perc = round(100.0 * n / tl, 1)

        else:
            perc = 0
        return perc


# main function
s1 = Seq("AATG")
s2 = Seq("TC")
s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())
s=[s1, s2, s3, s4]
bases=["A","C", "T", "G"]
n_bases=[]
percentage=[]
for sequence in s:
    if sequence == s1:
        name = "\nSEQUENCE 1:"
    elif sequence == s2:
        name = "\nSEQUENCE 2:"
    elif sequence == s3:
        name = "\nSEQUENCE 3:"
    else:
        name = "\nSEQUENCE 4:"
    print(name, sequence.strbases)
    print(" length:", sequence.len())
    for i in bases:
        print("Bases count: ")
        print(sequence.count(i))
        print("Bases percentage: ")
        print(sequence.perc(i))
