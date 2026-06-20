'''
Iterators:
gives one element at atime on demand

python refers iterators:
memory efficiency controlled access

Iterators:it is an object can be looped
1.list
2.tuple
3.set
4.dict
5.string

examples:
nums = [10,20,30,40]

for x in nums:
    print(x)

#syntax:
Iterable _object = [1,2,3,4]
it = iter(Iterable_object)
print(it)
'''
Iterable_object = [1,2,3,4]
it = iter(Iterable_object)
print(it)
print(next(it))
print(next(it))
'''
list
  |
iter()
  |
iterator

how loop in python works internally
iterators -->will be used internally
iter(),next()

nums = [1,2,3,4]
    p
    for x in nums:
    print(x)

    it = iter(nums)
    while True:
    try:
    x = next(it)
    print(x)
    execpt  stop iteration

'''
nums = [1,2,3,4]
it = iter(nums)
while True:
    try:
       x = next(it)
       print(x)
    except StopIteration:
        break   

    '''
nums = [2,3,4]
it = iter(nums)
print(next(it))
'''
name = "python"
it = iter(name)
print(it)

t =(1,2,3)
it = iter(t)
print(it)

d = {"a":10,"b":20}
it = iter(d)
print(next(it))


#No iterator
nums = [i for i in range (100000)]
#huge memory
#iterator approach
nums = [i for i in range (100000)]
#only the current element
#will be processed


#creating a custom iterator
#count
class count:
    #constructor
    def __init__(self,limit):
        self.num = 1
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
     if self.num >self.limit:
        raise StopIteration
     x = self.num
     self.num +=1
     return x
#object creation
c = count(5)
print(next(c))
'''
#create a custom iterator
#for even numbers
'''
class Evennumbers:
   #constructor method
      def __init__(self,limit):
        self.num = 2
        #max limit
        self.limit = limit
        #this method makes the object iterable
        #it returns the iteractor object itself
      def __iter__(self):
        return self
      # next value
      def __next__(self):
             if self.num >self.limit:
              raise StopIteration
             
             x = self.num
             self.num +=2
             return x
c = Evennumbers(5)
for i in c:
   print(i)
    
  