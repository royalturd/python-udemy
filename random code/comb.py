combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

# output  --   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]