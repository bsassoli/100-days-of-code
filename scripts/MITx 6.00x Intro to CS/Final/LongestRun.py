def longestRun(L):
    start = 0
    end = len(L)
    list_answers = []
    for pos in range(start, end):
        begin = pos
        ans = [L[begin]]
        while begin +1 <= end -1:
            # print(f'starting at {begin}')
            # print(L[begin])
            # print(L[begin+1])
            # print(L[begin] <= L[begin+1])
            if L[begin] <= L[begin+1]:
                ans.append(L[begin+1])
                list_answers.append(ans)
                begin += 1
            else:
                break

    l = [len(item) for item in list_answers]
    if len(l) == 0:
        return 1
    else:
        indx = max(l)
        return indx


test = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
test2 = [[0]]
print(longestRun(test))
print(longestRun(test2))
