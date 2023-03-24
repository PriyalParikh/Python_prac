def permutation(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return[list]
    else:
        l=[]
        for i in range(len(list)):
            a=list[i]
            b=list[:i] + list[i+1:]
            for j in permutation(b):
                l.append([a]+j)
        return l
data=list("123")
for p in permutation(data):
    print(p)