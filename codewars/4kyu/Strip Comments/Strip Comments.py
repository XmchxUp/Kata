def strip_comments(strng, markers):
    res = ""
    def remove_comment(s: str):
        idx = -1
        for m in markers:
            tmp = s.find(m)
            if tmp != -1:
                if idx == -1:
                    idx = tmp
                else:
                    idx = min(idx, tmp)
        if idx == -1:
            return s.rstrip()
        return s[:idx].rstrip()
                

    for line in strng.split("\n"):
        res += remove_comment(line) + "\n"
    
    return res[:-1]