#ex1
def square_generator(N):
    for i in range(1, N+1):
        yield i**2

N = int(input())
squares = square_generator(N)
for square in squares:
    print(square)

#ex2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i
n = int(input())
even_nums = even_numbers(n)
even_nums_str = ', '.join(map(str, even_nums))
print(even_nums_str)

#ex3
def div(n):
    for i in range(n + 1):
        if i%3==0 and i%4 == 0:
            yield i
n = int(input())
divisible_by_3_and_4 = div(n)
print( list(divisible_by_3_and_4))

#ex4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a = int(input('a: '))
b = int(input('b: '))
for square in squares(a, b):
    print(square)

#ex5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for num in countdown(n):
    print(num)
