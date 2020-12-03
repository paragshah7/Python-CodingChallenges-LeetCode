def getNumber(binary):
    num = binary.val
    print(num)
    while binary.next:
        num = num * 2 + binary.next.val
        binary = binary.next
    return num


print(getNumber([7,1,0,1]))
