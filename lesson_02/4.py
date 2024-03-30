a = 2
b = 2
c = 2

# answer = 'no'
# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         if i * j == c:
#             answer = 'yes'
#             break
#
# print(answer)

if c < a * b and (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")

