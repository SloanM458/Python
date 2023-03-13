#1) Basic - Print all integers from 0 to 150.

for x in range(0,151):
    print(x)



# 2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range(5, 1001, 5):
    print(y)

# Tested to see if both methods work, they do! 
for y in range, if y % 5 = 0: print y
for y in range(5,1001):
    if y % 5==0:
        print(y)


# 3) Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print 
# "Coding" instead. If divisible by 10, print "Coding Dojo".


for num in range (1,101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)



# 4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
oddnum = 0

for odd in range(0,500000):
    if odd % 2 == 1:
        oddnum = oddnum + odd

print(oddnum)

    


# 5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for num in range (2018,0, -4):
    if num % 2 == 0:
        print(num)


# 6) Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop 
# should print 3, 6, 9 (on successive lines)

lowNum = 0
highNum = 13
mult = 2
for num in range (lowNum, highNum, mult):
    if num / mult:
        print(num)
