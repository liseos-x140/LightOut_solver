import random
import numpy as np
import matplotlib.pyplot as plt


class bord:
    def __init__(self, n, m):
        self.n_size = n
        self.m_size = m
        init_state = random.sample(range(n*m), k=random.randint(1,n*m))
        self.state = [True if i in init_state else False for i in range(n*m)]
    
    def display(self):
        return 1