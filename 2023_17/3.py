

counter = 0
min = 2**20
l = (11, 13, 17, 19)

for i in range(11000, 22000 + 1):
    #  first = True
    micro_counter = 0
    for j in l:
        if i % j == 0:
            micro_counter += 1

    if micro_counter == 2:
        if min > i:
            min = i
        counter += 1


print(counter, min)
