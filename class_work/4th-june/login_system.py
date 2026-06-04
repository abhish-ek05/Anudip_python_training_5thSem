# A website allows users to log in using a password. The correct password is admin123. 
# Write a program that keeps asking the user to enter the password until the correct password is provided.

password = input("enter password :")

while password != "admin123":
    print("Wrong Password !!")
    password = input("Re-enter password ")
else:
    print("validation successful")
    