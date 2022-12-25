score = 0

#p1
with open('input.txt', 'r') as f:
    for line in f.readlines():
        words = line.split(" ")
        # print(words)
        if words[0] == "A":
            if words[1] == "X\n":
                score += 4
            elif words[1] == "Y\n":
                score += 8
            elif words[1] == "Z\n":
                score += 3
        elif words[0] == "B":
            if words[1] == "X\n":
                score += 1
            elif words[1] == "Y\n":
                score += 5
            elif words[1] == "Z\n":
                score += 9 
        elif words[0] == "C":
            if words[1] == "X\n":
                score += 7
            elif words[1] == "Y\n":
                score += 2
            elif words[1] == "Z\n":
                score += 6
print(score) 
            
# p2
with open('input.txt', 'r') as f:
    for line in f.readlines():
        words = line.split(" ")
        # print(words)
        if words[0] == "A":
            if words[1] == "X\n":
                score += 3
            elif words[1] == "Y\n":
                score += 4
            elif words[1] == "Z\n":
                score += 8
        elif words[0] == "B":
            if words[1] == "X\n":
                score += 1
            elif words[1] == "Y\n":
                score += 5
            elif words[1] == "Z\n":
                score += 9 
        elif words[0] == "C":
            if words[1] == "X\n":
                score += 2
            elif words[1] == "Y\n":
                score += 6
            elif words[1] == "Z\n":
                score += 7
print(score) 
