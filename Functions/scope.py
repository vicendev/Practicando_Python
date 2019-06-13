a = [1,2,3] #global

def f1():
    #global a // error si global a = 100 directamente
    #a = 100 // global example
    a[0] = 5
    print(a)

def f2():
    a = 50 #local
    print(a)

f1()
f2()
print(a)