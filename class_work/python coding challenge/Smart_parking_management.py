'''The parking status of vehicles in a mall is maintained as follows. 
Sample Data 
parking_slots = [ 
    "Occupied", "Vacant", "Occupied", "Vacant", 
    "Occupied", "Occupied", "Vacant", "Occupied", 
    "Vacant", "Occupied" 
] 
Tasks 
1. Display vacant parking slot numbers.  
2. Count occupied and vacant slots.  
3. Allocate the first vacant slot to a new vehicle.  
4. Calculate parking occupancy percentage.  
5. Store updated parking information in parking.txt.  '''

parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# 1. Display vacant slots
print("Vacant Parking Slots:")
vacant_slots = []

for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        print(i + 1, end=" ")
        vacant_slots.append(i)

print("\n")

# 2. Count occupied and vacant
occupied = 0
vacant = 0

for status in parking_slots:
    if status == "Occupied":
        occupied += 1
    else:
        vacant += 1

print("Occupied Slots:", occupied)
print("Vacant Slots:", vacant)

# 3. Allocate first vacant slot
for i in range(len(parking_slots)):
    if parking_slots[i] == "Vacant":
        parking_slots[i] = "Occupied"
        print("Vehicle Allocated to Slot", i + 1)
        break

# 4. Occupancy percentage
total = len(parking_slots)
occupancy = (occupied + 1) / total * 100  # because we just allocated one slot

print("Occupancy Percentage:", occupancy)

# 5. Save to file
f = open("parking.txt", "w")

for i in range(len(parking_slots)):
    f.write(f"Slot {i+1}: {parking_slots[i]}\n")

f.close()

print("Parking Details Saved Successfully.")