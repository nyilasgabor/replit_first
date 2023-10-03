n = int(input("Enter the number of values: "))
total = 0
for i in range(n):
  num = int(input(f"Enter number {i + 1}: "))
  total += num
print(f"The sum of the numbers is: {total}")
