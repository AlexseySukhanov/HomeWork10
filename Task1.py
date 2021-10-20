def maxdig(*args):
    '''
    Function maxdig  returns maximum number from list of numbers given in input()
    INPUT:list of numbers
    OUTPUT:maximum number
    '''
    max=args[0]
    for item in args:
        if item>max:
            max=item
    return max

print(maxdig(1,23,34,45))