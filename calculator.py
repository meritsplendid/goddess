# class Calculator:
#     def __init__(self):
#         self.ans = 0

#     def add(self, num1, num2):
#         """Add two numbers."""
#         return num1 + num2

#     def subtract(self, num1, num2):
#         """Subtract two numbers."""
#         return num1 - num2

#     def multiply(self, num1, num2):
#         """Multiply two numbers."""
#         return num1 * num2

#     def divide(self, num1, num2):
#         """Divide two numbers."""
#         if num2 == 0:
#             raise ValueError("Cannot divide by zero!")
#         return num1 / num2

#     def calculate(self):
#         print("Simple Calculator")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")

#         while True:
#             choice = input("Enter choice(1/2/3/4): ")

#             if choice in ('1', '2', '3', '4'):
#                 if self.ans == 0:
#                     num1 = float(input("Enter first number: "))
#                 else:
#                     print(f"Previous answer: {self.ans}")
#                     use_ans = input("Use previous answer? (yes/no): ")
#                     if use_ans.lower() == 'yes':
#                         num1 = self.ans
#                     else:
#                         num1 = float(input("Enter first number: "))

#                 num2 = float(input("Enter second number: "))

#                 if choice == '1':
#                     print(num1, "+", num2, "=", self.add(num1, num2))
#                     self.ans = self.add(num1, num2)

#                 elif choice == '2':
#                     print(num1, "-", num2, "=", self.subtract(num1, num2))
#                     self.ans = self.subtract(num1, num2)

#                 elif choice == '3':
#                     print(num1, "*", num2, "=", self.multiply(num1, num2))
#                     self.ans = self.multiply(num1, num2)

#                 elif choice == '4':
#                     try:
#                         print(num1, "/", num2, "=", self.divide(num1, num2))
#                         self.ans = self.divide(num1, num2)
#                     except ValueError as e:
#                         print(e)

#                 next_calculation = input("Let's do next calculation? (yes/no): ")
#                 if next_calculation.lower() != 'yes':
#                     break

#             else:
#                 print("Invalid Input")

# if __name__ == "__main__":
#     calculator = Calculator()
#     calculator.calculate()
