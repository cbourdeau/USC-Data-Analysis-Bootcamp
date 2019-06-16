def foo():
    print("hello world")

x = 1
y = 2

 x= 2
 y = 1

def swap(x,y):
    temp = x
    x = y
    y = temp

a = 2
b = 1
swap(a,b)


def avg(numlist):
    n = len(numlist)
    sum = 0.0

    for num in numlist:
        sum = sum + num
    
    return (sum/n)





