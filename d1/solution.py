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

