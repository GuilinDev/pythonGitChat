print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_nubmer = input("Second Number: ")
    if second_nubmer == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_nubmer)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)