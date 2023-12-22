import Group
import Function
import math


def function(x, y):  # 要求解的函数
    return 20 + (x ** 2) + (y ** 2) - 10 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))


if __name__ == '__main__':
    func = Function.Function(function, 5, -5, find_min=True) 
    group = Group.Group(300, 0.05, 0.8, 128, func)  
    group.start_evolution(100)

