def cube(x):
    return x*x*x


# print(cube(3))

l = [1,2,3,4,5,6,7]

newn = list(map(cube,l))

print(newn)

# filter


def felter_f(a):
    return a > 4
e = list(filter(felter_f,l))

print(e)
