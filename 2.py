a = set()
b = set()

n = int(input("tool majmoe n ra vared konid :"))
for i in range(n):
    a1 = int(input("entr the number: "))
    a.add(a1)

m = int(input("tool majmoe m ra vared konid :"))
for j in range(m):
    b1 = int(input("entr the number: "))
    b.add(b1)

j = a.union(b)
print(j)
l = a.intersection(b)
print(l)
