def keysWithValue(aDict, target):
    """
    aDict: a dictionary
    target: an integer

    RETURNS: a list of keys in aDict with the value target sorted
    in increasing order. (If aDict does not contain the value target,
    returns an empty list.)
    """
    ans = []
    if target not in aDict.values():
        return ans
    else:
        for key, value in aDict.items():
            if value == target:
                ans.append(key)
        ans = sorted(ans)
        return ans

dict = {88: 4, 2: 3, 4: 4, 6: 7}
print(keysWithValue(dict, 23))
