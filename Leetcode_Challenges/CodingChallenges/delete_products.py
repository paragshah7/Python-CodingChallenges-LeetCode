def delete_products(ids, m):
    countMap = {}
    size = 0 
    count = 0

    for i in ids:
      if i in countMap.keys():
        countMap[i] +=1
      else:
        countMap[i] = 1
        size += 1
    print(countMap)

    for key, value in countMap.items():
      if key <= m:
        m -= key
        count += 1
      else:
        return size - count - 1

    return size - count + 1


print(delete_products([1,1,1,1], 2))