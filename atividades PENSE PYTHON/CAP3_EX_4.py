#Use a versão alterada de do_twice para chamar print_twice duas vezes, passando
#'spam' como um argumento.


def do_twice(func, arg):
    func(arg)
    func(arg)
    
def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print, 'spam')
print('')
