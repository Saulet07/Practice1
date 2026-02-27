import re
s = input()
if re.match("[A-Za-z].*\d$", s):
    print("Yes")
else:
    print("No")