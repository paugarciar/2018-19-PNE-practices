print("Program to count the number of bases and the percentage of two sequences")
def count_bases(seq):
    """Counting the number of bases in the sequence"""
    resultA=seq.count("A")
    resultC=seq.count("C")
    resultT=seq.count("T")
    resultG=seq.count("G")
    number_bases={'Base A': resultA, 'Base C': resultC, 'Base T': resultT, 'Base G': resultG}
    #return result
    return number_bases
# main program
s1=input("Please enter the sequence 1: ")
s2=input("Please enter the sequence 2: ")
s=[s1,s2]
for element in s:
    n = count_bases(element)
    na=n['Base A']
    nc=n['Base C']
    nt=n['Base T']
    ng=n['Base G']
    #calculate the total sequence length
    tl=len(element)
    print("\nAnalysis of sequence: {}".format(element))
    print("The total length is: {}".format(tl))
    #calculate the percentage of bases in the sequence
    if tl>0:
        perca= round(100.0* na / tl, 1)
        percc = round(100.0 * nc / tl, 1)
        perct = round(100.0 * nt / tl, 1)
        percg = round(100.0 * ng / tl, 1)
    else:
        perca=0
        percc=0
        perct=0
        percg=0

    print('\nBase A')
    print("The number of As is:{}".format(na))
    print("The percentage of As is: {}%".format(perca))

    print('\nBase C')
    print("The number of Cs is:{}".format(nc))
    print("The percentage of Cs is: {}%".format(percc))

    print('\nBase T')
    print("The number of Ts is:{}".format(nt))
    print("The percentage of Ts is: {}%".format(perct))

    print('\nBase G')
    print("The number of Gs is:{}".format(ng))
    print("The percentage of Gs is: {}%".format(percg))