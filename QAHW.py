# #1.  Program to find the average of numbers in a list
#
# numbers = [100, 250, 380, 430, 500]
#
# if len(numbers) > 0:
#     # Calculate the sum of the numbers
#     total_sum = sum(numbers)
#
#     # Find the count of numbers
#     count = len(numbers)
#
#     # Calculate the average
#     average = total_sum / count
#
#     print(f"The average of the numbers in the list is: {average}")
# else:
#     print("The list is empty, so the average cannot be calculated.")


# 2.
# Program to reverse a number
# number = int(input("Enter a number: "))
#
# # Initialize a variable to store the reversed number
# reversed_number = 0
#
# # Store the original number for reference
# original_number = number
#
# # Loop to reverse the number
# while number > 0:
#     digit = number % 10  # Get the last digit
#     reversed_number = reversed_number * 10 + digit  # Append the digit to reversed_number
#     number = number // 10  # Remove the last digit
#
# # Output the result
# print(f"The reverse of {original_number} is {reversed_number}")


#3.  Program to find the sum of the digits of a number

# # Input a number from the user
# number = int(input("Enter a number: "))
#
# sum_of_digits = 0
#
# original_number = number
#
#
# while number > 0:
#     digit = number % 10
#     sum_of_digits += digit
#     number = number // 10
#
# print(f"The sum of the digits of {original_number} is {sum_of_digits}")

# 4. Program to check if a number is a palindrome
# Input a number from the user
# number = int(input("Enter a number: "))
#
# # Store the original number for reference
# original_number = number
#
# # Initialize a variable to store the reversed number
# reversed_number = 0
#
# # Reverse the number
# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit  # Append the digit to reversed_number
#     number = number // 10  # Remove the last digit
#
# if original_number == reversed_number:
#     print(f"{original_number} is a palindrome.")
# else:
#     print(f"{original_number} is not a palindrome.")


#5. Program to count the number of digits in a number

# number = int(input("Enter a number: "))
# digit_count = 0
#
# number = abs(number)
#
#
# if number == 0:
#     digit_count = 1
# else:
#     while number > 0:
#         number = number // 10
#         digit_count += 1
#
# # Output the result
# print(f"The number of digits is: {digit_count}")

# # 6. Program to print the multiplication table of a given number
#
# # Input a number from the user
# number = int(input("Enter a number: "))
#
# # Input the range for the table (optional)
# table_range = int(input("Enter the range of the table (default is 10): ") or 10)
#
# # Print the multiplication table
# print(f"\nMultiplication Table for {number}:\n")
# for i in range(1, table_range + 1):
#     print(f"{number} x {i} = {number * i}")


# 7. Program to check if a number is a prime number
# Input a number from the user
# number = int(input("Enter a number: "))

# Check if the number is prime
# if number <= 1:
#     print(f"{number} is not a prime number.")
# else:
#     is_prime = True  # Assume the number is prime
#     for i in range(2, int(number ** 0.5) + 1):  # Check divisors up to the square root of the number
#         if number % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")



# 8.  Program to check if a number is an Armstrong number
# Input a number from the user
# number = int(input("Enter a number: "))
#
# # Convert the number to a string to calculate the number of digits
# num_digits = len(str(number))
#
# # Initialize a variable to store the sum of the digits raised to the power
# sum_of_powers = 0
#
# # Store the original number for comparison
# original_number = number
#
# # Calculate the sum of the digits raised to the power of num_digits
# while number > 0:
#     digit = number % 10  # Extract the last digit
#     sum_of_powers += digit ** num_digits  # Add the digit raised to the power of num_digits
#     number = number // 10  # Remove the last digit
#
# # Check if the sum of powers is equal to the original number
# if sum_of_powers == original_number:
#     print(f"{original_number} is an Armstrong number.")
# else:
#     print(f"{original_number} is not an Armstrong number.")



  # 9. Program to check if a number is a Perfect number
