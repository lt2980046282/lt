import sys

import numpy as np
import numpy.random as rg
a = np.array([2, 3, 4])
print(a)
print(a.dtype)
b = np.array([1.2, 3.5, 5.1])
print(b.dtype)

c = np.array([((1.5, 2, 3), (4, 5, 6))], dtype=complex)
print(c)

d = np.zeros((3, 4))
print(d)

e = np.ones((2, 3, 4), dtype=np.int16)
print(e)

f = np.empty((2, 3))
print(f)
# 参数依次为开始位置，结束位置，生成间隔
e = np.arange(10, 30, 5)
print(e)
g = np.arange(0, 2, 0.3)
print(g)

from numpy import pi

a = np.linspace(0, 2, 9)
print(a)

b = np.linspace(0, 2*pi, 100)
print(b)

# set_printoptions开启打印整个数组
# np.set_printoptions(threshold=sys.maxsize)
c = np.arange(10000).reshape(100, 100)
print(c)

# 基操
a = np.array((0, 45, 90, 180))
b = np.arange(4)
print(b)
# 数组相减 大减小返回正数反之负数
c = a-b
print(c)
# 数组乘方
d = b**3
print(d)
# 数组三角函数运算
e = 10*np.sin(a)
print(e)
# 数组判断
f = a < 35
print(f)
# 数组相乘(合并成新数组)
g = a * b
print(g)
# 数组相乘再相加(一维数组可以生成总和)
h = a @ b
print(h)
# 效果同上
i = a.dot(b)
print(i)

# 一元运算
a = rg.random((2, 3))
print(a)
b = a.sum()
print(b)
c = a.min()
print(c)
d = a.max()
print(d)

# 通用功能
a = np.arange(3)
print(a)
b = np.exp(a)
print(b)
c = np.sqrt(a)
print(c)
b = np.array((2, -1, 4))
d = np.add(a, b)
print(d)
d = a+b
print(d)

# 索引，切片，循环

a = np.arange(10)**3
print(a)
b = a[2]
print(b)
c = a[2:5]
print(c)
a[:6:2] = 1000
print(a)
print(a[::-1])
for i in a:
    print(i**1/3)

# 多维数组


def f(x, y):
    return x*10+y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
print(b[2, 3])
print(b[0:5, 1])
print(b[:, 1])
print(b[1:3])
print(b[-1])
c = np.array([[[0,  1,  2],               # a 3D array (two stacked 2D arrays)
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(c.shape)
print(c[:, 1])
# b。flat
for row in b:
    print(row)


# 改变阵列形状
a = np.floor(10*rg.random((3, 4)))
print(a)
print(a.shape)
print(a.ravel())
print(a.reshape(2, 6))
print(a.T)
a.resize(2, 2, 3)
print(a)
print(a.reshape(4, -1))


a = np.floor(10*rg.random((2, 2)))
b = np.floor(10*rg.random((2, 2)))
c = np.vstack([a, b])
print(c)
d = np.hstack((a, b))
print(d)
from numpy import  newaxis
a = np.column_stack((a, b))
print(a)
b = a[:, newaxis]
print(b)
c = np.column_stack((a[:,newaxis], a[:,newaxis]))
print(c)
d = np.hstack((a[:,newaxis], a[:,newaxis]))   # the result is the same
print(d)