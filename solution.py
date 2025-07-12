# storing values
tree1 = 98
tree2 = 45
tree3 = 67      
tree4 = 23
tree5 = 89

# finding the total of trees
sum = tree1 + tree2 + tree3 + tree4 + tree5
print("Total number of trees:", sum)

# finding the average of trees
average = sum / 5
print("Average number of trees:", average)

# activity 2

# taking total amount as input from user
amount =int(input("Enter the amount: "))

# calculating the number of different notes
note_1 = amount // 100
note_2 = (amount % 100) // 50
note_3 = (amount % 50) // 10

print("Number of 100 notes:", note_1)
print("Number of 50 notes:", note_2)
print("Number of 10 notes:", note_3)

# activity 3

# take marks as input from user

print("Enter marks for 5 subjects:")

math = int(input("Math: "))
english = int(input("English: "))
science = int(input("Science: "))
history = int(input("History: "))
geography = int(input("Geography: "))

# calulate the percentage of marks

sum = math + english + science + history + geography
percentage = (sum / 500) * 100

print(end="percentage: ")
print(percentage)