#
# # Input a number from the user
# number = int(input("Enter a number: "))
#
# # Initialize the sum of divisors
# sum_of_divisors = 0
#
# # Find the proper divisors of the number (excluding the number itself)
# for i in range(1, number):
#     if number % i == 0:  # Check if i is a divisor of the number
#         sum_of_divisors += i  # Add the divisor to the sum
#
# # Check if the sum of divisors is equal to the original number
# if sum_of_divisors == number:
#     print(f"{number} is a Perfect number.")
# else:
#     print(f"{number} is not a Perfect number.")


# # 10.  Program to find the second largest number in a list
# # Input: A list of numbers
# numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#
# # Sort the list in ascending order
# numbers.sort()
#
# # Check if there are at least two distinct elements in the list
# if len(numbers) < 2:
#     print("The list does not contain enough elements to find the second largest number.")
# else:
#     # The second largest number is the second last element in the sorted list
#     second_largest = numbers[-2]
#     print(f"The second largest number is: {second_largest}")


# #10.  Given list
# my_list = [1, 2, 3, 4, 5, 8, 9]
#
# # Convert the list to a tuple
# my_tuple = tuple(my_list)
#
# # Print the tuple
# print("The tuple is:", my_tuple)



# Program to count the number of vowels in a string
# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
#
# vowel_count = 0
# for char in string:
#     if char in vowels:
#         vowel_count += 1
#
# print(f"The number of vowels in the string is: {vowel_count}")



# # Program to swap the first and last value of a list
#
# # Input a list from the user
# my_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
#
# # Check if the list has more than one element
# if len(my_list) > 1:
#     # Swap the first and last elements
#     my_list[0], my_list[-1] = my_list[-1], my_list[0]
# else:
#     print("The list must have at least two elements to swap.")
#
# # Output the modified list
# print("The list after swapping the first and last elements is:", my_list)


# import random
#
# random_int = random.randint(1, 10)  # Random integer between 1 and 10
# print("Random integer between 1 and 10:", random_int)


# # Calculate the sum of numbers from 1 to 100
# sum_of_numbers = sum(range(1, 101))
# print("The sum of numbers from 1 to 100 is:", sum_of_numbers)

# result = list("hello")
# print(result)

# # Function to calculate the average of numbers in a list
# def calculate_average(numbers):
#     # Check if the list is not empty to avoid division by zero
#     if len(numbers) == 0:
#         return 0
#     # Calculate the sum of the numbers and divide by the count
#     total_sum = sum(numbers)
#     average = total_sum / len(numbers)
#     return average
#
# # Input: A list of numbers
# # numbers = [10, 20, 30, 40, 50]
# #
# # # Calculate and print the average
# # average = calculate_average(numbers)
# # print("The average of the numbers in the list is:", average)
#
# square = lambda x: x ** 2
# print(square(9))

#
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# for i in range(5):
#     if i == 3:
#         pass
#     print(i)

# import random
#
# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)

#
# text = "SHIREEN, SHRESTHA!"
# lowercase_text = text.lower()
# print(lowercase_text)
# # Output: "hello, world!"
#

#
# my_list = [1, 2, 3]
# my_list.append(4)  # Adds a single item
# my_list.extend([5, 6])  # Adds multiple items
# print(my_list)

# class MyClass:
#     pass


# try:
#     # Code that may raise an exception
#     result = 10 / 0
# except ZeroDivisionError:
#     # Handles specific exception
#     print("Cannot divide by zero.")
# except Exception as e:
#     # Handles any other exceptions
#     print(f"An error occurred: {e}")
# else:
#     # Executes if no exceptions occur
#     print("Operation successful.")
# finally:
#     # Executes regardless of exceptions
#     print("Execution complete.")


#
# str1 = "Shireen"
# str2 = "Shrestha"
# result = str1 + " " + str2
# print(result)  # Output: "Hello World"


#
# words = ["Shireen", "Shrestha"]
# result = " ".join(words)
# print(result)  # Output: "Hello World"

x = 10  # Global variable

def modify_global():
    global x
modify_global()
print(x)
