num = 777777
left = 0
right = 0
count = 6

num_s = str(num)
for i in num_s:
    if count > 3:
        right += int(i)
        count -= 1
    else:
        left += int(i)
        count -= 1

if left == right:
    print('Yes')
else:
    print('No')
