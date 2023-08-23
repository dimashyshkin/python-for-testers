# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# file = open('text2.txt', 'w')
# file.write("Hello, Python! It's Dmitry here.")
# file.close()

try:
    with open('text3.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("The file text3.txt does not exist")

with open('C:/Users/Dmitry/PycharmProjects/pythonForTestersProject/files/text.txt', 'r') as file:
    print(file.read())