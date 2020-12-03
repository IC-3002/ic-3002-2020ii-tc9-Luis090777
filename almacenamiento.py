def maximizar(As, D):
    As.sort(key=lambda x: x[1])
    total = 0
    res = []

    for x in range(len(As)):
        if total + As[i][1] <= D:
            res.append(As[x])
            total =  total + As[x][1]
        else:
            return  res
