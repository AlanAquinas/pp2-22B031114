#---------------------------------------------- 1
class cin_cout():
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
#---------------------------------------------- 2
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l = 0):
        Shape.__init__(self)
        self.length = l
    def area(self):
        return self.l * self.l

#leng = Square(5)
#print(Square.area(leng))
#---------------------------------------------- 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

#xRectangle = Rectangle(5, 2)
#print(aRectangle.area())
#---------------------------------------------- 4
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
#---------------------------------------------- 5
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    def deposit(self, dep):
        self.balance += dep
        print('Deposit accepted')
    def withdraw(self, wd):
        if self.balance > wd:
            self.balance -= wd
            print('Withdrawal accepted')
        else:
            print('Withdrawal unavailable')
    #acc0 = Account("Savos'kin TOP", 1000)
    #acct0.withdraw(500)
# ---------------------------------------------- 6
def isPrime(n):
    if n <= 1: return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def returnPrime(list):
    primes = []
    for l in list:
        if isPrime(l):
            primes.append(l)
    return primes













