# wap to input 10 sentences from the user and write them to a file 

f = open("file_handling.txt", "w")

for i in range(4):
    print(f"enter line number {i+1} ", end=" ")
    text = input()
    f.write(text)
    f.write("\n")
f.close()
print("data has been written successfully")

