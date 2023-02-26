# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#         elif a < b:
#             a, b = b, a
#         return func(a, b)
#     return inner
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(2,5)
#
# divide(2,0)

# def outer_function():
#
#     def inner_function():
#
#         print('I came from the inner function.')
#
#     # Executing the inner function inside the outer function.
#     inner_function()
# outer_function()
# def friendly_reminder(func):
#     '''Reminder for husband'''
#
#     func()
#     print('Don\'t forget to bring your wallet!')
#
# def action():
#
#     print('I am going to the store buy you something nice.')
#
# friendly_reminder(action)
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)

# printer("Hello")
from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-" * 30}')
        func()
        print("Hello")
    return wrapper


@log_datetime
def daily_backup():
    print('Daily backup job has finished.')


daily_backup()


