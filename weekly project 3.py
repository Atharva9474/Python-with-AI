# Find Most Repetitive Element in a List
# Simple beginner-friendly code

# Given list
L1 = [1, 2, 2, 3, 2, 3, 4, 5]

print("List:", L1)

# Count how many times each number appears
count_dict = {}

for number in L1:
    if number in count_dict:
        count_dict[number] = count_dict[number] + 1
    else:
        count_dict[number] = 1

print("Count of each number:", count_dict)

# Find the number with highest count
max_count = 0
most_repetitive = 0

for number, count in count_dict.items():
    if count > max_count:
        max_count = count
        most_repetitive = number

print("Most repetitive element:", most_repetitive)
print("It appears", max_count, "times")