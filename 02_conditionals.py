# age = 25
#
# if age >= 18:
#     print("Adult")

# marks = 60
#
# if marks == 60:
#     print("Pass")

# age = int(input("Write your age: "))
#
# if age >= 18:
#     print("You can vote.")

# password =(input("Enter your password: "))
#
# if password == "python123":
#     print("Access Granted")
# else:
#     print("Wrong Password! Try Again.")

# name = "Riaj"
#
# if name == "Rahim":
#     print("Hello")

# marks = 75
#
# if marks >= 80:
#     print("A")
# elif marks >= 60:
#     print("B")
# else:
#     print("Fail")

# marks = 50
#
# if marks >= 80:
#     print("A")
# elif marks >= 60:
#     print("B")
# else:
#     print("Fail")

# marks = int(input("Enter your marks: "))
#
# if marks >= 40:
#     print("Grade A")
# elif marks >=60:
#     print("Grade B")
# else:
#     print("Fail")

# marks = 90
#
# if marks >= 80:
#     print("Grade B")
# elif marks >= 80:
#     print("Grade A")

# age = 20
#
# if age >= 18:
#     print("Adult")
#
# print("Welcome")
#
# print("End")

                ###Logical Operators (and, or, not)###

# age = 20
# has_id = True
#
# if age >= 18 and has_id:
#     print("You can enter.")

# age = 16
# has_id = True
#
# if age >= 18 and has_id:
#     print("You can enter.")
# else:
#     print("Who are you?")

# day = "Saturday"
#
# if day == "Saturday" or day == "Sunday":
#     print("Holiday")

# logged_in = False
#
# if not logged_in:
#     print("Please log in.")

# age = int(input("Age: "))
# ticket = input("Do you have a ticket? (yes/no): ")
#
# if age >= 18 and ticket == "yes":
#     print("Enjoy the movie!")
#
# else:
#     print("You cannot enter.")

# marks = int(input("Enter marks: "))
#
# if marks >= 60 and marks < 80:
#     print("Grade B")

# logged_in = False
#
# if not logged_in:
#     print("Login Required")

# country = "India"
#
# if country == "Bangladesh" or country == "India":
#     print("South Asia")

# is_raining = True
#
# if not is_raining:
#     print("Go outside")
# else:
#     print("Stay home")

# age = 20
# student = False
#
# if age >= 18 and not student:
#     print("Adult Non-Student")
# else:
#     print("Other")

# number = int(input('Write a Number: '))
# if number % 2 == 0:
#     print("Even Number.")
# else:
#     print("Odd Number.")

# marks = int(input('Write your marks: '))
#
# if marks >= 90:
#     print('A+')
# elif marks >= 80:
#     print('A')
# elif marks >= 60:
#     print('B')
# elif marks >= 40:
#     print('C')
# else:
#     print('Fail.')

# age = int(input("How old are you? "))
# has_id = True
# if age >= 18 and has_id:
#     print("You can vote.")
# else:
#     print("You can not vote.")

# age = int(input("How old are you? "))
# student_check  = input("Are you a student? (yes/no)-- ")
#
# if age >= 18 and student_check == "yes":
#     print("You'll get Student Discount.")
# else:
#     print("Sorry. You cannot get Student Discount.")

# user = input("Would you like to get wet in the rain? (yes/no)---- ")
# if not user == "yes":
#     print("Take your umbrella.")
# else:
#     print("Have fun!")


                    ### Nested if ###

# age = 16
# ticket = "yes"
#
# if age >= 18:
#     if ticket == "yes":
#         print("You can enter.")

# age = 20
# ticket = "no"
#
# if age >= 18:
#     if ticket == "yes":
#         print("You can enter.")
#     else:
#         print("You need a ticket.")
# else:
#     print("You are too young.")

# age = 20
# ticket = "yes"
#
# if age >= 18:
#     if ticket == "yes":
#         print("Allowed")

# age = 15
# ticket = "yes"
#
# if age >= 18:
#     if ticket == "yes":
#         print("Allowed")

