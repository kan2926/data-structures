
def permuteRec(s, i, res, final_res):
    if i == len(s):
        final_res.append(','.join(res))
        return final_res
    res.append(s[i])
    permuteRec(s, i+1, res, final_res)
    res.pop()
    permuteRec(s, i+1, res, final_res)
    return final_res

def powerSet(s):
    s = sorted(s)
    res = []
    res = permuteRec(list(s), 0, [], res)
    return res

s = "cab"
res = powerSet(s)
print(res)
