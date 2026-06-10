f = open("employees.txt","w")
f.writelines(2)

f.close()

f = open("employees.txt","r")
print(f.read())