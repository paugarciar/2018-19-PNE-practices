print("Practice 1")

# Creation of seq class
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        pass
        #comp_str=[]
        # pattern = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        #for base in string:
        #   comp_str.append(pattern[base])
    # here object complement()

    def reverse(self):
        return reversed(self.strbases)

    #count(base) and perc(base) need base but also self
