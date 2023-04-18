import pandas as pd
# import logging

class beam():
    def __init__(self, number, L, H):
        self.number = number
        self.L = L
        self.H = H
        global Lm
        Lm = L / self.number

    def read_data(self):
        data = pd.read_excel('DynamicStrain.xlsx', sheet_name='Sheet1')
        return data

    def get_data(self, data, i):
        data_required = data.loc[i]
        # logging.basicConfig(level=logging.INFO,
        #                     format='  %(levelname)s   %(message)s')
        # logging.info(f'Loop NO.{i+1} times ')
        print('\n', f"\033[31mLoop NO.{i+1} times {'='*100}\033[0m")
        return data_required

    def q_calculation(self, data, i):
        Strain = beam.get_data(self, data, i)
        Hm = self.H / 2
        q = Strain.values / Hm
        return q

    def R_calculation(self, q):
        SumQ = 0
        for i in range(self.number):
            SumQ += q[i] * Lm * (self.number - i - 0.5) / self.number
        return SumQ

    def M_calculation(self, SumQ, q):
        # print('SumQ:', SumQ)
        # print('q:', q)
        list_M = []
        for i in range(self.number):
            SumM = -SumQ * Lm * (i+1)
            for j in range(i+1):
                SumM += q[j] * Lm * Lm * (i-j+0.5)
            list_M.append(SumM)
        print('list_M:', list_M)
        return list_M

    def F_calculation(self, SumQ, q):
        list_F = []
        for i in range(self.number):
            SumF = -SumQ
            for j in range(i+1):
                SumF += q[j] * Lm
            list_F.append(SumF)
        # print('list_F:', list_F)
        return list_F



