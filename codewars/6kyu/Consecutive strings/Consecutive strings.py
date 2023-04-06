def longest_consec(strarr, k):
    # your code
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    def generate_k_len_str(idx):
        res = ""
        for i in range(k):
            res += strarr[i+idx]
        return res

    lst = []
    for i in range(n-k+1):
        lst.append(generate_k_len_str(i))
    
    return sorted(lst, key=lambda s : len(s), reverse=True)[0]

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)