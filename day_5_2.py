file_path = 'inputs/day_5.txt'

l = []
with open(file_path, 'r') as f:
    line = f.readline()
    while line[1] != '1':
        l.append([x for x in line])
        line = f.readline()
    crates = [[x[4*j + 1] for x in l if x[4*j + 1] not in [' ', '[', ']']] for j in range(9)]
    f.readline()
    for i in f.readlines():
        qty, _, from_, _, to = i[5:].rstrip().split(' ')
        for j in range(int(qty), 0, -1):
            crates[int(to) - 1].insert(0, crates[int(from_) - 1][j-1])                                                               
            crates[int(from_) - 1].pop(j-1)

print(''.join([i[0] for i in crates]))