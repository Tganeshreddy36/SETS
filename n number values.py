"""
Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
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
