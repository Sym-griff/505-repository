

# create empty list 
numbers = []

#Loop 10 times to get 10 numbers from user
for i in range(10):

    #get number from user and convert it to integer 
    n = int(input("Enter a number: "))

    #add number to the list 
    numbers.append(n)

# Display original list
print("\nOriginal list:", numbers)

# Count even and odd numbers
even = 0
odd = 0

# loop through all numbers in list and check which ones are even and odd 
for n in numbers:
    #increase count if even 
    if n % 2 == 0:
        even += 1
    #increase count if odd
    else:
        odd += 1

    #display results of even and odd count 
print("\nEven numbers:", even)
print("Odd numbers:", odd)

# ask user to ask for a number to search for 
search = int(input("\nEnter a number to search for: "))


#see if number exists in list 
if search in numbers:
    #display if number exists in list and its index 
    print(f"\n{search} found at index {numbers.index(search)}")
else:
    #Display if number doesnt exists in list 
    print("\nSorry the data you are looking for does not exist in the list")

# displayfirst three elements using List slicing
print("\nFirst three elements:", numbers[:3])

# display max, min, and sum of the list 
print("\nMaximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of values:", sum(numbers))

# make copy the original list
numbers_copy = numbers.copy()

# Sort the copied list
numbers_copy.sort()

#display both lists 
print("\nOriginal list (before sorting):", numbers)
print("\nSorted copied list:", numbers_copy)
print("\nOriginal list (after sorting copied list):", numbers)

# create a new list with squares using comprehension
squares = [n * n for n in numbers]

#display squares list
print("\nSquares list:", squares)
