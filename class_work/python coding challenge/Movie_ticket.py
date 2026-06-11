'''Seat booking status in a cinema hall is stored as follows. 
Sample Data 
tickets = { 
    "A1": "Booked", 
    "A2": "Available", 
    "A3": "Booked", 
    "A4": "Available", 
    "B1": "Booked", 
    "B2": "Available", 
    "B3": "Booked", 
    "B4": "Available", 
    "C1": "Booked", 
    "C2": "Available" 
} 
Tasks 
1. Display available seats.  
2. Count booked and available seats.  
3. Reserve the first available seat.  
4. Save updated booking details to tickets.txt.  
5. Calculate hall occupancy percentage.  '''

tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# 1. Display available seats
print("Available Seats:")
available_seats = []

for seat in tickets:
    if tickets[seat] == "Available":
        available_seats.append(seat)
        print(seat)

# 2. Count booked and available seats
booked_count = 0
available_count = 0

for seat in tickets:
    if tickets[seat] == "Booked":
        booked_count += 1
    else:
        available_count += 1

print("\nBooked Seats:", booked_count)
print("Available Seats:", available_count)

# 3. Reserve first available seat
if len(available_seats) > 0:
    first_seat = available_seats[0]
    tickets[first_seat] = "Booked"
    print("\nFirst available seat reserved:", first_seat)

# 4. Save updated details to file
file = open("tickets.txt", "w")

for seat in tickets:
    file.write(seat + "," + tickets[seat] + "\n")

file.close()

# 5. Hall occupancy percentage
total_seats = len(tickets)
occupancy = (booked_count / total_seats) * 100

print("\nHall Occupancy Percentage:", occupancy)