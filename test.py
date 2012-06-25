print'Lab 05'
print

print'Problem 1'
print'--------------------------- 1a -------------------------------'
print

def do(thing):
    return str(thing) + str(1)

x = do(5)
print x

print'This function captures any input as a string and concatenates'
print'it with 1. That is d(5) gives 51'


print
print'--------------------------- 1b -------------------------------'
print

def do(one, two = 5):
    return one + two

x = do(5)
print x

print'This function outputs 10, although only one argument was provided,'
print'the parameter two has a default value of 5'


print
print'--------------------------- 1c -------------------------------'
print

print"The function outputs 25 after executing 'do(inp, 5)' and 8 after executing 'print inp'" 


print
print'--------------------------- 1d -------------------------------'
print

print"This function appends 'four' to the end of the list, that is: "

def try_to_change_list_contents(the_list):
    the_list.append('four')

outer_list = ['one', 'two', 'three']
try_to_change_list_contents(outer_list)
print outer_list


print
print'--------------------------- 1e -------------------------------'
print

print"The function ouputs 72 for 'print do(6, inp)  "
print
print

print'Problem 2'
print
print'--------------------------- 2 -------------------------------'
print


def factorial(number):
    output = 1
    for i in range(1,number + 1):
        output *= i
    print 'the factorial of',number,'is',output
        
factorial(5)


print
print'--------------------------- 3 -------------------------------'
print

def fibonacci(n):
    fibo_list = [0,1]
    for i in range(1,n+1):
        fibo_list.append(fibo_list[i] + fibo_list[i-1])
    fibo_list.remove(0)
    if n == 1:
        fibo_list.remove(fibo_list[0])
    if n >= 2:
        fibo_list.remove(fibo_list[n])
    print fibo_list

fibonacci(15)

print
print'--------------------------- 4 -------------------------------'
print

def prime(n):
    factor_count = 0
    prime_count = 0

    for i in range(1, n+1):
        if n % i == 0:
            factor_count += 1
    if factor_count == 2:
        print'True'
    else:
        print'False'
            

print
print'Challenge Problem'
print'--------------------------- 4 -------------------------------'
print

def isPalindrome(phrase):
    n = len(phrase)
    found = True
    for i in range(len(phrase)):

        if (phrase[i]).lower() != (phrase[n-1]).lower():
            found =False
        n -=1
    if found == True:
        print '"',phrase,'"', 'is a Palindrome'
    else:
        print '"',phrase,'"' 'not a palindrome'
        

isPalindrome('This is kofi')
isPalindrome('madam')
        

print
print'--------------------------- 5 -------------------------------'
print

def str_compare(str1, str2):
    if len(str1)<= len(str2):
        if ((str2.find(str1))>=0 and (str2.rfind(str1))<=len(str1)):
            print 'found'
        else:
            print'not found'
    else:
        if ((str1.find(str2))>=0 and (str1.rfind(str2))<=len(str2)):
            print 'found'
        else:
            print'not found'
        
        

str_compare('mango','manmango')
str_compare('mango','kankango')
str_compare('mango','ango')
str_compare('mango','kango')
            

