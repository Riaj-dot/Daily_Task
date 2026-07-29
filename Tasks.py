# age = input("How old are you? ")
# print(type(age))

# age = input("How old are you? ")
# print (age + age)

# age = int(input("How old are you? "))
# print((age))
# print(type(age))

                    ### Condition Tasks ###

# number = 7
# if number % 2 == 0:
#     print("The Number is Even.")
# else:
#     print("The Number is Odd.")

# marks = 75
# if marks >= 80:
#     print("A+")
# elif marks >= 50:
#     print("Pass.")
# else:
#     print("Fail.")

# signal = "Red"
# if signal == "Red":
#     print("Stop!")
# elif signal == "Yellow":
#     print("Slow Down!")
# elif signal == "Green":
#     print("Go!")
# else:
#     print("Invalid signal!")

# age = 20
# has_ticket = True
# if age >= 18 and has_ticket:
#     print("You can enter.")
# else:
#     print("You cannot enter.")

# has_coupon = False
# is_member = True
# if has_coupon or is_member:
#     print("You got a discount.")
# else:
#     print("No discount.")

# is_raining = False
#
# if not is_raining:
#     print("Go outside!")
# else:
#     print("Stay home.")

# cgpa = 3.9
# attendance = 92
#
# if cgpa >= 3.8 and attendance >= 90:
#     print("You got the scholarship.")
# else:
#     print("Scholarship not granted.")

# is_student = True
# age = 65
#
# if is_student or age > 60:
#     print("You get a 50% discount.")
# else:
#     print("Regular fare applies.")

# is_holiday = False
#
# if not is_holiday:
#     print("Go to work!")
# else:
#     print("Enjoy your day off.")

# weight = float(input("Enter your weight (kg)--- "))
# height = float(input("Enter your height (m)--- "))
#
# BMI = weight / (height * height)
#
# print("-" * 30)
# print("Your BMI is--", BMI)
#
# if BMI < 18.5:
#     print("Underweight")
# elif BMI < 25:
#     print("Normal.")
# elif  BMI < 30:
#     print("Overweight")
# else:
#     print("Obese")

# num1 = int(input("Write first number: "))
# num2 = int(input("Write second number: "))
#
# if (num1 % 2 == 0 and num2 % 2 == 0) or (num1 > 100 or num2 > 100):
#     print("শর্ত পূরণ হয়েছে।")
# else:
#     print("শর্ত পূরণ হয়নি।")

# num1 = int(input("Write the first number: "))
# num2 = int(input("Write the second number:"))
#
# if (num1 % 2 == 0 and num2 % 2== 0) or (num1 > 100 or num2 > 100):
#     print("The condition is fulfilled.")
# else:
#     print("The condition is not fulfilled.")

balance = 5000

user_pin = int(input("Enter Your PIN: "))

if user_pin != 1234:
    print("Incorrect PIN.")
else:
    print("1. Check Balance")
    print("2. Withdraw Money")

    option = int(input("Please select an option (1/2): "))

    if option == 1:
        print("Your balance is:", balance)
    elif option == 2:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount

            print("Transaction Successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance!")

    else:
        print("Invalid Option!")






































