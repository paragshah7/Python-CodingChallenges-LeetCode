import sys


def get_pattern_matches(blobs, pattern):
    counter = 0
    totalCount = 0
    output = ''

    for i in range(len(blobs)):
        if pattern == '':
            counter = 0
            totalCount = 0
        elif pattern == blobs[i:i + len(pattern)]:
            counter += 1
            totalCount += 1

        if blobs[i] == '|':
            output += str(counter) + '|'
            counter = 0
    output += str(counter) + '|' + str(totalCount)

    return output


""" Inputs: 
;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
aa;aaaakjlhaa|aaadsaaa|easaaad|sa
bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32
"""

for line in sys.stdin:
    pattern = line.split(';')[0]
    blobs = line[len(pattern) + 1:]

    result = get_pattern_matches(blobs, pattern)
    print(result)

