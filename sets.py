set1 = set(map(int, input("Enter elements of Set 1 seperated by space: ").split()))
set2 = set(map(int, input("Enter elements of Set 2 seperated by space: ").split()))

print("\nSet 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("\nUnion:", union_set)

# intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

#Difference
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)
print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)

#Symmetric difference
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference", symmetric_diff)