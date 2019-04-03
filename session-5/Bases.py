def count_bases(seq):
    """Counting the number of bases in the sequence"""
    resultA=seq.count("A")
    resultC=seq.count("C")
    resultT=seq.count("T")
    resultG=seq.count("G")
    number_bases={'Base A': resultA, 'Base C': resultC, 'Base T': resultT, 'Base G': resultG}
    #return result
    return number_bases