# age = int(input("Enter your age: "))
# ticket = input("Do you have a ticket? (yes/no): ")
#
# if age >= 18:
#     if ticket == "yes":
#         print("Welcome!")
#     else:
#         print("Buy a ticket.")
#
# else:
#     print("You are not allowed.")

# age = int(input("Enter your age: "))
#
# if age >= 18:
#     # বয়স ১৮ বা তার বেশি হলেই কেবল টিকিটের প্রশ্ন জিজ্ঞেস করবে
#     ticket = input("Do you have a ticket? (yes/no): ")
#
#     if ticket == "yes":
#         print("Welcome!")
#     else:
#         print("Buy a ticket.")
# else:
#     # ১৮ এর কম হলে সরাসরি এই মেসেজ দেখাবে, টিকিটের কথা জিজ্ঞেসই করবে না
#     print("You are not allowed.")

# age = int(input("Enter your age: "))
#
# if age >= 18:
#     ticket = input("Do you have a ticket? (yes/no): ")
#     if ticket == "yes":
#         print("Welcome!")
#     else:
#         print("Buy a ticket.")
#
# else:
#     print("You are not allowed.")

# age = int(input("How old are you? "))
#
# if age >= 18:
#
#     ticket = input("Do you have a ticket? (yes/no): ")
#     if ticket == "yes":
#         print("Enter")
#     else:
#         print("Please earn money and buy a ticket.")
#
# else:
#     print("Please grow up first.")

# a  = float(input("Enter first number: "))
# b  = float(input("Enter second number: "))
# c = float(input("Enter third number: "))
#
# if  a >= b:
#
#     if a >= c:
#         print("The largest number: ", a)
#     else:
#         print("The largest number: ", c)
#
# else:
#
#     if b >= c:
#         print("The largest number: ", b)
#     else:
#         print("The largest number: ", c)





# age = 20
# ticket = "no"
#
# if age < 18:
#     print("You are too you.")
# else:
#     if ticket == "yes":
#         print("You can enter.")
#     else:
#         print("You need a ticket.")

# age = 20
# has_id = True
#
# if age >= 18:
#     if has_id:
#         print("You can enter.")
#     else:
#         print("You are old enough but we need to check ID.")
#
# else:
#     print("Sorry, you are not old enough.")

# pin_correct = True
# balance = 5000
# withdraw_amount = 2000
#
# if pin_correct:
#     print("PIN Verified.")
#
#     if balance >= withdraw_amount:
#         print("Please collect your cash.")
#     else:
#         print("Insufficient balance.")
#
# else:
#     print("Wrong PIN! Try again")

# age = 18
# passed_test = True
#
# if age >= 18:
#     if passed_test:
#         print("You get the driving license.")
#     else:
#         print("You need to pass the test first.")
#
# else:
#     print("You are too young to drive.")

# total_amount = 1001
# is_premium = False
#
# if total_amount > 1000:
#     if is_premium:
#         print("Free Shipping + 20% Discount!")
#     else:
#         print("Free shipping only.")
#
# else:
#     print("No discount, shipping charge 50 Taka.")

# number = int(input("Write a number: "))
#
# if number >= 0:
#     if number % 2 == 0:
#         print("The number is Even.")
#     else:
#         print("The number is odd.")
#
# else:
#     print("The Number is Negative.")

            ### Ternary expression (এক লাইনে if/else) ###

# age = 20
# status = 'Adult' if age >= 18 else "Minor"
# print(status)

# age = 25
# if 18 <= age <= 60:
#     print("You are in the active age.")

# marks = 89
# if marks > 50:
#     print("Pass!")
# else:
#     print("Fail!")

# marks = 80
# status = "Pass!" if marks > 50 else "Fail!"
# print(status)
#
#                     ### Chained Comparison ###

# age = int(input("Write your age: "))
#
# if 13 <= age <= 19:
#     print("You are a teenager.")
# elif age < 13:
#     print("You are a child.")
# else:
#     print("You are an adult.")











