a = [1,2,3,4,5,6,7,8,9,10]
b = [1,2,3,4,5]

print(a[:10])   # 10번째 index까지 출력된다.
print(a[1:])    # 1번째 index까지 제외하고 출력된다.
print(a[1:2])   # 1번째 index까지 제외되고, 2번째 index까지 출려된다. == 2번째 index만 출려된다.

# python list slicing 기본 규칙
# [n, m]
# n : n번째 index까지 제외됨을 나타낸다.
# m : m번째 index까지 포함됨을 나타낸다.
# ==> n+1 ~ m 까지 포함됨을 나타낸다.