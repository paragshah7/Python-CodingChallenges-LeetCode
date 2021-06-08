def makingAnagrams(s1, s2):
    # for i in s1:
    #     if i in s2:
    #         s1 = s1.replace(i,"",1)
    #         s2 = s2.replace(i,"",1)
    # return len(s1)+len(s2)
    k = [c for c in s1]
    l = list()
    for i in s2:
        if i in k:
            k.remove(i)
        else:
            l.append(i)

    return len(k) + len(l)


print(makingAnagrams('rather', 'harder'))
print(makingAnagrams('apple', 'pear'))