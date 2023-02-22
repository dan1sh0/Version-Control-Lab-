numbers = []
while True: 
   # enter as many numbers as you want 
   num = input("Enter a number(or enter 'done' to finish): ")
   if num == 'done':
      break
   else:
      numbers.append(float(num))

if numbers:
    average = sum(numbers) / len(numbers)
    print("The average of the numbers is:", average)
else:
    print("No numbers were entered.")
   