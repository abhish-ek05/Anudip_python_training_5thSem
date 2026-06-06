'''Problem Statement 
A bus has seats represented as: 
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
Where: 
• 1 → Seat Booked  
• 0 → Seat Available  
Write a program to: 
1. Count booked and available seats.  
2. Find the first available seat and stop searching immediately.  
3. Create a list of all available seat numbers.  
4. Determine whether the bus is more than 70% occupied.  '''

seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
avail = 0
booked = 0
availst = []
firstSeat = 0
for i in seats:
    if i==0:
        avail += 1
        if firstSeat == 0 :
            firstSeat = seats.index(i)+1

        availst.append(seats.index(i)+1)
        seats.remove(i)
        
    else:
        booked += 1
        
print(availst)