x = [1,2,3,0,'a','dhyey7',1.7,0,1,2,1,True]
print(x)

x.append(4)
print(x)

# x.clear()
# print(x)

# x.copy()
# print(x)

y = x.count(1)
z = x.count(2)
p = x.count(0)
print(y,z,p)

cars = ['Bmw','maruti']
more_cars =['tata']
print(cars)
# cars.append(more_cars)
# print(cars)
cars.extend(more_cars)
print(cars)

# # list of animals
# Animals= ["cat", "dog", "tiger",'hhhh']
# # searching positiion of dog
# print(Animals.index("hhhh"))

# a =[1,2,3,5,7]
# # print(a.index(7))
# # print(a.index(2,0,3))

a =[1,2,3,5,7,1,2]
a.insert(3,15)
print(a)

b = [3,5,7,14,9]
print(b)
b.pop(2)
print(b)

c = [1,2,3,34,5,5,1,3,2]
print(c)
c.remove(34)
print(c)
c.remove(1)
print(c)

c.reverse()
print(c)

d = [1,5,2,6,3,8,4]
d.sort(reverse=True)
print(d)