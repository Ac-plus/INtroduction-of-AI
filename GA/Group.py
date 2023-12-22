import random
import Individual


class Group:
    def __init__(self, group_size, mutation_rate, crossover_rate, dna_length, function):
        '''
        构造函数
        :param group_size: 种群大小
        :param mutation_rate: 变异率
        :param crossover_rate: 交叉率
        :param dna_length: DNA序列长度,即基因长度
        :param function: 要求解的函数
        '''
        self.group_size = group_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.function = function
        self.individuals = []  # 所有个体
        self.best_individual = None  # 最优个体
        self.dna_length = dna_length
        self.init_group()

    def generate_gene(self):
        '''
        生成一个基因序列
        :return: 返回一个由0,1组成的序列
        '''
        gene = []
        for i in range(self.dna_length):
            gene.append(random.randint(0, 1))
        return gene

    def init_group(self):
        '''
        初始化种群的所有个体
        '''
        for i in range(self.group_size):
            self.individuals.append(Individual.Individual(self.generate_gene()))

    def crossover(self, father, mother):
        '''
        交叉
        :param father: 父亲
        :param mother: 母亲
        :return: 孩子
        '''
        gene = [i for i in father.gene]  # 首先默认孩子接收父亲的基因
        child = Individual.Individual(gene)  # 直接传入father.gene会导致更改child的基因时father的基因也会修改，种群基因变得不稳定
        if self.crossover_rate > random.random():  # 判断是否发生交叉
            cross_point = random.randint(1, self.dna_length - 1)  # 交叉发生的位置
            child.gene[cross_point:] = mother.gene[cross_point:]  # 交叉位置后的基因变为母亲的基因
        return child

    def muter(self, individual):
        '''
        变异
        :param individual: 可能变异的个体
        :return: 变异之后的个体或原个体
        '''
        if self.mutation_rate > random.random():  # 判断是否变异
            index = random.randint(0, self.dna_length - 1)  # 变异的位置
            individual.gene[index] = 1 - individual.gene[index]  # 取反
        return individual

    def get_child(self, father, mother):
        '''
        产生一个孩子
        :param father: 父亲
        :param mother: 母亲
        :return: 孩子
        '''
        child = self.crossover(father, mother)
        child = self.muter(child)
        return child

    def calculate_variable(self, x):
        '''
        将0,1序列转换成自变量值域内的一个十进制数
        :param x: 要转换的序列
        :return: 转换后的十进制数
        '''
        r = 0
        for i in range(len(x)):  # 序列的每一位
            r += ((2 ** i) * x[i])  # 乘以权重
        r /= ((2 ** len(x)) - 1)  # 变成0~1之间的小数，相当于一个比例系数
        r *= (self.function.max_variable - self.function.min_variable) + self.function.min_variable  # 控制在函数自变量值域
        return r

    def set_fit(self, individual):
        '''
        求出适应度
        :param individual: 要求的个体
        '''
        x = individual.gene[0:self.dna_length // 2 + 1]  # 基因序列的前面一半代表x，后面一半代表y
        y = individual.gene[self.dna_length // 2 + 1:]
        x = self.calculate_variable(x)  # 计算x，y对应的十进制数值
        y = self.calculate_variable(y)
        r = self.function.function(x, y)  # 计算适应度
        individual.fit = r

    def select_next_generation(self):
        '''
        选择合适的下一代
        :return: 下一代
        '''
        for i in range(len(self.individuals)):  # 计算所有个体的适应度，应注意此时个体数量已经是种群大小的两倍
            self.set_fit(self.individuals[i])
        self.individuals.sort(key=lambda individual: individual.fit, reverse=not self.function.find_min)  # 按适应度排列
        self.best_individual = self.individuals[0]  # 排在越前的个体越符合要求
        new_individuals = self.individuals[0:self.group_size]  # 选择种群大小数量的个体
        return new_individuals

    def get_next_generation(self):
        '''
        获取下一代
        '''
        next_generation = []
        for i in range(self.group_size):  # 每个个体与一个随机个体繁衍
            father = self.individuals[i]
            mother = self.individuals[random.randint(0, self.group_size - 1)]
            child = self.get_child(father, mother)
            next_generation.append(child)
        self.individuals += next_generation  # 此时的种群数量已经变为两倍
        self.individuals = self.select_next_generation()  # 选择出其中更符合要求的一半群体

    def print_best_individual_info(self):
        '''
        打印相关信息
        '''
        x = self.best_individual.gene[0:self.dna_length // 2 + 1]
        y = self.best_individual.gene[self.dna_length // 2 + 1:]
        x = self.calculate_variable(x)
        y = self.calculate_variable(y)
        print("x:", x, " y:", y, " Result:", self.best_individual.fit)

    def start_evolution(self, generation):
        '''
        开始繁衍进化
        :param generation: 要繁衍的代数
        '''
        for i in range(generation):
            print("Gen", i + 1, "best individual", end="\t")
            self.get_next_generation()
            self.print_best_individual_info()

