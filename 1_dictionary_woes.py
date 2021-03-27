

def fixup_case(vals):
    """
    Solution: Standardized the keys by lowering them and returning a new dictionary with key,value pair
    """
    if len(vals) == 0:
        return

    fixed = {}
    for key,value in vals.items():
        fixed[key.lower()] = value

    return fixed


if __name__ =='__main__':

    vals= {'ArhaM_RiZvI':1,
           'AHMED_khan':2,
           'Muhammad_Iqbal':3,
           'elon_musk':4}

    print(fixup_case(vals))