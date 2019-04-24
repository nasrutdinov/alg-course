file_list = []
f = open('symbol.txt')
line = f.readline()
while line:
    line = f.readline()
    file_list.append(line)
f.close()


A_count = {}
for line in file_list:
    for char in line:
        if char in A_count:
            A_count[char] += 1
        else:
            A_count[char] = 1
print(A_count)
