

counter = 0
max = -1
for i in range(0, 13920 + 1):
    odd_17 = i % 17 == 0
    not_odd_7_15_18_34 = bool(i % 7) and bool(i % 15) and bool(i % 18) and bool(i % 34)
    if odd_17 and not_odd_7_15_18_34 and i > 10836:
        counter = counter + 1
        if max < i:
            max = i


print(counter, max)
