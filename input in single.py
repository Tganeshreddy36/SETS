"""
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
"""
# Read the values in a single line
values = input("Enter the values separated by space: ").split()

# Create a set from the values to remove duplicates
unique_values = set(map(int, values))

# Convert the set to a sorted list
sorted_values = sorted(unique_values)

# Print the sorted values space-separated
print(" ".join(map(str, sorted_values)))
"""
