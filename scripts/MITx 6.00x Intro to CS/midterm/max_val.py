def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    provisional = []

    def flatten(target):
        for element in target:
            if type(element) == int:
                provisional.append(element)
            else:
                flatten(element)
        return provisional

    return(max(flatten(t)))


trial = [[2,5], 3, (6,9), [1,2,[3,4],4]]
print(max_val(trial))
