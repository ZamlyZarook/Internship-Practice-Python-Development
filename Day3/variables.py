
x = 'global x'

def test():
    global x
    x = 'local x'
    print(x)


test()
print(x)


import builtins

print(dir(builtins))