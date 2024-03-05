t = (27, 12, 29, 13, 19, 18, 20, 24, 20, 84, 93, 82, 94, 95, 12)

print(t.count(12))

print(t.index(19))

for i in t:
    print(i, end=' ')

t1 = (1, 2, 4, 6)
t2 = (12, 19, 20, 31)

t3 = t1 + t2
print('\n',t3)

print(18 in t)
print(100 not in t)

print(t[5:10])

print(len(t))