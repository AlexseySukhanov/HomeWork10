def next_in_iterable(iter):
    import math

    '''
    Function findit search item in given iterable object
    INPUT:item to find, iterable object
    OUTPUT:position of searching item in iterable object, if item not exist returns -1
    '''
    if iter[-1]-iter[-2]==iter[-2]-iter[-3]:
        return linear(iter)
    if iter[-1]/iter[-2]==iter[-2]/iter[-3]:
        return multy(iter)
    if round(iter[-1]**(1/2))-1==round(iter[-2]**(1/2)):
        return sq(iter)
    if round(iter[-1]**(1/3))-1 == round(iter[-2]**(1/3)):
        return qube(iter)


def linear(iter):
    return iter[-1]+(iter[-1]-iter[-2])
def multy(iter):
    return int(iter[-1]*iter[-1]/iter[-2])
def sq(iter):
    return int((iter[-1]**(1/2)+1)**2)
def qube(iter):
    return int((iter[-1]**(1/3)+1)**3)


numbers=input("Input iterable: ").split(",")
numbers=[int(item) for item in numbers]
print(next_in_iterable(numbers))
