array = [ [1,2,3],[2,1,3], [4,3,6]]
sumOfAll = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        sumOfAll += array[i][j]

print(sumOfAll)