file = open('sums.txt')
for line in file:
    print(sum([int(a) for a in line.split()]))
file.close()
