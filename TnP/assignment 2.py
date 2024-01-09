'''
Q1.Write a program in Python to input 5 numbers from keyboard and find their sum and
average.
Test Data
Input the 5 numbers: 1 2 3 4 5
Expected Output:
Input the 5 numbers:
1
2
3
4
5
The sum of 5 no is : 15
The Average is : 3                   
'''
print("Enter 5 numbers")
i=Sum=avg=0
nums=[]
for i in range(6):
   nums.insert(i, int(input()))
   Sum=sum(nums)
   i=i+1
   
print("Sum is :",Sum)

print("avg is :", Sum/5)
    
'''

Q2. Write a program in Python to print the Floyd&#39;s Triangle.
Test Data
Input number of rows: 5
Expected Output:
Input number of rows: 5
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''

rows = int(input("Enter the number of rows for Floyd's Triangle: "))
number = 1
for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(number, end=" ")
            number += 1
        print()
        
        
'''
Q3. Write a program in Python to display the pattern like a diamond.
'''

rows = int(input("Enter the number of rows for the diamond: "))
for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(1, 2 * i):
            print("*", end="")
        print()



'''
Q4. Write a Python program that reads an integer and check whether it is negative, zero, or positive.
'''

number = int(input("Enter an integer: "))
if number < 0:
    print("number is a negative number.")
elif number == 0:
    print("number is zero.")
else:
    print("number is a positive number.")

'''
Q5. Write a Python program that reads a positive integer and count the number of digits the number has.
'''
number = int(input("Enter a positive integer: "))
if number <= 0:
    print("Please enter a positive integer.")
else:
    num_str = str(number)
    num_digits = len(num_str)
    print(f"The number {number} has {num_digits} digit(s)")

'''
Q6. Write a Python program that accepts three numbers and prints "All numbers are equal" if all three numbers are equal, "All numbers are different" if all three numbers are different and "Neither all are equal or different" otherwise.
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 != num2 and num2 != num3 and num1 != num3:
    print("All numbers are different.")
else:
    print("Neither all are equal nor different.")

'''
Q7. Write a program that accepts three numbers from the user and prints "increasing" if the numbers are in increasing order, "decreasing" if the numbers are in decreasing order, and "Neither increasing nor decreasing order" otherwise.
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 < num2 < num3:
    print("Increasing order.")
elif num1 > num2 > num3:
    print("Decreasing order.")
else:
    print("Neither increasing nor decreasing order.")


'''
Q8. Write a Python program to check given Number is Strong Number or not.
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def is_strong_number(number):
    num_str = str(number)
    sum_of_factorials = sum(factorial(int(digit)) for digit in num_str)
    return sum_of_factorials == number
num = int(input("Enter a number to check if it's a strong number: "))
if is_strong_number(num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")


'''
Q9. Write a Python program to check given Number is Armstrong Number or not.
'''

def count_digits(n):
    return len(str(n))
def is_armstrong_number(number):
    num_digits = count_digits(number)
    sum_of_powers = sum(int(digit) ** num_digits for digit in str(number))
    return sum_of_powers == number
num = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


'''
Q10. Write a Python program to check given Number is Palindrome or Not.
'''

def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
num = int(input("Enter a number to check if it's a palindrome: "))
if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")


'''
Q11. Write a Python program to print Fibonacci series
'''

def fibonacci_series(n):
    fib_series = [0,1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
        return fib_series
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("\nFibonacci Series:")
    series = fibonacci_series(num_terms)
    print(series)


'''
Q12. Write a Python program to print reverse Number.
'''

def reverse_number(number):
    num_str = str(number)
    reversed_num = int(num_str[::-1])
    return reversed_num
num = int(input("Enter a number to reverse: "))
reversed_num = reverse_number(num)
print(f"The reverse of {num} is: {reversed_num}")

'''
Q13. Write a Python program to find sum of all even numbers between 1 to n.
'''

def sum_of_even_numbers(n):
    sum_even = 0
    for num in range(2, n + 1, 2):
        sum_even += num
    return sum_even
n = int(input("Enter the value of n: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_even_numbers(n)
    print(f"The sum of even numbers between 1 and {n} is: {result}")

'''
Q14. Write a Python program to find first and last digit of a number.
'''

num = int(input("Enter any number : "))
number_str = str(num)
print("First digit of a number", number_str[0])
print("Last digit of a number", number_str[-1])


'''
Q15. Write a Python program to swap first and last digits of a number.
'''
num = int(input("Enter any number : "))
digits = 0
temp = num
while temp > 0:
    temp //= 10
    digits += 1
first_digit = num // 10**(digits-1)
last_digit = num % 10
middle_part = (num // 10) % (10**(digits - 2))
swapped_num = last_digit * 10**(digits - 1) + middle_part * 10 + first_digit
print(num)
print(swapped_num)


'''
Q16. Write a Python program to find all factors of a number.
'''

num = int(input("Enter any number : "))
for i in range(1,num+1):
    if num % i == 0:
        print(i)


'''
Q17. Write a Python program to find maximum between two numbers.
'''

first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
maximum_number = max(first_number, second_number)
print("Maximum of two Numbers:", maximum_number)


'''
Q18. Write a Python program to check whether a number is even or odd without using if else
'''
number = int(input("Enter Any Number: "))
result = "Even Number" * (number % 2 == 0) + "Odd Number" * (number % 2 != 0)
print(result)


'''
Q19. Write a Python program to swap two Numbers without using arithmetic operations and
'''

A = int(input("Enter A: "))
B = int(input("Enter B: "))
print("Before Swapping:")
print("A =", A, "B =", B)
(A, B) = (B, A)
print("After Swapping:")
print("A =", A, "B =", B)


'''
Q20. Write a Python program to print Following Pattern
'''

rows = int(input("Enter the rows: "))
current_char = ord('A')
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(current_char), end=" ")
        current_char += 1
    print()


  