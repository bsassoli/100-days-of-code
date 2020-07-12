def getSublists(L, n):
    ans = []
    start = 0
    end = start + n
    while end <= len(L):
        ans.append(L[start: end])
        start += 1
        end = start + n
    return ans


a = getSublists([1], 2)
print(a)
