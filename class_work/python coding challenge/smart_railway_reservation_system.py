'''A railway reservation system stores the booking status of seats in a train coach. 
Sample Data 
seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
} 
Tasks 
1. Display all available seat numbers.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Cancel booking for a given seat number.  
5. Store the updated reservation status in reservations.txt.  
6. Display occupancy percentage.  '''

seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
}

seats = { 
    1: "Booked", 
    2: "Available", 
    3: "Booked", 
    4: "Available", 
    5: "Booked", 
    6: "Booked", 
    7: "Available", 
    8: "Booked", 
    9: "Available", 
    10: "Booked" 
}

# 1. Display available seats
print("Available seats are:")
for key, value in seats.items():
    if value == "Available":
        print(key, end=" ")
print("\n")

# 2. Count booked and available seats
countAvail = 0
countBooked = 0

for value in seats.values():
    if value == "Available":
        countAvail += 1
    else:
        countBooked += 1

print(f"Booked seats are: {countBooked}")
print(f"Available seats are: {countAvail}")
print("\n")

# 3. Reserve first available seat
reserved = False
for key, value in seats.items():
    if value == "Available":
        seats[key] = "Booked"
        print(f"Reserved seat is: {key}")
        reserved = True
        break

print("\n")

# 4. Cancel booking for a given seat number
seat = int(input("Enter seat number to cancel booking: "))

if seat in seats:
    if seats[seat] == "Booked":
        seats[seat] = "Available"
        print(f"Booking cancelled for seat: {seat}")
    else:
        print("Seat is already available")
else:
    print("Seat not present")

print("\nUpdated seat status:")
print(seats)

# 5. Save to file
with open("reservations.txt", "w") as file:
    for key, value in seats.items():
        file.write(f"{key}:{value}\n")

# 6. Occupancy percentage
total = len(seats)
occupied = countBooked

occupancy = (occupied / total) * 100
print(f"\nOccupancy percentage: {round(occupancy,2)}%")