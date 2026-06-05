score = []
total = int(input("enter total number of players : "))

if total>0:
    for i in range(1,total+1):
        a = int(input(f"enter socre of player {i} : "))
        while a<0:
            print("no negative score !!!")
            a=int(input(f"enter socre of player {i} : "))

        else:
            score.append(a)
            
            
else:
    print("score is zero")  

print(f"total score is {sum(score)}")