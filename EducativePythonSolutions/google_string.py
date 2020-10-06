# "{a,bb}{x,y}{1,2}" → ["ax1", "ax2", "ay1", "ay2", "bbx1", "bbx2", "bby1", "bby2"]

string = "{a,b}{x,y}{1,2}"
n = len(string)
temp = []
big_string = []

new_string = []
i = 0

# print(string[5:n])

# for i in range(len(string)):
while i < n:
    print(i)
    if string[i] == '{':
        temp = []
        i = i + 1
        while string[i] != '}':
            if string[i] == ',':
                i = i + 1
            else:
                temp.append(string[i])
                i = i + 1
    big_string.append(temp)
    i = i + 1

print(big_string)

j = 0
k = 0
m = len(big_string)

# while j < m:
#     print(j, k)
#     text = big_string[0][0] + big_string[1][0] + big_string[2][k]
#     k = k + 1
#     print(text)
#     j = j + 1

print(big_string[0][0] + big_string[1][0] + big_string[2][0])
print(big_string[0][0] + big_string[1][0] + big_string[2][1])
print(big_string[0][0] + big_string[1][1] + big_string[2][0])
print(big_string[0][0] + big_string[1][1] + big_string[2][1])
print(big_string[0][1] + big_string[1][0] + big_string[2][0])
print(big_string[0][1] + big_string[1][0] + big_string[2][1])
print(big_string[0][1] + big_string[1][1] + big_string[2][0])
print(big_string[0][1] + big_string[1][1] + big_string[2][1])

# while k < 2:
#     print(big_string[j][j] + big_string[j+1][j] + big_string[j+2][k])
#     k = k + 1
#     print(big_string[0][j] + big_string[1][j] + big_string[2][k])
#     k = 0

print(new_string)
