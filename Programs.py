# # Local and Global Variables

# x=50
# def display():
#     x=100
#     print("Local x:",x)
# display()
# print("Global x:",x)

# # Function Composition

# def square(x):
#     return x*x
# def double(x):
#     return x*2
# num=int(input("Enter a number: "))
# result=double(square(num))
# print("Result:",result)

# # Search element in a list

# nums=[10,20,30,40,50]
# key=int(input("Enter a number to search: "))
# if key in nums:
#     print("Element found")
# else:
#     print("Element not found")

# # Sort a list of numbers

# num = [5, 2, 9, 1, 5, 6]
# num.sort()
# print("Sorted list:", num)

# # Remove duplicates from a list

# nums = [1, 2, 3, 2, 4, 1, 5]
# nums = list(set(nums))
# print("List after removing duplicates:", nums)

# # Arithematic Operations on two numbers

# a=float(input("Enter first number: "))
# b=float(input("Enter second number: "))
# print("Addition:",a+b)
# print("Subtraction:",a-b)
# print("Multiplication:",a*b)
# print("Modulus:",a%b)
# print("Division:",a/b)

# # Solutioon to detremine if a number is prime or not

# n=int(input("Enter a number: "))
# if n<=1:
#     print(n,"is not a prime number")
# else:
#     for i in range(2,int(n/2)+1):
#         if n%i==0:
#             print(n,"is not a prime number")
#             break
#     else:
#         print(n,"is a prime number")

# # Palindrome check

# n=int(input("Enter a number: "))
# org=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if org==rev:
#     print(org,"is a palindrome")
# else:
#     print(org,"is not a palindrome")

# # Prgm to accept n elements in a list and display the avg largest and smallest number in the list

# n=int(input("Enter the number of elements: "))
# nums=[]
# for i in range(n):
#     val=int(input("Enter element: "))
#     nums.append(val)
# print("List:", nums)
# print("Sum:", sum(nums))
# print("Average:", sum(nums)/n)
# print("Largest:", max(nums))
# print("Smallest:", min(nums))  

# # Insertion Delection Sort and Reverse of a list

# num=[5, 2, 9, 1, 5, 6]
# print("Original list:", num)
# num.append(60)
# print("List after insertion:", num)
# num.remove(2)
# print("List after deletion:", num)
# num.sort()
# print("List after sorting:", num)
# num.reverse()
# print("List after reversing:", num)


# # Perform division and handle division by zero error

# a= float(input("Enter numerator: "))
# b= float(input("Enter denominator: "))
# try:
#     result=a/b
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Denominator cannot be zero.")

# Accept an Integer and handle ValueError 

# try:
#     num = int(input("Enter an integer: "))
#     print("You entered:", num)
# except ValueError:
#     print("Error: Please enter a valid integer.")

# # Prgm to demonstrate try,except and finally block

# try :
#     a= int(input("Enter first number: "))
#     b= int(input("Enter second number: "))
#     result=a/b
# except valueError:
#     print("Error: Please enter valid integers.")
# except ZeroDivisionError:
#     print("Error: Denominator cannot be zero.")
# else:
#     print("Result:", result)
# finally:
#     print("Execution completed.")