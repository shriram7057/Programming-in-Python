#Fun with return Statement
# Every python function by default returns a value is none
# We can use return statement to return a ANY TYPE of value from a function

# def add(a,b):
#     ans=a+b
#     return ans
# print(add(10,20))
#
# total=add(10,20)
# print(total)

# def luckyNumber():
#     print("lucky Number function starts")
#     return 10
#     return 20
#     print("lucky Number function ends")
# print(luckyNumber())
#
# def add(a, b):
#     ans = a + b
#     print(ans)
#     return ans     # you forgot to return the value
#
# def div(a, b):
#     ans = a / b
#     print(ans)
#     return ans     # you also need to return the value
#
# def square(n):
#     ans = n * n
#     return ans
#
# print(square(div(add(20, 30), 2)))

x=10
def fun1():
    y=20
    print("locally inside the fun1 ,x=",x)
    print("locally inside the fun1 ,y=",y)
fun1()
print("Globally ,outside the fun  x=",x)
print("Globally ,outside the fun  y=",y)
