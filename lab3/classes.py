#ex1
class methods:
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s = input()
    def printstring(self):
        print(self.s.upper())
strmet = methods()
strmet.getstring()
strmet.printstring()

#ex2
class Shape(object):
     def __init__(self):
         pass
     def area(self):
         return 0
class Square(Shape):
     def __init__(self, length):
         Shape.__init__(self)
         self.length=length
     def area(self):
         return self.length*self.length
aSq= Square(4)
print(aSq.area())

#ex3
class Shape(object):
     def __init__(self):
         pass 
     def area(self):
         return 0
class rectangle(Shape):
    def __init__(self, length , width):
        Shape.__init__(self)
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
aSq= rectangle(4,7)
print(aSq.area())
    
#ex4
class point():
    def __init__(self, x, y):
        self.x= x
        self.y = y   
    def show(self):
        print(f'({self.x}, {self.y})')
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def dist(self , other):
        distance =((self.x - other.x)**2+(self.y-other.y)**2)**0.5
        return distance 
point1 = point(2, 3)
point2 = point(5, 7)
point1.show()
point1.move(8, 11)
print(point1.dist(point2))

#ex5
class account:
    def __init__(self , owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.balance=0
    def deposit(self,amount ):
        self.balance += amount
        print(f'{amount} deposited,new balance: {self.balance}')
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} withdrawn , new balance: {self.balance}')
        else:
            print('Withdrawal can not be processed.')
my_account = account("nka")
my_account.deposit(100)
my_account.withdraw(200)

#ex6
def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
numbers = input().split()
numbers = list(map(int, numbers)) 
prime_numbers = list(filter(lambda x: prime(x), numbers))
print( prime_numbers)

