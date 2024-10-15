"""
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
"""
# Read the first set of values
set1 = set(map(int, input("Enter the first set of values: ").split()))

# Read the second set of values
set2 = set(map(int, input("Enter the second set of values: ").split()))

# Calculate the intersection between the two sets
common_values = set1.intersection(set2)

# Print the common values space-separated
print(" ".join(map(str, sorted(common_values))))
"""
