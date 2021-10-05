# 1 Digite este exemplo em um script e teste-o.

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')
    
do_twice(print_spam)