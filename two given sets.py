"""
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
"""
# Read the first set of values
set1 = set(map(int, input("Enter the first set of values: ").split()))

# Read the second set of values
set2 = set(map(int, input("Enter the second set of values: ").split()))

# Calculate the symmetric difference between the two sets
different_values = set1.symmetric_difference(set2)

# Print the different values space-separated
print(" ".join(map(str, sorted(different_values))))
"""
