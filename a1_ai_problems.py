# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

#Fibonacci Sequence 
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence 

assert fibonacci(2) == [0,1], "fb test 2"
assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "fb test 10"

#Palindrome Check
def palindrome(p):
    return True if p[::-1] == p else False

assert palindrome("I palindrome I") == False, "test 1"
assert palindrome("racecar") == True, "test 2"
assert palindrome("kayak") == True, "test 3"
assert palindrome("12321") == True, "test 4"

#Sum of Multiples
def sum_of_multiples(multiple, limit):
    sum = 0
    for i in range(multiple, limit):
        if i % multiple == 0:
            sum += i
    return sum

assert sum_of_multiples(3,13) == 30, "sum test 1"

print("passed")