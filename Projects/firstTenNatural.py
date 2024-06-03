natural_number=list(range(1,11))
print(natural_number)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplied_number=[i*2 for i in natural_number]
print(multiplied_number)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



num = int(input("Enter a number: "))

if num % 2 == 0:
    if num in range(2, 6):
        print("Not weird")
    elif num in range(6, 21):
        print("Weird")
    elif num > 20:
        print("Not weird")
else:
    print("Weird")

  