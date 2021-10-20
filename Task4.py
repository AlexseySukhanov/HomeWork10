def findit(item,*args):
    '''
    Function findit search item in given iterable object
    INPUT:item to find, iterable object
    OUTPUT:position of searching item in iterable object, if item not exist returns -1
    '''
    i=0
    for itm in args:
        if itm==item:
            return i
        i+=1
    return -1

print(findit(10,12,14,10,15))