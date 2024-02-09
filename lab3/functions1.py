#ex1
def GramsToOunces(grams):
    ounces = 28.3495231*grams
    return ounces

gramsValue= float(input())
ouncesValue= GramsToOunces(gramsValue)
print(ouncesValue)

#ex2
def FarToCel(far):
    cel = (5/9)*(far-32)
    return cel

farValue= float(input())
celValue= int(FarToCel(farValue))
print(celValue)

#ex3
def solve(numheads, numlegs):
    numChickens=0
    numRabbits=0
    for numChickens in range(numheads + 1):
        numRabbits = numheads-numChickens
        if(4* numRabbits + 2*numChickens) == numlegs:
            return numRabbits, numChickens
    return "No solution"

numheads=35
numlegs=94
print("Number of rabbits and chickens: ",solve(numheads, numlegs) )

#ex4
def is_prime(num):

    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
numbers = list(map(int,input().split()))
print(filter_prime(numbers))

#ex5
from itertools import permutations
def print_permutations(str):
    perms = permutations(str)
    for perm in perms:
        print(''.join(perm))
user_input = input()
print_permutations(user_input)

#ex6
def reverseSentences(sentence):
    words = sentence.split()
    reversedSentences =''.join(reversed(words))
    return reversedSentences
userInput = input("Write a sentence: ")
reversedResult=reverseSentences(userInput)
print("Reversed sentence:  ",reversedResult )

#ex7
def has_33(nums):
    for i in range(len(nums) -1):
        if nums[i]== 3 and nums[i+1] == 3:
            return True
    return False
num1= [1,3,3]
num2=[1,3,1,3]
num3=[3,1,3]
print(has_33(num1))
print(has_33(num2))
print(has_33(num3))

#ex8
def spy_game(nums):
    t=False
    for i in range(len(nums)-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]:
            t= True
            break
        else:
            continue
        print(t)
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])

#ex9
def volumeSphere(radius):
    volume=(4/3)*3.14*(radius**3)
    return volume

r=float(input())
volumeResult= volumeSphere(r)
print(float(volumeResult))

#ex10
def newlist(mylist):
    unique = []
    for i in range(len(mylist)):
        unique.append(mylist[i])
    print(unique)
mylist = [1,1,12,2]
newlist(mylist)

#ex11
def palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
word = input()
if palindrome(word):
    print("is a palindrome!")
else:
    print("is NOT a palindrome.")

#ex12
def histogram(nums):
    for i in nums:
        print( "*" * i)       
inputnums = input()
nums_list = [int(num) for num in inputnums.split()]
histogram(nums_list)

#ex13
import random
def guess():
    print("Hello! What is your name?")
    b = input()
    d = random.randint(1,20)
    print(f'Well, {b}, I am thinking of a number between 1 and 20.\nTake a guess.')
    c = int(input())
    i=1
    while c != d:
        if c<d:
            print('Your guess is too low.\nTake a guess.')
        else:
            print('Your guess is too high.\nTake a guess.')
        i+=1
        c = int(input())
    print(f'Good job, {b} You guessed my number in {i} guesses!')
guess()

#ex14
from functions1 import guess
guess()