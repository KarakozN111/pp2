#ex1
import math
def DegreeRadians(deg):
    rad= deg*(math.pi/180)
    return rad
deg= float(input())
result=(DegreeRadians(deg))
roundedResult= round(result, 6)
print(roundedResult) 

#ex2
def areaTrapezoid(h,b1,b2):
    area=(1/2)*(b1+b2)*h
    return area
h= (input())
b1=(input())
b2=(input())
result= areaTrapezoid(h,b1,b2)
print(result)

#ex3
import math
def areaRegularPolygon(sides, length):
    apothem= length/(2*math.tan(math.pi/sides))
    perimetr= sides* length
    area= (1/2)*perimetr* apothem
    return area
sides=int(input())
length= float(input())
result= int(areaRegularPolygon(sides, length))
print(result)

#ex4
def areaParallelogram(lengthbase, height):
    area= lengthbase*height
    return area
lengthbase=float(input())
height= float(input())
result= areaParallelogram(lengthbase, height)
print(result)