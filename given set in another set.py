"""
 Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
"""
# Read the first set of values from input
set1 = set(map(int, input("Enter the first set of values: ").split()))

# Read the second set of values from input
set2 = set(map(int, input("Enter the second set of values: ").split()))

# Update the first set with the second set
set1.update(set2)

# Print the updated set values space-separated
print(" ".join(map(str, sorted(set1))))
"""
