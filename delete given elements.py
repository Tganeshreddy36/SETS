"""
 Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
"""
# Read the set values from input
set_values = set(map(int, input("Enter the set values separated by space: ").split()))

# Read the element to be deleted
element_to_delete = int(input("Enter the element to delete: "))

# Check if the element is in the set and delete it if present
if element_to_delete in set_values:
    set_values.remove(element_to_delete)
    # Print the updated set values space-separated
    print(" ".join(map(str, sorted(set_values))))
else:
    print("Given value is not present in the set list.")
"""
