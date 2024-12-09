left_list = []
right_list = []


with open('input.txt') as f:
    for line in f:
        line = line.split()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))


left_list.sort()
right_list.sort()


total_distance = 0

for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(total_distance)   