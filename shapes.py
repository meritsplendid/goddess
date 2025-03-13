# # ##################################inverted right triangle###############################
# n = 7
# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print("  ", end=" ")
#     for k in range(i):
#         print("*  ", end="")
#     print()



# n = 7
# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print(" # ", end=" ")
#     for k in range(i):
#         print(" # ", end=" ")
#     print()


    # n = 7
# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print("  ", end=" ")
#     for k in range(i):
#         print("#  ", end="")
#     print()

# n = 7
# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print("", end="")
#     for k in range(i):
#         print("*  ", end="")
#     print()



# n = 9
# for i in range(n):
#     for j in range(n-i):
#         print("  ", end = "")
#     for k in range(i):
#         print("*   ", end = "")
#     print()
# n-=1   
# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print("  ", end = "")
#     for k in range(i):
#         print(" *  ", end ="")
#     print()






# # #star in heart form
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("* ", end=" ")
#         else:
#             print("  ", end="")
#     print()



# for row in range(5):
#     for col in range(6):
#         if (row+col==3) or (row==0 and col%3==0) or (row==1 and col%3==1) or (row==2 and col%3==1) or (row==3 and col%3==1) or (col+row==7):
#             print(" * ", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# def multiply(num1, num2, *num3):
#     x = [*num3]
#     result =num1 * num2
#     for i in x:
#         result = result * i
#     return result

# print(multiply(3,7, 8, 9))


# def myfunc(fname, lname):
#     return f"Good afternoon {fname} {lname}"

# print(myfunc("Merit"))