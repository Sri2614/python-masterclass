# Sets - Unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife","spoon"}

dishes = {"bowl","plate","cup","knife"}

# utensils.add("vessel")
# utensils.remove("knife")
# utensils.clear()

# utensils.update(dishes)
# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)

print(dishes.difference(utensils))

print(dishes.intersection(utensils))