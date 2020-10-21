s = "aaabcbc"
t = "abc"

while t in s:
    if t in s:
        s = s.replace(t, '')

print(s)
