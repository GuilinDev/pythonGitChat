current_number = 1
while(current_number <= 5):
    print(current_number)
    current_number += 1

print("\n")
# test continue
current_number2 = 0
while(current_number2 < 10):
    current_number2 += 1
    if current_number2 % 2 == 0:
        continue
    print(current_number2)