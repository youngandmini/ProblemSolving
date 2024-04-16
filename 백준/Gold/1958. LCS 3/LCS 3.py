import sys

str1 = list("0" + sys.stdin.readline().rstrip())
str2 = list("0" + sys.stdin.readline().rstrip())
str3 = list("0" + sys.stdin.readline().rstrip())

# # 2줄일때
# dp_table = [[0 for j in range(len(str2))] for i in range(len(str1))]
# max_length = 0
# for i in range(1, len(str1)):
#     for j in range(1, len(str2)):
#         dp_table[i][j] = max(dp_table[i][j-1], dp_table[i-1][j])
#         if str1[i] == str2[j]:
#             dp_table[i][j] = max(dp_table[i][j], dp_table[i-1][j-1]+1)
#             max_length = max(max_length, dp_table[i][j])
# print(max_length)

# 세줄일때
max_length = 0
dp_table = [[[0 for k in range(len(str3))] for j in range(len(str2))] for i in range(len(str1))]
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        for k in range(1, len(str3)):
            dp_table[i][j][k] = max(dp_table[i][j][k-1],
                                    dp_table[i][j-1][k],
                                    dp_table[i-1][j][k])
            if str1[i] == str2[j] == str3[k]:
                dp_table[i][j][k] = max(dp_table[i][j][k], dp_table[i - 1][j - 1][k-1] + 1)
                max_length = max(max_length, dp_table[i][j][k])
print(max_length)