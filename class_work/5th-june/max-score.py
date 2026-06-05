score = []
total = int(input("enter total number of players : "))

if total>0:

    for i in range(1,total+1):
        a = int(input(f"enter score of player {i} : "))

        while a<0:
            print("no negative score !!!")
            a=int(input(f"enter score of player {i} : "))

        score.append(a)
  
    print(f"maximum score is {max(score)}")

elif total==0:
    print("score is zero") 

else:
    print("invalid entry") 
    

