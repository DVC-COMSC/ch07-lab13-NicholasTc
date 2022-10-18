numbers = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

rnum = len(numbers)
cnum = len(numbers[0])

# ******************************
# Make your Code
# ******************************

cross_count = 0

for i in range(rnum):
    for j in range(cnum):
        if numbers[i][j] == 1:
            # check for it's neighbors
            try:
                if numbers[i + 1][j-1] == 1 and numbers[i + 1][j] == 1 and numbers[i + 1][j + 1] == 1 and numbers[i + 2][j] == 1:
                    cross_count += 1
            except IndexError:
                continue

print(cross_count)
        
