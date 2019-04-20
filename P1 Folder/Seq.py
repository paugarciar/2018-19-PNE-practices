# Creation of seq class that will be used in Seq_main.py
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
