# wap to input the sentence and display the frequency of vowels which are present in the given sentence

sent=input("enter any sentence : ")

freqA= 0
freqE = 0
freqI = 0
freqO = 0
freqU = 0
for i in sent:
    if i in "aA":
        freqA+=1
    elif i in "eE":
        freqE+=1
    elif i in "iI":
        freqI+=1
    elif i in "oO":
        freqO+=1
    elif i in "uU":
        freqU+=1

if freqA > 0:
    print("a : ",freqA)
if freqE > 0:
    print("e : ",freqE)
if freqI > 0:
    print("i : ",freqI)
if freqO > 0:
    print("o : ",freqO)
if freqU > 0:
    print("u : ",freqU)
