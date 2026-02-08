s = input()

operation = ""

for ch in s:
    if ch == "+" or ch == "-" or ch == "*":
        operation = ch
        break

left_part = ""
right_part = ""
found = False

for ch in s:
    if ch == operation:
        found = True
        continue

    if not found:
        left_part += ch
    else:
        right_part += ch

left_number = ""

for i in range(0, len(left_part), 3):
    piece = left_part[i:i+3]

    if piece == "ZER":
        left_number += "0"
    elif piece == "ONE":
        left_number += "1"
    elif piece == "TWO":
        left_number += "2"
    elif piece == "THR":
        left_number += "3"
    elif piece == "FOU":
        left_number += "4"
    elif piece == "FIV":
        left_number += "5"
    elif piece == "SIX":
        left_number += "6"
    elif piece == "SEV":
        left_number += "7"
    elif piece == "EIG":
        left_number += "8"
    elif piece == "NIN":
        left_number += "9"

right_number = ""

for i in range(0, len(right_part), 3):
    piece = right_part[i:i+3]

    if piece == "ZER":
        right_number += "0"
    elif piece == "ONE":
        right_number += "1"
    elif piece == "TWO":
        right_number += "2"
    elif piece == "THR":
        right_number += "3"
    elif piece == "FOU":
        right_number += "4"
    elif piece == "FIV":
        right_number += "5"
    elif piece == "SIX":
        right_number += "6"
    elif piece == "SEV":
        right_number += "7"
    elif piece == "EIG":
        right_number += "8"
    elif piece == "NIN":
        right_number += "9"

a = int(left_number)
b = int(right_number)

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
else:
    result = a * b

result_str = str(result)
answer = ""

for digit in result_str:
    if digit == "0":
        answer += "ZER"
    elif digit == "1":
        answer += "ONE"
    elif digit == "2":
        answer += "TWO"
    elif digit == "3":
        answer += "THR"
    elif digit == "4":
        answer += "FOU"
    elif digit == "5":
        answer += "FIV"
    elif digit == "6":
        answer += "SIX"
    elif digit == "7":
        answer += "SEV"
    elif digit == "8":
        answer += "EIG"
    elif digit == "9":
        answer += "NIN"

print(answer)