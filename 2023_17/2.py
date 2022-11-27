

counter = 0
max = -1
min = 2**20

for i in range(5913, 11753 + 1):
    odd_5_11 = i % 5 == 0 and i % 11 == 0
    not_odd_7_10_13_22 = i % 7 != 0 and i % 10 != 0 and i % 13 != 0 and i % 22 != 0
    if odd_5_11 and not_odd_7_10_13_22:
        counter += 1

        if min > i:
            min = i


print(counter, min)
