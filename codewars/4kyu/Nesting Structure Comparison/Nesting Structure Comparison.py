def same_structure_as(original,other):
    a, b = isinstance(original, list), isinstance(other, list)
    if not a and not b:
        return True
    elif (not a) or (not b):
        return False
    elif len(original) != len(other):
        return False
    
    for i in range(len(original)):
        if not same_structure_as(original[i], other[i]):
            return False
    return True
            