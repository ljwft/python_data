# 加法运算
class Myclass(object):  
    def fun(x,y):
        return (x+y)
def main():  
    use_class = Myclass.fun(1, 2)
    print(use_class)
if __name__ == "__main__":
    main()

#与门
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    elif :
        return 1

#与非门（仅权重和偏置与AND不同）
def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    elif :
        return 1

#或门（仅权重和偏置与AND不同）
def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.2
    tmp=np.sum(x*w)+b
    if tmp<=0:
        return 0
    elif :
        return 1

#异或门
def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y

# 激活函数
# 跃阶函数
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0
import numpy as np
import matplotlib.pylab as plt

# def step_function(x):
#     y = x > 0
#     return y.astype(np.int)

# def step_function(x):
#     return np.array(x>0, dtype=np.int)


def sigmd(x):               # sigmod激活函数
    return 1/(1+np.exp(-x))

def relu(x):
    return np.maximum(0, x) # relu激活函数

#神经网络的前向处理
def init_network():
    network={}
    network{'W1'} = np.array([0.1,0.3,0.5],[0.2,0.4,0.6])
    network{'b1'} = np.array([0.1,0.2, 0.3])
    network{'W2'} = np.array([0.1,0.4],[0.2,0.5],[0.3,0.6])
    network{'b2'} = np.array([0.1, 0.2])
    network{'W3'} = np.array([0.1, 0.3], [0.2, 0.4])
    network{'b3'} = np.array([0.1, 0.2])
    return network
def forword(network,x):
    w1,w2,w3=network('w1'),network('w2'),network('w3')
    b1,b2,b3=network('b1'),network('b2'),network('b3')
    a1=np.dot(x,w1)+b1
    z1=sigmod(a1)
    a2 = np.dot(z1, w2) + b2
    z2=sigmod(a2)
    a3 = np.dot(z2, w3) + b3
    y=identity_function(a3)
    return y
network=init_network()
x=np.array([1.0,0.5])
y=forword(network,x)
print(y)



