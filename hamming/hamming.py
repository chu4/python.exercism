def distance(t1, t2):
    dif=0
    for i in range(0,len(t1)):
        if t1[i] !=t2[i]:
            dif+=1
    return dif