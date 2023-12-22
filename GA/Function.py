# Function.py
class Function:
    def __init__(self, function, max_variable, min_variable, find_min=True):
        '''
        构造函数
        :param function: 要求解的函数
        :param max_variable: 函数自变量的最大值
        :param min_variable: 函数自变量的最小值
        :param find_min: 求最小值，默认为True，False即为求最大值
        '''
        self.function = function
        self.max_variable = max_variable
        self.min_variable = min_variable
        self.find_min = find_min

