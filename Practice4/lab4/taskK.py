import json

s = json.loads(input())
p = json.loads(input())


for x in p:
    if p[x] is None:
        if x in s:
            del s[x]
    elif x in s and type(s[x]) == dict and type(p[x]) == dict:
        for y in p[x]:
            if p[x][y] is None:
                if y in s[x]:
                    del s[x][y]
            else:
                s[x][y] == p[x][y]
    else:
        s[x] = p[x]
print(json.dumps(s, sort_keys = True, separators = (',', ':')))