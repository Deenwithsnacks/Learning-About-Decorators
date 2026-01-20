# def add(a, b):
#     return a + b


# sum = add
# print(sum(1, 2))

# def outer():
#     print("This runs first")
    
#     def inner():
#         print("This runs second")
    
#     inner()
    
# outer()

# def parent():
#     print("come here child")
    
#     def child():
#         print("im coming oo")

#     child()

# # parent()

# new_parent = parent
# new_parent()


# def outer():
#     def inner():
#         print("i am returned")
#     return inner

# # outer()()

# my_func = outer()
# my_func()

def me_winning():
    def python_hype():
        print("Python is cool")
    return python_hype

hype = me_winning()
hype()
