

counter = 0
min = 2**20
my_counter = 0

for i in range(2 * (10**10), (4 * (10**10)) + 1, 100000):
    odd_7_100000 = i % 7 == 0 and i % 100000 == 0
    not_odd_13_29_43_101 = i % 13 != 0 and i % 29 != 0 and i % 43 != 0 and i % 101 != 0

    if odd_7_100000 and not_odd_13_29_43_101:
        if counter % 1000 == 0:
            my_counter += 1
            print(i, my_counter, counter)
        counter += 1
        if min > i:
            min = i


print(counter, min)
