def count_words(text):
    import string
    '''
    Function count_words count words separeted by space in string object
    INPUT:string object
    OUTPUT:number of words
    '''
    if len(text)==0:
        return 0
    if text.count(" ")==0 and len(text)>0:
        return 1
    for i in string.ascii_letters:
        if i in text:
            return text.count(" ") + 1
    for i in string.digits:
        if i in text:
            return text.count(" ") + 1
    return 0
    return text.count(" ")+1

st="M1 Pro takes the exceptional performance of the M1 architecture to a whole new level for pro users. Even the most ambitious projects are easily handled with up to 10 CPU cores, up to 16 GPU cores, a 16‑core Neural Engine, and dedicated encode and decode media engines that support H.264, HEVC, and ProRes codecs."

print(count_words(st))