#string


x='frog'


print (x[3])



# list

x = ['pig', 'cow', 'horse']


print (x[1])


#tuple 

x = ('Kevin', 'Niklas', 'Jenny', 'Craig')

print(x[0])



#slicing - slice out substrings, sublists, subtuples using indexes

print(x[1:])

x = "computer"
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5])
print(x[-1])
print(x[-3:])
print(x[:-2])


#adding / concatenating


#string

x = "horse" + "string"
print(x)


#list 

y = ['pig', 'cow' ] + ['horse']
print(y)


#tuple 

z = ('Kevin', 'Niklas', 'Jenny' ) + ('Craig',)

print(z)


#multiplying

#multiply a sequence using *


#string

x = 'bug' * 3
print(x)


#list 

y = [8,5] * 3
print(y)


#tuple


z = (2, 4) * 3
print(z)


#checking membership


#string

x = 'bug'
print('u' in x)


#list 

y = ['pig', 'cow', 'horse']
print('cow' not in y)



#tuple

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print('Niklas' in z)


#iterating - iterating through them items in s sequence


#item

x = [7,8,3]
for item in x:
    print(item)



# index & item

y = [7,8,3]
for index, item in enumerate(y):
    print(index, item)




#count number of items in a sequence


#string
x = 'bug'
print(len(x))


# tuple

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(len(z))

#list 

y = ['pig', 'cow', 'horse']
print(len(y))


#minimum


#string
x = 'bug'
print(min(x))


#list
y = ['pig', 'cow', 'horse']
print(min(y))


#maximum

# string

x = "bug"
print(max(x))


# list

y = ['pig', 'cow', 'horse']
print(max(y))


# tuple

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(max(z))



#sum - find the sum of items in a sequence. Entire sequence must be numeric



#list


y = [2,5,8,12]
print(sum(y))
print(sum(y[-2:]))



# tuple

z = (50, 4, 7, 19)
print(sum(z))


#sorting - returns a new list of items in sorted order.
#Does not change the original list.


#string 

x = 'bug'
print(sorted(x))



#list 
y = ['pig', 'cow', 'horse']
print(sorted(y))



#tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z))


#sorting - sort by second letter


z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(z, key=lambda k: k[1]))


#count(item) - returns count of an item



#string
x = 'hippo'
print(x.count('p'))



#list
y = ['pig', 'cow', 'horse', 'cow']
print(y.count('cow'))


#tuple
z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.count('Kevin'))



#index(item)


#string 
x = 'hippo'
print(x.index('p'))


#list 

y = ['pig', 'cow', 'horse', 'cow']
print(y.index('cow'))


#tuple

z = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(z.index('Jenny'))



#unpacking


x = ['pig', 'cow', 'horse']
a,b,c = x
print(a,b,c)



#Lists
#general purposes
#Grow and shrink size as needed
#Sequence type
#Sortable


#constructors - creating a new list


x = list()
y = ['a', 25, 'dog', 8.43]
tuple1 = (10, 20)
z = list(tuple1)



#list comprehension 


a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i>4]
print(b)


#delete - delete a list or an item ina list 


x = [5,3,8,6]
del(x[1])
print(x)
del(x)

#append - append an item to a list

x = [5,3,8,6]
x.append(7)
print(x)


#extend - append a sequence to a list

x = [5,3,8,6]
y = [12, 13]
x.extend(y)
print(x)

#insert - insert an item at a given index

x = [5,3,8,6]
x.insert(1,7)
print(x)
x.insert(1, ['a', 'm'])
print(x)


#pop - pops last item off list and returns item

x = [5,3,8,6]
x.pop()  #pop off 6
print(x)
print(x.pop())



#remove - remove first instance of an item


x = [5,3,8,6,3]
x.remove(3)
print(x)


#reverse

#reverse the order of the list. It is an in-place sort, meaning it changes the original list.

x = [5,3,8,6]
x.reverse()
print(x)


#sort - sort the list in place

x = [5,3,8,6] # doesnt return a new list.
x.sort()
print(x)


#reverse sort - sort items descending.

x = [5,3,8,6]

x.sort(reverse=True)
print(x)



#TUPLES


#immutable(cant add/ change)
#useful for fixed data
#Faster than lists
#sequence type



x = ()
x = (1,2,3)
x = 1,2,3
x = 2,
print(x, type(x))


list1 = [2,4,6]
x = tuple(list1)
print(x, type(x))



#tuples are immutable


x = (1,2,3)

#del(x[1])
#x[1] = 8


#Sets

#store non-duplicate items
#very fast access vs lists
#math set ops (union, intersect)
#sets are Unordered


#constructors

x = {3,5,3,5}
print(x)


y = set()
print(y)


list1 = [2,3,4]
z = set(list1)
print(z)



#set operations

x = {3,8,5}

print(x)
x.add(7)
print(x)


x.remove(3)
print(x)



# get length of set x


print(len(x))


#check membership in x


print(5 in x )

#pop random item from set x


print(x.pop(), x)


#delete all items from set x

x.clear()

print(x)



#Mathematical set operations

s1 = {1,2,3}
s2 = {3,4,5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)


#Dictionaries

#Key/Value pairs
#Associative arry, Like Java HashMap
#Dicts are Unordered




x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(x)
x = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])
print(x)
x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x)


#dict operations


x['shrimp'] = 38.2 #add or update
print(x)


#delete an item
del(x['shrimp'])
print(x)



#get length of dict x
print(len(x))


#delete all items from dict x
x.clear()
print(x)


#accessing keys and values in a dict

y = {'pork':25.3, "beef":33.8, "chicken":22.7}
print(y.keys())
print(y.values())
print(y.items()) # key-value pairs



# check membership in y_keys (only looks in keys, not values)

print('beef' in y)


# check membership in y_values

print('clams' in y.values())


#iterating a dict- note items are in random order

for key in y:
    print(key, y[key])


for k, v in y.items():
    print(k,v)




#Python List Comprehensions



import random


under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))



# get squared values


squares = [x**2 for x in under_10]
print('squares: ' + str(squares))


# get odd numbers using mod

odds = [x for x in range(10) if x%2 == 1 ]
print('odds: ' + str(odds))


#get multiples of 10


ten_x = [x* 10 for x in range(10)]
print('ten_x: ' + str(ten_x))


#get all numbers from a string

s = 'I love 2 go t0 the store 7 times a w3ek. '
nums = [x for x in s if x.isnumeric()]
print('nums: '+ ''.join(nums))


#get index of a list item
names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print('index = ' + str(idx[0]))


#delete an item from a list


letters = [x for x in 'ABCDEF' ]
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)




