total = 0
for line in open('input'):
    digits = [d for d in line if d.isdigit()]
    num = digits[0] + digits[-1]
    total += int(num)
print(total)
