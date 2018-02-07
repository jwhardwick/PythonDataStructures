def fibList(n, l=[]):
    if len(l) >= n:
        return l
    if l == [] or l == [1]:
        l.append(1)
    else:
        l.append(l[-2] + l[-1])
    return fibList(n,l)
