a = {1,2,4,7.13,'name',"",4.987}
print(a)
a.add(10)
print(a)
b = ("dhyey",2)
a.add(b)
print(a)
a.add(7.13)
print(a)

b = {1,2,3,0,4,5,8,9}
b.pop()
print(b)
c ={1,2,3,5,8,0.5,44}
print(b.difference(c))
print(c.difference(c))
print(c.difference(b))

print(b.intersection(c))
print(c & b)
print(b.symmetric_difference(c))

# p = frozenset([1,2,3,4])
# print(1 in p)
# print('hello' in p)

p = {1,2,3}
q = {4,5,6,1}
print(p.isdisjoint(q))

v = {1,2,3,4,5,6}
u = {1,2,3}
w = {4,5,6,7,8}
print(u.issubset(v))
print(v.issuperset(u))
print(v.union(u).union(w))