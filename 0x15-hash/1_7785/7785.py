import sys
input = sys.stdin.readline
n = int(input())

dic = {}
for _ in range(n):
    line = list(input().split()) # ['Baha', 'enter']
    if line[1] == "enter": dic[line[0]] = 0
    elif line[1] == "leave": del dic[line[0]]

# 딕셔너리 키(이름)들을 가져와서 sorted() 함수로 정렬된 '새로운' 리스트 생성
# reverse=True로 알파벳 역순(내림차순) 정렬
sorted_list = sorted(dic.keys(), reverse=True)

for name in sorted_list:
    print(name)