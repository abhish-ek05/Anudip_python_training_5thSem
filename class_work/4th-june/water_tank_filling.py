import time

level = 0
while level < 100:
    level = level + 10
    print(f"water level is {level}")
    time.sleep(5)
print("water tank is full")