#part 1

f = open('input.txt', 'r')

max = 0

temp_sum = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        if line == "" or line == '\n':
            if temp_sum > max:
                max = temp_sum
            temp_sum = 0
        else:
            temp_sum += int(line)

print(max)

#part 2

f = open('input.txt', 'r')

max1 = 0

max2 = 0

max3 = 0

temp_sum = 0

with open('input.txt', 'r') as f:
    for line in f.readlines():
        if line == "" or line == '\n':
            if temp_sum > max1:
                max3 = max2
                max2 = max1
                max1 = temp_sum
            elif temp_sum > max2:
                max3 = max2
                max2 = temp_sum
            elif temp_sum > max3:
                max3 = temp_sum
            temp_sum = 0
        else:
            temp_sum += int(line)

print(max1 + max2 + max3)