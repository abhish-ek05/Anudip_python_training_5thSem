# wap to input a sentence from the user and count the numbers of special characters present in the sentence

sent=input("enter any sentence : ")
count = 0
for i in range(len(sent)):
    if not sent[i].isalnum():
        count += 1
print (f" special characters are {count}")