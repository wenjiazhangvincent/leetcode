
lst = range(22)
for i in xrange(len(lst)):
    lst[i] += 1
    if lst[i] < 10:
        lst[i] = '0' + str(lst[i])
    else:
        lst[i] = str(lst[i])
print lst