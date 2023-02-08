# ----------------------------------------------------1
def gram_ounce(grams):
    return 28.3495231 * grams
# ----------------------------------------------------2
def f_c(f):
    c = (5 / 9) * (f-32)
    return c
# ----------------------------------------------------3
def solve(numheads, numlegs):
    chika, rabbit = numheads-1, 1
    while chika != 35:
        if (chika*2) + (rabbit*4) == numlegs:
            return chika, rabbit
        chika-=1
        rabbit+=1

# ----------------------------------------------------4
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

# ----------------------------------------------------5
def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp
def permutations(ch, curr_index=0):
    if curr_index == len(ch) - 1:
        print(''.join(ch))

    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        permutations(ch, curr_index + 1)
        swap(ch, curr_index, i)
# ----------------------------------------------------6
def reverse_sentence(sent):
    x = sent.split()
    x.reverse()
    print(x)
print(reverse_sentence("live to eat, and eat to live"))

# ----------------------------------------------------7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 2, 3, 4, 5, 6]))
print(has_33([3, 3, 2]))
print(has_33([2, 3, 3]))

# ----------------------------------------------------8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# ----------------------------------------------------9
def volume_of_sphere(r):
    return (4/3)*3.14*r*r*r
# ----------------------------------------------------10
def unique_elements(elements):
    x = []
    for i in range(len(elements)):
        if i not in x:
            x.append(i)
    return x
# ----------------------------------------------------11
def is_palindrome(word):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True
# ----------------------------------------------------12
def histogram(nums):
    for i in nums:
        for j in range(i):
            print("*")
        print(end = "\n")
# ----------------------------------------------------13
import random

def guess_the_number():
    n = random.randint(0, 22)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    guess = input()
    count_of_guess = 1
    while(guess != n):
        count_of_guess+=1
        if guess < n:
            input("Your guess is lower.")
        else:
            input("Your guess is bigger.")
    print(f"Good job, {name}! You guessed my number in {count_of_guess} guesses!")
    return 0









