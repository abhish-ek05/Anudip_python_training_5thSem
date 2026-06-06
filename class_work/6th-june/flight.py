'''Problem Statement 
A flight reservation system stores passenger records as tuples: 
bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
) 
Where: 
• Passenger ID  
• Destination  
• Booking Status  
Tasks 
Write a Python program to: 
1. Display all passengers whose booking status is Confirmed.  
2. Count the number of passengers travelling to Delhi.  
3. Count Confirmed, Waiting, and Cancelled bookings separately.  
4. Create a list containing passenger IDs with Waiting status.  
5. Determine which destination has the highest number of bookings.  '''

bookings = ( 
    ("P101", "Delhi", "Confirmed"), 
    ("P102", "Mumbai", "Waiting"), 
    ("P103", "Delhi", "Confirmed"), 
    ("P104", "Chennai", "Cancelled"), 
    ("P105", "Mumbai", "Confirmed"), 
    ("P106", "Delhi", "Waiting") 
) 