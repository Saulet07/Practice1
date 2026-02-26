import json

J = json.loads(input().strip())
q = int(input())

for _ in range(q):
    s = input().strip()

    cur = J
    i = 0
    ok = True

    while i < len(s):
        if s[i] == '.':
            i += 1

        key = ""
        while i < len(s) and s[i] not in ".[":
            key += s[i]
            i += 1

        if key:
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                ok = False
                break

        if i < len(s) and s[i] == '[':
            i += 1
            num = ""
            while s[i] != ']':
                num += s[i]
                i += 1
            i += 1

            idx = int(num)
            if isinstance(cur, list) and 0 <= idx < len(cur):
                cur = cur[idx]
            else:
                ok = False
                break

    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")