# from magic_eight_ball import get_eight_ball_response
# question = input("Ask the Magic Eight Ball a question: ")

# try:
#     if not question.strip():
#         raise ValueError("Question cannot be empty.")
#     answer = get_eight_ball_response()
#     print(f'Magic Eight Ball says: {answer}')
# except ValueError as error:
#     print(error)

# balance = 500.00
# print("Welcome to the Bank!")

# while True:
#     print("\n1.Check balance:")
#     print("2.Deposit money:")
#     print("3.Withdraw money:")
#     print("4.Exit")

#     option = input("Choose an option: ")
#     match option:
#         case "1": 
#             print(f"Your balance is: ${balance:.2f}")
#         case "2":
#             try:
#                 amount = float(input("Enter amount to deposit: "))
#                 if amount <= 0:
#                     raise ValueError("Deposit amount must be positive.")
#                 balance += amount
#                 print(f"Deposited: ${amount:.2f}. New balance: ${balance:.2f}")
#             except ValueError as error:
#                 print(error)
#         case "3":
#             try:
#                 amount = float(input("Enter amount to withdraw: "))
#                 if amount <= 0:
#                     raise ValueError("Withdrawal amount must be positive.")
#                 if amount > balance:
#                     raise ValueError("Insufficient funds.")
#                 balance -= amount
#                 print(f"Withdrew: ${amount:.2f}. New balance: ${balance:.2f}")
#             except ValueError as error:
#                 print(error)
#         case "4":
#             print("Thank you for using the bank!")
#             break
#         case _:
#             print("Invalid option. Please choose again.")

print("Temperature Converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
option = input("Choose an option: ")

try:
    temperature = float(input("Enter the temperature: "))

    match option:
        case "1":
            result = (temperature * 9 / 5) + 32
            print(f"{temperature}°C is {result:.2f}°F")
        case "2":
            result = (temperature - 32) * 5 / 9
            print(f"{temperature}°F is {result:.2f}°C")
        case "3":
            result = temperature + 273.15
            print(f"{temperature}°C is {result:.2f}K")
        case _:
            print("Invalid option. Please choose again.")
except ValueError:
    print("Please enter a valid number.")