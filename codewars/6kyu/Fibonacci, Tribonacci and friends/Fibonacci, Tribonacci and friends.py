def Xbonacci(signature,n):
    #your code here
    if n == 0:
        return []
    s_len = len(signature)
    if n <= s_len:
        return signature[:n]
    res = list(signature)
    for i in range(s_len, n):
        elem = 0
        for k in range(0,s_len):
            elem += res[i-k-1]
        res.append(elem)
    return res