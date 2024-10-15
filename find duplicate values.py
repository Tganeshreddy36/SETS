"""
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
"""
# Read the number of values
n = int(input("Enter the number of values: "))

# Initialize an empty set to store the values
values_set = set()

# Read n values and add them to the set
for _ in range(n):
    value = int(input())
    values_set.add(value)

# Convert the set to a sorted list
sorted_values = sorted(values_set)

# Print the values space-separated
print(" ".join(map(str, sorted_values)))
"""
