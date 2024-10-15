"""
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
7) Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
"""
# Read the values in a single line
values = input("Enter the values separated by space: ").split()

# Create a set from the values to remove duplicates
unique_values = set(values)

# Print the number of unique elements
print(len(unique_values))
"""
