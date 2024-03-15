################################################
#           spacing and indentation
################################################

x = 1
+ 2
print(x)        # 1

x = 1 \
    + 2
print(x)        # 3


def say_hello():
    print("Hello there!")


print(say_hello())
# Hello there!
# None


def say_hello2():
    print("Hello there!")


print(say_hello2())
# Hello there!
# None


# def say_hello():
# print("Hello there!")     # incorrect


#     def say_hello():
# print("Hello there")      # incorrect
