def count_a(seq):
    """Counting the number of As in the sequence"""
    result=0
    #counter for As
    for b in seq:
        if b=="A":
            result+=1
    #return result
    return result
#main program
s="AGTACACTGGT"
na=count_a(s)
print("The number of As is:{}".format(na))

#calculate the total sequence length
tl=length

#calculate the percentage of As in the sequence
perc= round(100,0*na/ tl, 1)

print("The total length is: {}".format(tl))
print("The percentage of As is: {}%".format(perc))