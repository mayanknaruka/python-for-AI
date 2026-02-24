print('hello')

# for i in range(1,10):
#     print("hello", i)
  

# def hello():
#     for i in range(10):
#         print("hello")

# hello()


# def hello(n):
#     if n == 0:
#         return
#     print("hello world")
#     hello(n - 1)

# hello(10)

def print(n, sum):
    if n == 0:
        sum = sum + 1
        print(n-1, sum)           # recursive call with negative number
        sum = 0
        print (print(10, sum))    # very wrong — nested print + function returns None