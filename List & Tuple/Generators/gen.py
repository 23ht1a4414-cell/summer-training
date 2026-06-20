'''
problem with list:
list =[1,2,3,4,5]
entire list is stored in memory
nums = [i for i in range (100000)]
python consumes:
high memory
slower


Generator:
products values one at a time only when it is needed saved memory


'''

#example:




'''
Genetors:
remembers the varbles
remembers line position
continue from the same place
#diff b/w return & yeild
return                    yield
ends the function       pauses the function
returns single value    will return multiple values
no state memory           remembers the state
'''
def test():
    return 1
x =test()
print(x)
#with yield
def test():
    yield 1
    yield 2
for i in test():
    print(i)
# for loop uses iter(),next()internally
#create a generator for even numbers
def even_numbers(limit):
    num = 2
    while num <= limit:
        yield num
        num +=2
x = even_numbers(10)
for i in x:
    print(i)
#write a program for fibonacci using generators 
def fibonacci(limit):
    a, b = 0, 1
    while a<=limit:
        yield a
        a, b = b, a + b
x = fibonacci(10)
for num in x:
    print(num)


