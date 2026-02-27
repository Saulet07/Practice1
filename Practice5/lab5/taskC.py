import re
s = input()
p = input()
text = re.findall(re.escape(p), s)
print(len(text))