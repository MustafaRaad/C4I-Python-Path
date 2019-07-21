def Join(string):
    return str(" ".join(string))


def count_character(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index: index + len(target)] == target:
            total += 1
        index += 1
    return total

test = ['R', 'A', 'M', 'D', 'A', 'N', 'K', 'A', 'R', 'E', 'E', 'M']
test1 = Join(test)
# print(test1)
# print(count_character(test1, 'A')) ######Or test1.find('A')
# print (test1.replace('M','N'))
# print (test1.replace('E',''))
