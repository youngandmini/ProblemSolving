import sys

address = sys.stdin.readline().rstrip()

# 2번 규칙 적용
address_zero_parsed = address.split(sep = "::")
address_parsed = address.split(sep = ":")
if len(address_zero_parsed) == 2:
    replaced = ""
    # 처음이나 끝이라면
    for i in range(len(address_zero_parsed)):
        if address_zero_parsed[i] == "":
            replaced = ("0000:" * (8 - len(address_parsed) + 2))
            # 끝이라면 추가작업
            if i == len(address_zero_parsed)-1:
                replaced = ":" + replaced[:-1]
            break
    # 중간이라면
    else:
        replaced = ":" + ("0000:" * (8 - len(address_parsed) + 1))
    address = address.replace("::", replaced)

# 1번 규칙 적용
address_parsed = address.split(sep = ":")
result = ""
for token in address_parsed:
    result += "0" * (4 - len(token))
    result += token
    result += ":"
print(result[:-1])