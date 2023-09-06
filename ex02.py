array = [ ["B","A","N","A","N","A"],["H","I"]]
newArray = []
for i in range(len(array)):
    word = ""
    for j in range(len(array[i])):
        word += array[i][j]
    newArray.append(word)

print(newArray)

for i in range(3):
    print("I LOVE YOU")
    