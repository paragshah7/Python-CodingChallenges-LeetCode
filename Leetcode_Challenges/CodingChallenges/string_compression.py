word = "abbcccb"
k = 2
flag = 0
subString = "acb"

while len(word) >= k:
    print('***********', word)
    start = 0
    for w in range(len(word)):
        sub = word[start:start + k]
        if len(sub) == k and sub == len(sub) * sub[0]:
            word = word.replace(sub, '')
            break
        start += 1
    else:
        flag = 1
    if flag == 1:
        break
print(word)
