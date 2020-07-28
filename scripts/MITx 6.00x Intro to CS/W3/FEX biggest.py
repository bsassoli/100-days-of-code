def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    lendic = {k: len(v) for (k,v) in aDict.items()}
    return max(lendic, key=lendic.get)
