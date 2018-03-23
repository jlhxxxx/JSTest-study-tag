#! python3
# sortDict.py - sort a dict


def sortDict(dic, pos=1, *li):
    out = []
    if li != ():
        li = list(li[0])
        for e in li:
            if e in dic:
                out.append([e.upper(), dic[e]])
        return out
    else:
        for k, v in dic.items():
            out.append((k.upper(), v))
        return sorted(out, key=lambda e: e[pos], reverse=pos)
    
# dic = {
#     '严重的': 10,
#     '一般的': 17,
#     '轻微的': 15
#     }
# li = ['致命的', '严重的', '一般的', '轻微的']
# result = sortDict(dic, 1, li)

# dic2 = {'V20180103': 18, 'V20180101': 47, 'V20180102': 8}
# result2 = sortDict(dic2, 0)

print('done')