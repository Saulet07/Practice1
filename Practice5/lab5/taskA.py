import re
s = input()
text = re.match("Hello", s)
if text:
    print("Yes")
else:
    print("No")