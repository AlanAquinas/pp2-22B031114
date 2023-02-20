#----------------------------------- 1
import math

num = float(input())

print(math.radians(num))

#----------------------------------- 2
Height = float(input('Height: '))
wegth = float(input('Base, first value: '))
length = float(input('Base, second value: '))
trape = (wegth+length)*Height/2

print(trape)

#----------------------------------- 3

n = float(input('Input number of sides: '))
s = float(input('Input the length of a side: '))
area = (n * pow(s,2))/ 4 * math.tan(math.pi / n)

print(f"The area of the polygon is: {area}")

#----------------------------------- 4

l =float(input('Length of base: '))
h = float(input('Height of parallelogram: '))

print(f'Expected Output: {l*h}')