input = '245182-790572'.split('-')
start = int(input[0])
end = int(input[1])
numbers = set()

#Part 1
for i in range(start, end):
    num = str(i)
    if num[0] <= num[1] <= num[2] <= num[3] <= num[4] <= num[5]:
        if not num[0] < num[1] < num[2] < num[3] < num[4] < num[5]:
            numbers.add(num)

print("There are " + str(len(numbers)) + " possible passwords.")

#Part 2
good = set()
for i in numbers:
    chars = {}
    num = str(i)
    for n in num:
        if chars.get(n):
            chars[n] += 1
        else:
            chars[n] = 1
    
    for key in chars:
        if chars[key] == 2:
            good.add(num)

print("There are " + str(len(good)) + " passwords that meet the second criteria")

