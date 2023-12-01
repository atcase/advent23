words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = "123456789"
total = 0
for line in open('input'):
    # Find first
    while True:
        print(line)
        for idx, word in list(enumerate(words)) + list(enumerate(digits)):
            if line.startswith(word):
                first = idx + 1
                break
        else:
            line = line[1:]
            continue
        break
    # Find last
    while True:
        print(line)
        for idx, word in list(enumerate(words)) + list(enumerate(digits)):
            if line.endswith(word):
                last = idx + 1
                break
        else:
            line = line[:-1]
            continue
        break
    total += first * 10 + last
print(total)
