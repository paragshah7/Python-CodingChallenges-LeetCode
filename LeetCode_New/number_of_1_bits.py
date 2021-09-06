"""
If we have number n, then n&(n-1) will remove the rightmost in binary representation of n. For example if n = 10110100, then n & (n-1) = 10110100 & 10110011 = 10110000, where & means bitwize operation and. Very convinient, is it not? What we need to do now, just repeat this operation until we have n = 0 and count number of steps.

Complexity It is O(1) for sure, because we need to make no more than 32 operations here, but it is quite vague: all methods will be O(1), why this one is better than others? In fact it has complexity O(m), where m is number of 1-bits in our number. In average it will be 16 bits, so it is more like 16 operations, not 32 here, which gives us 2-times gain. Space complexity is O(1)

"""

def hammingWeight(n):
        ans = 0
        while n:
            n &= (n-1)
            ans += 1
        return ans

def hammingWeight_noBit(n):
    ans=0
    while n>0:
        if n%2 == 1:
            ans += 1
        n = n/2
    return ans


print(hammingWeight(5))
