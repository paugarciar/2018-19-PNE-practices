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
s=input("Please enter the sequence: ")
na=count_a(s)
print("The number of As is:{}".format(na))

#calculate the total sequence length
tl=length

#calculate the percentage of As in the sequence
if tl>0:
    perc= round(100.0* na / tl, 1)
else:
    perc=0

print("The total length is: {}".format(tl))
print("The percentage of As is: {}%".format(perc))