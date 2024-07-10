row1 = ["?","?","?"]
row2 = ["?","?","?"]
row3 = ["?","?","?"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Example: 21 for Column 2 Row 1\n")

pos1 = int(position[0])-1
pos2 = int(position[1])-1

map[pos1][pos2] = "X"

print(f"{row1}\n{row2}\n{row3}")