import heapq
def top_3_words(text:str):
    counter = {}
    res = []
    i = 0
    n = len(text)
    while i < n and not (text[i].isalpha() or text[i] == "'"):
        i += 1
    j = i
    while i < n:
        if j < n and (text[j].isalpha() or text[j] == "'"):
            j += 1
        else:
            word = text[i:j].lower()
            if any(c.isalpha() for c in word):
                counter[word] = counter.get(word, 0) + 1
            i = j + 1

            while i < n and not (text[i].isalpha() or text[i] == "'"):
                i += 1
            j = i + 1
    if counter:
        max_q = []
        for k, v in counter.items():
            heapq.heappush(max_q, (-v, k))
        while max_q and len(res) != 3:
            res.append(heapq.heappop(max_q)[1])
    return res

# print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
# print(top_3_words("  //wont won't won't "))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))