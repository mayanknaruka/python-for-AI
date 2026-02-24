print('hello')

# for i in range(1,10):
#     print("hello", i)
  

# def hello():
#     for i in range(10):
#         print("hello")

# hello()


def hello(n):
    if n == 0:
        return
    print("hello world")
    hello(n - 1)

hello(10)