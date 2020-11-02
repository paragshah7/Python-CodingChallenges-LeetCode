A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["lo","oo"]

# print(A)
# print(B)
C = []
D = set()

# for i in B:
#     # print(i)
#     for j in A:
#         if i not in j:
#             A.remove(j)
            # C.append(j)

for b in B:
    if len(b) > 1:
        if len(set(b)) != len(b):
            
            print(b.count('o'))
        else:
            C = C + list(b)
            D = set(C)
B = list(D) + B
print(B)

# for b in B:
#     for a in A:
#         if b not in a:
#             print(b)
#             A.remove(a)
#             print(A)
#
# print(A)
# D = set(C)
# print(D)



# for d in D:
#     for a in A:
#         if d not in a:
#             A.remove(a)
#
# print(A)
