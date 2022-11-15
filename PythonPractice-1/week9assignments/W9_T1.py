#W9_T1

Items = [1000,500,100]

print("Handling \"Items\" list:")
print("Current items: ")

for x in range(len(Items)):
    print(" - "+str(Items[x]))

last_item = float(input("\nGive a number:"))

Items.append(last_item)

print(" Current items: ")
for x in range(len(Items)):
    print(" - "+str(Items[x]))

Items.sort()


print("\nCurrent items: ")
for x in range(len(Items)):
    print(" - "+str(Items[x]))

print("\nThank you for using the program.")
