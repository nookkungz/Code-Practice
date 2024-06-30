n = [int(n) for n in input().split()]
a = str(input())
n.sort()
dic = {
    "A" : n[0],
    "B" : n[1],
    "C" : n[2]
}
output = [dic[char] for char in a]
for i in output: print(i , end=" ")