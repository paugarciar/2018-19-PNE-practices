

# Creation of seq class
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        comp_str=""
        pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        for base in self.strbases:
            comp_str+=pattern[base]
        return comp_str

    def reverse(self):
        rev_str = self.strbases[::-1]
        return rev_str

    def count(base):
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
        return A, C, T, G

    def perc(base):
        tl = len(element)
        n = s1.count(base)#finish this
        if tl > 0:
            perca = round(100.0 * na / tl, 1)
            percc = round(100.0 * nc / tl, 1)
            perct = round(100.0 * nt / tl, 1)
            percg = round(100.0 * ng / tl, 1)
        else:
            perca = 0
            percc = 0
            perct = 0
            percg = 0

print("Practice 1")

s1=Seq("AATG")
s1.complement()
s1.reverse()