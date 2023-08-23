# try:
#     total = 5 + "10"
# except (TypeError, ValueError):
#     print("You can't add a string to an int")
#
# # raise ValueError("Custom error message")
#
# class CustomError(Exception):
#     pass
#
# raise CustomError("Our custom error")
#
# # int_value = int("123")
#
# #list = [1, 2, 3]
# #print(list[3])

try:
    total = 5 + "10"
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")