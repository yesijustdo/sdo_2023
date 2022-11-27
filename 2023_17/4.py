
counter = 0
min = 2**20


for i in range(7525, 13486 + 1):
    odd_7 = i % 7 == 0
    not_odd_6_9_14_21 = i % 6 != 0 and i % 9 != 0 and i % 14 and i % 21 != 0

    if odd_7 and not_odd_6_9_14_21:
        counter += 1
        if min > i:
            min = i


print(counter, min)
