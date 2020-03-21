import re


def demo(**args_v):
    for k, v in args_v.items():
        print(k, v)


demo(name='ngcx')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def dn(a):
    return a < 10


ls = filter(dn, a)
ls = [i for i in a if i > 1]
print(ls)
re.compile()