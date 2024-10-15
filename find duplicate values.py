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

# Read the values in a single line
values = list(map(int, input().split()))

# Count duplicates
duplicates_count = len(values) - len(set(values))

# Create a set to get unique values
unique_values = set(values)

# Print the number of duplicate values
print(f"Duplicate Values: {duplicates_count}")

# Print the unique values space-separated
print(" ".join(map(str, sorted(unique_values))))
"""
